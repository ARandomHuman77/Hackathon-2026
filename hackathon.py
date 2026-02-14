import pygame, sys, os
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import random

os.chdir(os.path.dirname(__file__))

pygame.mixer.pre_init(44100, -16, 2, 256)
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)


# [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean, German, Swedish]

chinese_word_bank = {
    "Hello": ["你好","nǐ hǎo"],
    "Good morning": ["早上好", "zǎo shang hǎo"],
    "Good afternoon": ["下午好", "xià wǔ hǎo"],
    "Good evening": ["晚上好", "wǎn shang hǎo"],
    "Thank you": ["谢谢", "xiè xie"],
}
hindi_word_bank = {
    "Hello": "नमस्ते",
    "Goodbye": "अलविदा",
    "Please": "कृपया",
    "Thank you": "धन्यवाद",
    "Yes": "हाँ",
    "No": "नहीं",
    "Excuse me": "माफ़ कीजिए",
    "Sorry": "माफ़ करना",
}
french_word_bank = {
    "Hello": "Bonjour"
}
hebrew_word_bank = {
    "Hello": "שלום"
}
spanish_word_bank = {
    "Hello": "Hola"
}
tamil_word_bank = {
    "Hello": "வணக்கம்"
}
japanese_word_bank = {
    "Hello": "こんにちは"
}
korean_word_bank = {
    "Hello": "안녕하세요"
}
german_word_bank = {
    "Hello": "Hallo"
}
swedish_word_bank = {
    "Hello": "Hej"
}

language_to_index = {
    "Chinese": 0,
    "Hindi": 1,
    "French": 2,
    "Hebrew": 3,
    "Spanish": 4,
    "Tamil": 5,
    "Japanese": 6,
    "Korean": 7,
    "German": 8,
    "Swedish": 9
}


languages = []
show_pinyin = False
lang_index = 0
language_list = ["Chinese", "Hindi", "French", "Hebrew", "Spanish", "Tamil", "Japanese", "Korean", "German", "Swedish"]


answer_counter = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lost In Translation")
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.SysFont("Times New Roman", 58)
body_font = pygame.font.SysFont("Times New Roman", 25)
button_font = pygame.font.SysFont("Times New Roman", 29)
counter_font = pygame.font.SysFont("Times New Roman", 30)
font_latin = pygame.font.Font("NotoSans-VariableFont_wdth.ttf", 25)
font_pinyin = pygame.font.Font("NotoSans-VariableFont_wdth.ttf", 18)

# Language-specific fonts (ensure font files exist!)
# Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean
try:
    font_chinese = pygame.font.Font("NotoSansSC-VariableFont_wght.ttf", 25)
    font_hindi = pygame.font.Font("NotoSansDevanagari-VariableFont_wdth.ttf", 25)
    font_hebrew = pygame.font.Font("NotoSansHebrew-VariableFont_wdth.ttf", 25)
    font_tamil = pygame.font.Font("NotoSansTamil-VariableFont_wdth.ttf", 25)
    font_japanese = pygame.font.Font("NotoSansJP-VariableFont_wght.ttf", 25)
    font_korean = pygame.font.Font("NotoSansKR-VariableFont_wght.ttf", 25)
except pygame.error as e:
    print(f"Warning: Missing language fonts - {e}")
    font_chinese = font_hindi = font_hebrew = font_tamil = font_japanese = font_korean = pygame.font.SysFont("arial", 25)


