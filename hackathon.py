import pygame, sys
from pygame.locals import QUIT

WIDTH = 400
HEIGHT = 400

WHITE = (255, 255, 255)
<<<<<<< Updated upstream
=======
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)


languages = ["Chinese", "Hindi", "French"]

answer_counter = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Testing')

clock = pygame.time.Clock()

<<<<<<< Updated upstream
while True:
=======
# Fonts
title_font = pygame.font.SysFont("Times New Roman", 58)
body_font = pygame.font.SysFont("Times New Roman", 25)
button_font = pygame.font.SysFont("Times New Roman", 29)
counter_font = pygame.font.SysFont("Times New Roman", 30)

# Language-specific fonts (ensure font files exist!)
try:
    font_chinese = pygame.font.Font("NotoSansSC-VariableFont_wght.ttf", 25)
    font_hindi = pygame.font.Font("NotoSansDevanagari-VariableFont_wdth.ttf", 25)
except pygame.error as e:
    print(f"Warning: Missing language fonts - {e}")
    font_chinese = font_hindi = pygame.font.SysFont("arial", 25)
font_latin = pygame.font.SysFont("arial", 25)

# UI Layout (MENU BUTTONS - text-based)
rules_box = pygame.Rect(60, 140, 680, 220)
start_button_rect = pygame.Rect(WIDTH // 2 - 140, 400, 120, 50)  # Rename to avoid collision
quit_button_rect = pygame.Rect(WIDTH // 2 + 20, 400, 120, 50)    # Text-based quit button (Rect)

# Background
try:
    background = pygame.image.load("galaxy_background_proper.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error loading background: {e}")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(PURPLE)

# Answer boxes
box_size = 120
box_y = -box_size
answer_boxes = [
    pygame.Rect(100 + i * 160, box_y, box_size, box_size)
    for i in range(4)
]



# Boulder image
try:
    boulder_image = pygame.image.load("space_boulder_proper.png").convert_alpha()
    boulder_image = pygame.transform.scale(boulder_image, (box_size, box_size))
except pygame.error as e:
    print(f"Error loading boulder: {e}")
    boulder_image = pygame.Surface((box_size, box_size))
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
    english_word = random.choice(list(word_bank.keys()))
    lang_index = random.randint(0, 2)
    correct_translation = word_bank[english_word][lang_index]
    language = languages[lang_index]
    return english_word, language, correct_translation

def generate_answers(correct_translation, lang_index):
    answers = [correct_translation]
    while len(answers) < 4:
        random_word = random.choice(list(word_bank.keys()))
        wrong_translation = word_bank[random_word][lang_index]
        if wrong_translation not in answers:
            answers.append(wrong_translation)
    random.shuffle(answers)
    return answers

def get_font_for_language(language):
    if language == "Chinese":
        return font_chinese
    elif language == "Hindi":
        return font_hindi
    else:
        return font_latin

def draw_button(screen, rect, label, font, fill_color, text_color):
    pygame.draw.rect(screen, fill_color, rect, border_radius=8)
    pygame.draw.rect(screen, PURPLE, rect, width=2, border_radius=8)
    text_surf = font.render(label, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)



# Game State Initialization
english_word, language, correct_translation = get_random_word()
lang_index = languages.index(language)
answers = generate_answers(correct_translation, lang_index)

# Create UFO Object
player_ufo = Ufo(300, 470, 200, 170)

shots = [] 
bullet_speed = 10
boulder_speeds = [random.uniform(0.75, 1.75) for _ in answer_boxes]
# boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]
# Game States
running = True
game_on = False
game_over = False  # New state for game over screen

# Main Game Loop
while running:
>>>>>>> Stashed changes
    clock.tick(60)

    # Fill the screen with the background color... this will cover any previous drawings...
    screen.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # Exits the program gracefully without freezing
            sys.exit()


<<<<<<< Updated upstream
    pygame.display.flip()
=======
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
            "1.) Guess the translation of English words",
            "     in French, Hindi, or Mandarin",
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
        start_color = (180, 0, 180) if start_button_rect.collidepoint(mouse_pos) else PURPLE
        draw_button(screen, start_button_rect, "Start", button_font, start_color, WHITE)
        
        # Hover effect for quit button
        quit_color = (180, 0, 180) if quit_button_rect.collidepoint(mouse_pos) else PURPLE
        draw_button(screen, quit_button_rect, "Quit", button_font, quit_color, WHITE)

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

            screen.blit(boulder_image, box.topleft)
            font = get_font_for_language(language)
            text_surface = font.render(answers[i], True, WHITE)
            text_rect = text_surface.get_rect(center=box.center)
            screen.blit(text_surface, text_rect)
            if box.y > screen.get_height():
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
                            english_word, language, correct_translation = get_random_word()
                            lang_index = languages.index(language)
                            answers = generate_answers(correct_translation, lang_index)
                            
                            # Clears all bullets
                            shots.clear()
                            for i, box in enumerate(answer_boxes[:]):
                                boulder_speeds = [random.uniform(0.75, 1.75) for _ in answer_boxes]
                                # boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]
                                box_y = random.randint(0, box_size)
                                box.y = -box_y

                        else:
                            # Wrong answer: trigger game over
                            game_on = False
                            game_over = True

                            shots.clear()


    # GAME OVER STATE
    elif game_over:
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

        # Create transparent background for final score
        bg_padding = 12
        bg_rect = final_score_rect.inflate(bg_padding * 2, bg_padding * 2)

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
        
        # Draw image-based quit button
        game_over_quit_button.draw()
        play_again_button.draw()
        if play_again_button.check_click(event):
            # RESET GAME
            answer_counter = 0
            shots.clear()

            english_word, language, correct_translation = get_random_word()
            lang_index = languages.index(language)
            answers = generate_answers(correct_translation, lang_index)

            player_ufo.rect.x = 300
            player_ufo.rect.y = 470

            for i, box in enumerate(answer_boxes[:]):
                box.y = -box_size
                boulder_speeds = [random.uniform(0.75, 1.75) for _ in answer_boxes]
                # boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]

            game_over = False
            game_on = True

        elif game_over_quit_button.check_click(event):
            running = False


    # Update Screen
    pygame.display.flip()

# Cleanup
pygame.quit()
sys.exit()
>>>>>>> Stashed changes