# UI Layout (MENU BUTTONS - text-based)
rules_box = pygame.Rect(60, 140, 680, 220)
start_button_rect = pygame.Rect(WIDTH // 2 - 140, 350, 120, 50)  # Rename to avoid collision
quit_button_rect = pygame.Rect(WIDTH // 2 + 20, 350, 120, 50)    # Text-based quit button (Rect)

# Background
try:
    background = pygame.image.load("galaxy_background_proper.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error loading background: {e}")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(PURPLE)

# Answer boxes
boulder_size = 120
boulder_y = -boulder_size
answer_boxes = [
    pygame.Rect(100 + i * 160, boulder_y, boulder_size, boulder_size)
    for i in range(4)
]

# Boulder image
try:
    boulder_image = pygame.image.load("space_boulder_proper.png").convert_alpha()
    boulder_image = pygame.transform.scale(boulder_image, (boulder_size, boulder_size))
except pygame.error as e:
    print(f"Error loading boulder: {e}")
    boulder_image = pygame.Surface((boulder_size, boulder_size))
    boulder_image.fill((100, 100, 100))


# UFO Class
class Ufo:
    def __init__(self, startX, startY, width, height):
        try:
            self.image = pygame.image.load("ufo_proper.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        except pygame.error as e:
            print(f"Error loading UFO: {e}")
            self.image = pygame.Surface((width, height))
            self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY

# IMAGE-BASED QUIT BUTTON CLASS (for game over screen)
class ImageQuitButton:  # Rename to avoid confusion with text quit button
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        screen.blit(self.image, self.rect.topleft)
    
    def check_click(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Game Over Screen Functions
def load_ending_image(image_path, screen_size):
    try:
        ending_image = pygame.image.load(image_path).convert_alpha()
        ending_image = pygame.transform.scale(ending_image, screen_size)  # Resize to fit screen
        return ending_image
    except pygame.error as e:
        print(f"Error loading ending image: {e}")
        fallback_bg = pygame.Surface(screen_size)
        fallback_bg.fill((30, 30, 60))
        return fallback_bg

# Load Game Over Assets
ending_image = load_ending_image("HAHA! Loser!!.png", (WIDTH, HEIGHT))

# Load Image Quit Button (for game over screen)
try:
    quit_img = pygame.image.load("Quit end.png").convert_alpha()
    quit_img = pygame.transform.scale(quit_img, (150, 70))  # Resize for visibility
except pygame.error as e:
    print(f"Error loading quit image: {e}")
    quit_img = pygame.Surface((150, 70))
    quit_img.fill((255, 0, 0))

# Load Play Again Button Image (game over screen)
try:
    again_img = pygame.image.load("Again.png").convert_alpha()
    again_img = pygame.transform.scale(again_img, (180, 80))
except pygame.error as e:
    print(f"Error loading again image: {e}")
    again_img = pygame.Surface((180, 80))
    again_img.fill((0, 255, 0))

# Create Image Quit Button Instance (game over screen)
game_over_quit_button = ImageQuitButton(
    x=WIDTH // 2 - quit_img.get_width()// 2 + 40 ,  # Center horizontally
    y=HEIGHT // 2 - 50,                        # Below game over image
    image=quit_img
)

# Create Image Again Button Instance (game over screen)
play_again_button = ImageQuitButton(
    x=game_over_quit_button.rect.x + game_over_quit_button.rect.height + 80,
    y=game_over_quit_button.rect.y - 5,
    image=again_img
)

# Game Functions
def get_random_word():
    if len(languages) > 0:
        lang_num = random.randint(0, len(languages)-1)
        correct_lang = languages[lang_num]
        lang_index = language_to_index[correct_lang]
        language = language_list[lang_index]
        correct_pinyin = None
        # [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean, German, Swedish]
        if language == "Chinese":
            english_word = random.choice(list(chinese_word_bank.keys()))
            correct_translation = chinese_word_bank[english_word][0]
            correct_pinyin = chinese_word_bank[english_word][1]
        elif language == "Hindi":
            english_word = random.choice(list(hindi_word_bank.keys()))
            correct_translation = hindi_word_bank[english_word]
        elif language == "French":
            english_word = random.choice(list(french_word_bank.keys()))
            correct_translation = french_word_bank[english_word]
        elif language == "Hebrew":
            english_word = random.choice(list(hebrew_word_bank.keys()))
            correct_translation = hebrew_word_bank[english_word]
        elif language == "Spanish":
            english_word = random.choice(list(spanish_word_bank.keys()))
            correct_translation = spanish_word_bank[english_word]
        elif language == "Tamil":
            english_word = random.choice(list(tamil_word_bank.keys()))
            correct_translation = tamil_word_bank[english_word]
        elif language == "Japanese":
            english_word = random.choice(list(japanese_word_bank.keys()))
            correct_translation = japanese_word_bank[english_word]
        elif language == "Korean":
            english_word = random.choice(list(korean_word_bank.keys()))
            correct_translation = korean_word_bank[english_word]
        elif language == "German":
            english_word = random.choice(list(german_word_bank.keys()))
            correct_translation = german_word_bank[english_word]
        elif language == "Swedish":
            english_word = random.choice(list(swedish_word_bank.keys()))
            correct_translation = swedish_word_bank[english_word]
        
        return english_word, language, correct_translation, correct_pinyin

def generate_answers(correct_translation, language):
    answers = [correct_translation]
    while len(answers) < 4:
        if language == "Chinese":
            random_word = random.choice(list(chinese_word_bank.keys()))
            wrong_translation = chinese_word_bank[random_word][0]
        elif language == "Hindi":
            random_word = random.choice(list(hindi_word_bank.keys()))
            wrong_translation = hindi_word_bank[random_word]
        elif language == "French":
            random_word = random.choice(list(french_word_bank.keys()))
            wrong_translation = french_word_bank[random_word]
        elif language == "Hebrew":
            random_word = random.choice(list(hebrew_word_bank.keys()))
            wrong_translation = hebrew_word_bank[random_word]
        elif language == "Spanish":
            random_word = random.choice(list(spanish_word_bank.keys()))
            wrong_translation = spanish_word_bank[random_word]
        elif language == "Tamil":
            random_word = random.choice(list(tamil_word_bank.keys()))
            wrong_translation = tamil_word_bank[random_word]
        elif language == "Japanese":
            random_word = random.choice(list(japanese_word_bank.keys()))
            wrong_translation = japanese_word_bank[random_word]
        elif language == "Korean":
            random_word = random.choice(list(korean_word_bank.keys()))
            wrong_translation = korean_word_bank[random_word]
        elif language == "German":
            random_word = random.choice(list(german_word_bank.keys()))
            wrong_translation = german_word_bank[random_word]
        elif language == "Swedish":
            random_word = random.choice(list(swedish_word_bank.keys()))
            wrong_translation = swedish_word_bank[random_word]
        if wrong_translation not in answers:
            answers.append(wrong_translation)
    random.shuffle(answers)
    return answers

def get_font_for_language(language):
    if language == "Chinese":
        return font_chinese
    elif language == "Hindi":
        return font_hindi
    elif language == "Hebrew":
        return font_hebrew
    elif language == "Tamil":
        return font_tamil
    elif language == "Japanese":
        return font_japanese
    elif language == "Korean":
        return font_korean
    else:
        return font_latin

        # [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean]


def draw_button(screen, rect, label, font, fill_colour, text_colour):
    pygame.draw.rect(screen, fill_colour, rect, border_radius=8)
    pygame.draw.rect(screen, PURPLE, rect, width=2, border_radius=8)
    text_surf = font.render(label, True, text_colour)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

# Create UFO Object
player_ufo = Ufo(300, 470, 200, 170)

max_boulder_speed = 1.0

shots = [] 
bullet_speed = 10
boulder_speeds = [random.uniform(0.75, max_boulder_speed) for _ in answer_boxes]

# boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]

boulder_angles = [0 for _ in answer_boxes]  # initial rotation for each boulder
boulder_rotation_speeds = [random.uniform(-5, 5) for _ in answer_boxes]  # degrees per frame

# Game States
running = True
game_on = False
game_over = False  # New state for game over screen


sad_song_files = ["meow.wav", "rickroll_proper.wav", "communism.wav", "orphans.wav"]

# Variable that keeps track if the music is playing
end_music_playing = False


pew_sound = pygame.mixer.Sound("pew.wav")
pew_sound.set_volume(0.5)



# Game State Initialization


# language button format
chinese_rect = pygame.Rect(50, 410, 120, 50)
hindi_rect = pygame.Rect(180, 410, 120, 50)
french_rect = pygame.Rect(180, 470, 120, 50)
hebrew_rect = pygame.Rect(180, 530, 120, 50)
spanish_rect = pygame.Rect(50, 530, 120, 50)
tamil_rect = pygame.Rect(310, 410, 120, 50)
japanese_rect = pygame.Rect(310, 470, 120, 50)
korean_rect = pygame.Rect(310, 530, 120, 50)
german_rect = pygame.Rect(440, 410, 120, 50)
swedish_rect = pygame.Rect(440, 470, 120, 50)

pinyin_rect = pygame.Rect(60, 460, 100, 30)

# boulder speeds button format
min_speed = pygame.Rect(680, 450, 120, 50)
med_speed = pygame.Rect(680, 500, 120, 50)
max_speed = pygame.Rect(680, 550, 120, 50)

# [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean] 



# Main Game Loop
while running:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        # MOUSE CLICKS
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # MENU STATE (game_on = False, game_over = False)
            if not game_on and not game_over:
                if len(languages) > 0:
                    if start_button_rect.collidepoint(event.pos):
                        game_on = True
                        english_word, language, correct_translation, correct_pinyin = get_random_word()
                        # lang_index = languages.index(language)
                        
                        answers = generate_answers(correct_translation, language)
                elif quit_button_rect.collidepoint(event.pos):
                    running = False
                if chinese_rect.collidepoint(event.pos):
                    if "Chinese" not in languages:
                        languages.append("Chinese")
                        print(languages)
                    else:
                        languages.remove("Chinese")
                        print(languages)
                elif hindi_rect.collidepoint(event.pos):
                    if "Hindi" not in languages:
                        languages.append("Hindi")
                        print(languages)
                    else:
                        languages.remove("Hindi")
                        print(languages)
                elif french_rect.collidepoint(event.pos):
                    if "French" not in languages:
                        languages.append("French")
                        print(languages)
                    else:
                        languages.remove("French")
                        print(languages)
                elif hebrew_rect.collidepoint(event.pos):
                    if "Hebrew" not in languages:
                        languages.append("Hebrew")
                        print(languages)
                    else:
                        languages.remove("Hebrew")
                        print(languages)
                elif spanish_rect.collidepoint(event.pos):
                    if "Spanish" not in languages:
                        languages.append("Spanish")
                        print(languages)
                    else:
                        languages.remove("Spanish")
                        print(languages)
                elif tamil_rect.collidepoint(event.pos):
                    if "Tamil" not in languages:
                        languages.append("Tamil")
                        print(languages)
                    else:
                        languages.remove("Tamil")
                        print(languages)
                elif japanese_rect.collidepoint(event.pos):
                    if "Japanese" not in languages:
                        languages.append("Japanese")
                        print(languages)
                    else:
                        languages.remove("Japanese")
                        print(languages)
                elif korean_rect.collidepoint(event.pos):
                    if "Korean" not in languages:
                        languages.append("Korean")
                        print(languages)
                    else:
                        languages.remove("Korean")
                        print(languages)
                elif german_rect.collidepoint(event.pos):
                    if "German" not in languages:
                        languages.append("German")
                        print(languages)
                    else:
                        languages.remove("German")
                        print(languages)
                elif swedish_rect.collidepoint(event.pos):
                    if "Swedish" not in languages:
                        languages.append("Swedish")
                        print(languages)
                    else:
                        languages.remove("Swedish")
                        print(languages)
                elif min_speed.collidepoint(event.pos):
                    if not max_boulder_speed == 1.0:
                        max_boulder_speed = 1.0
                elif med_speed.collidepoint(event.pos):
                    if not max_boulder_speed == 1.5:
                        max_boulder_speed = 1.5
                elif max_speed.collidepoint(event.pos):
                    if not max_boulder_speed == 2.0:
                        max_boulder_speed = 2.0
                elif pinyin_rect.collidepoint(event.pos):
                    show_pinyin = not show_pinyin


# [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean] 
        
            
            # GAME OVER STATE (game_over = True)
            elif game_over:
                # Check click on image quit button
                if game_over_quit_button.check_click(event):
                    running = False
        
        
        elif game_on and not game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(player_ufo.rect.centerx - 5, player_ufo.rect.y + 60, 10, 10)
                shots.append(bullet_rect)
                pew_sound.play()

    # UFO Movement (only in game state)
    if game_on and not game_over:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_ufo.rect.x > 0:
            player_ufo.rect.x -= 5
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_ufo.rect.x < WIDTH - player_ufo.rect.width:
            player_ufo.rect.x += 5


    # Displays the screen
    screen.blit(background, (0, 0))

    # MENU STATE
    if not game_on and not game_over:
        # Title
        title_surf = title_font.render("Lost in Translation", True, WHITE)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, 70))
        screen.blit(title_surf, title_rect)

        # Rules Box
        pygame.draw.rect(screen, WHITE, rules_box, border_radius=12)
        pygame.draw.rect(screen, PURPLE, rules_box, width=2, border_radius=12)

        # Rules Text
        rules_lines = [
            "Rules:",
            "1.) Select the language(s) you would like to translate",
            "     English words into",
            "2.) Guess wrong and the game ends! (RIP UFO)",
            "3.) You might want friends who speak different languages",
            "4.) Use a/d to move and space to shoot. Have fun!( ͡° ͜ʖ ͡°)"
        ]


        line_y = rules_box.top + 20
        for line in rules_lines:
            text_surf = body_font.render(line, True, BLACK)
            text_rect = text_surf.get_rect(centerx=rules_box.centerx, y=line_y)
            screen.blit(text_surf, text_rect)
            line_y += 28

        # Menu Buttons (text-based)
        # Hover effect for start button
        start_colour = (180, 0, 180) if start_button_rect.collidepoint(mouse_pos) else PURPLE
        draw_button(screen, start_button_rect, "Start", button_font, start_colour, WHITE)
        
        # Hover effect for quit button
        quit_colour = (180, 0, 180) if quit_button_rect.collidepoint(mouse_pos) else PURPLE
        draw_button(screen, quit_button_rect, "Quit", button_font, quit_colour, WHITE)

        # Languages buttons
        if "Chinese" in languages:
            chinese_colour = (25, 25, 25)
        elif chinese_rect.collidepoint(mouse_pos):
            chinese_colour = (180, 0, 180)
        else: 
            chinese_colour = PURPLE
        draw_button(screen, chinese_rect, "Chinese", button_font, chinese_colour, WHITE)

        if show_pinyin:
            pinyin_colour = (25, 25, 25)
        elif pinyin_rect.collidepoint(mouse_pos):
            pinyin_colour = (180, 0, 180)
        else:
            pinyin_colour = PURPLE

        draw_button(screen, pinyin_rect, "Pinyin?", button_font, pinyin_colour, WHITE)

        if "Hindi" in languages:
            hindi_colour = (25, 25, 25)
        elif hindi_rect.collidepoint(mouse_pos):
            hindi_colour = (180, 0, 180)
        else: 
            hindi_colour = PURPLE
        draw_button(screen, hindi_rect, "Hindi", button_font, hindi_colour, WHITE)

        if "French" in languages:
            french_colour = (25, 25, 25)
        elif french_rect.collidepoint(mouse_pos):
            french_colour = (180, 0, 180)
        else: 
            french_colour = PURPLE
        draw_button(screen, french_rect, "French", button_font, french_colour, WHITE)

        if "Hebrew" in languages:
            hebrew_colour = (25, 25, 25)
        elif hebrew_rect.collidepoint(mouse_pos):
            hebrew_colour = (180, 0, 180)
        else: 
            hebrew_colour = PURPLE
        draw_button(screen, hebrew_rect, "Hebrew", button_font, hebrew_colour, WHITE)

        if "Spanish" in languages:
            spanish_colour = (25, 25, 25)
        elif spanish_rect.collidepoint(mouse_pos):
            spanish_colour = (180, 0, 180)
        else: 
            spanish_colour = PURPLE
        draw_button(screen, spanish_rect, "Spanish", button_font, spanish_colour, WHITE)

        if "Tamil" in languages:
            tamil_colour = (25, 25, 25)
        elif tamil_rect.collidepoint(mouse_pos):
            tamil_colour = (180, 0, 180)
        else: 
            tamil_colour = PURPLE
        draw_button(screen, tamil_rect, "Tamil", button_font, tamil_colour, WHITE)

        if "Japanese" in languages:
            japanese_colour = (25, 25, 25)
        elif japanese_rect.collidepoint(mouse_pos):
            japanese_colour = (180, 0, 180)
        else: 
            japanese_colour = PURPLE
        draw_button(screen, japanese_rect, "Japanese", button_font, japanese_colour, WHITE)

        if "Korean" in languages:
            korean_colour = (25, 25, 25)
        elif korean_rect.collidepoint(mouse_pos):
            korean_colour = (180, 0, 180)
        else: 
            korean_colour = PURPLE
        draw_button(screen, korean_rect, "Korean", button_font, korean_colour, WHITE)

        if "German" in languages:
            german_colour = (25, 25, 25)
        elif german_rect.collidepoint(mouse_pos):
            german_colour = (180, 0, 180)
        else: 
            german_colour = PURPLE
        draw_button(screen, german_rect, "German", button_font, german_colour, WHITE)

        if "Swedish" in languages:
            swedish_colour = (25, 25, 25)
        elif swedish_rect.collidepoint(mouse_pos):
            swedish_colour = (180, 0, 180)
        else: 
            swedish_colour = PURPLE
        draw_button(screen, swedish_rect, "Swedish", button_font, swedish_colour, WHITE)

        # [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean, German, Swedish] 

        if max_boulder_speed == 1.0:
            min_colour = (25, 25, 25)
        elif min_speed.collidepoint(mouse_pos):
            min_colour = (180, 0, 180)
        else: 
            min_colour = PURPLE
        draw_button(screen, min_speed, "SLOW", button_font, min_colour, WHITE)

        if max_boulder_speed == 1.5:
            med_colour = (25, 25, 25)
        elif med_speed.collidepoint(mouse_pos):
            med_colour = (180, 0, 180)
        else: 
            med_colour = PURPLE
        draw_button(screen, med_speed, "MEDIUM", button_font, med_colour, WHITE)

        if max_boulder_speed == 2.0:
            max_colour = (25, 25, 25)
        elif max_speed.collidepoint(mouse_pos):
            max_colour = (180, 0, 180)
        else: 
            max_colour = PURPLE
        draw_button(screen, max_speed, "FAST", button_font, max_colour, WHITE)

    # GAME STATE
    elif game_on and not game_over:
        # Question Text
        question_surf = title_font.render(
            f"What is '{english_word}' in {language}?",
            True,
            WHITE
        )
        question_rect = question_surf.get_rect(center=(WIDTH // 2, 50))
        screen.blit(question_surf, question_rect)
        
        # Display the integer "answer_counter"
        counter_surf = title_font.render(
            f"Score: {answer_counter}", 
            True,
            WHITE
        )
        counter_rect = counter_surf.get_rect(center=(WIDTH // 5, HEIGHT - 80))  # near bottom
        screen.blit(counter_surf, counter_rect)
        

        # Answer Boxes (Boulders)
        for i, box in enumerate(answer_boxes[:]):
            box.y += boulder_speeds[i]
            # box.x += boulder_drift[i]

            # boulder rotations?
            # Update rotation
            boulder_angles[i] += boulder_rotation_speeds[i]
            boulder_angles[i] %= 360  # keep angle in 0-359

            # Rotate the image
            rotated_image = pygame.transform.rotate(boulder_image, boulder_angles[i])
            rotated_rect = rotated_image.get_rect(center=box.center)  # keep centered

            # Rotate the image
            rotated_image = pygame.transform.rotate(boulder_image, boulder_angles[i])
            rotated_rect = rotated_image.get_rect(center=box.center)  # keep centered

            screen.blit(rotated_image, rotated_rect.topleft)
            font = get_font_for_language(language)
            if language == "Chinese" and show_pinyin == True:
                # chinese 

                text_surface = font.render(answers[i], True, WHITE)
                text_rect = text_surface.get_rect(center=box.center)
                screen.blit(text_surface, text_rect)
                for key, value in chinese_word_bank.items():
                    if value[0] == answers[i]:
                        pinyin_text = value[1]
                        break
                pinyin_surface = font_pinyin.render(pinyin_text, True, WHITE)
                pinyin_rect = pinyin_surface.get_rect(center=(box.centerx, box.centery + 25))
                screen.blit(pinyin_surface, pinyin_rect)
            else:
                text_surface = font.render(answers[i], True, WHITE)
                text_rect = text_surface.get_rect(center=box.center)
                screen.blit(text_surface, text_rect)

            if box.y > screen.get_height() or box.y + 50 == player_ufo.rect.y:
                game_on = False
                game_over = True


        # Draw UFO
        screen.blit(player_ufo.image, player_ufo.rect)


        for bullet in shots[:]:
            bullet.y -= bullet_speed

            if bullet.y < 0:
                shots.remove(bullet) 

        # Draw the bullet
        for bullet in shots:
            pygame.draw.rect(screen, RED, bullet)


            for i, box in enumerate(answer_boxes):                        
                    if box.collidepoint(bullet.x, bullet.y):
                        # Check if answer is correct
                        
                        if answers[i] == correct_translation:
                            # Correct answer: generate new question
                            answer_counter += 1
                            english_word, language, correct_translation, correct_pinyin = get_random_word()
                            # lang_index = languages.index(language)
                            answers = generate_answers(correct_translation, language)
                            
                            # Clears all bullets
                            shots.clear()
                            for i, box in enumerate(answer_boxes[:]):
                                boulder_speeds = [random.uniform(0.75, max_boulder_speed) for _ in answer_boxes]
                                # boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]
                                boulder_y = random.randint(0, boulder_size)
                                box.y = -boulder_y
                            boulder_angles = [0 for _ in answer_boxes]  # initial rotation for each boulder
                            boulder_rotation_speeds = [random.uniform(-5, 5) for _ in answer_boxes]  # degrees per frame

                        else:
                            # Wrong answer: trigger game over
                            game_on = False
                            game_over = True

                            shots.clear()


    # GAME OVER STATE
    elif game_over:
        
        # Load the music file (WAV)
        end_music = pygame.mixer.Sound(random.choice(sad_song_files))
        end_music.set_volume(0.5)

        if not end_music_playing:
            # Play music (loops infinitely)
            end_music_channel = end_music.play(-1)
            end_music_playing = True

        # Draw game over background image
        screen.blit(ending_image, (0, 0))
        
        # Draw final score text
        final_score_surf = title_font.render(
            f"Final Score: {answer_counter}",
            True,
            BLACK
        )
        final_score_rect = final_score_surf.get_rect(
            bottomright=(WIDTH - 105, HEIGHT - 45)  # padding from edges
        )

        # print the answer 
        # Get correct font for translation
        ans_font = get_font_for_language(language)
        # Render first part (English text)
        text_part1 = f"{english_word} in {language} is   "
        part1_surf = body_font.render(text_part1, True, BLACK)

        # Render translation in language font
        part2_surf = ans_font.render(correct_translation, True, BLACK)

        # Position them side-by-side
        total_width = part1_surf.get_width() + part2_surf.get_width()
        x = 330
        y = 400

        part1_rect = part1_surf.get_rect(topleft=(x, y))
        part2_rect = part2_surf.get_rect(topleft=(part1_rect.right, y))

        # Background box
        bg_padding = 12
        bg_rect = pygame.Rect(
            x - bg_padding,
            y - bg_padding,
            total_width + bg_padding * 2,
            part1_surf.get_height() + bg_padding * 2
        )

        score_bg = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            score_bg,
            (255, 255, 255, 150),
            score_bg.get_rect(),
            border_radius=10
        )

        screen.blit(score_bg, bg_rect.topleft)

        # Draw text
        screen.blit(part1_surf, part1_rect)
        screen.blit(part2_surf, part2_rect)

    

        # Create transparent background for final score
        bg_padding = 12
        bg_rect = final_score_rect.inflate(bg_padding * 2, bg_padding * 2)

        bg_padding = 12
        # bg_rect = answer_rect.inflate(bg_padding * 2, bg_padding * 2)

        score_bg = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            score_bg,
            (255, 255, 255, 150),
            score_bg.get_rect(),
            border_radius=10
        )
        # score_bg.fill((255, 255, 255, 150))  # White with alpha (0–255)

        screen.blit(score_bg, bg_rect.topleft)

        screen.blit(final_score_surf, final_score_rect)

        # screen.blit(answer_surf, answer_rect)
        
        # Draw image-based quit button
        game_over_quit_button.draw()
        play_again_button.draw()

        if play_again_button.check_click(event):

            end_music_channel.stop()
            end_music_playing = False # Stops music

            # RESET GAME
            answer_counter = 0
            shots.clear()

            english_word, language, correct_translation, correct_pinyin = get_random_word()
            # lang_index = languages.index(language)
            answers = generate_answers(correct_translation, language)

            player_ufo.rect.x = 300
            player_ufo.rect.y = 470

            for i, box in enumerate(answer_boxes[:]):
                box.y = -boulder_size
                boulder_speeds = [random.uniform(0.75, max_boulder_speed) for _ in answer_boxes]
                # boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]
            boulder_angles = [0 for _ in answer_boxes]  # initial rotation for each boulder
            boulder_rotation_speeds = [random.uniform(-5, 5) for _ in answer_boxes]  # degrees per frame

            game_over = False
            game_on = True

        elif game_over_quit_button.check_click(event):
            running = False


    # Update Screen
    pygame.display.flip()

# Cleanup
pygame.quit()

sys.exit()
