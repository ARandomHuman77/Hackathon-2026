import pygame, sys, os
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import random

os.chdir(os.path.dirname(__file__))

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)


# [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean]
word_bank = {
    "Hello": ["你好", "नमस्ते", "Bonjour", "שלום", "Hola", "வணக்கம்", "こんにちは", "안녕하세요", "Hallo", "Hej"],
    "Goodbye": ["再见", "अलविदा", "Au revoir", "להתראות", "Adiós", "பிரியாவிடை", "さようなら", "안녕히 가세요", "Auf Wiedersehen", "Adjö"],
    "Please": ["请", "कृपया", "S'il vous plaît", "בבקשה", "Por favor", "தயவு செய்து", "お願いします", "제발", "Bitte", "Snälla"],
    "Thank you": ["谢谢", "धन्यवाद", "Merci", "תודה", "Gracias", "நன்றி", "ありがとう", "감사합니다", "Danke", "Tack"],
    "Yes": ["是", "हाँ", "Oui", "כן", "Sí", "ஆம்", "はい", "네", "Ja", "Ja"],
    "No": ["不", "नहीं", "Non", "לא", "No", "இல்லை", "いいえ", "아니요", "Nein", "Nej"],
    "Excuse me": ["打扰一下", "माफ़ कीजिए", "Excusez-moi", "סליחה", "Perdón", "மன்னிக்கவும்", "すみません", "실례합니다", "Entschuldigung", "Ursäkta"],
    "Sorry": ["对不起", "माफ़ करना", "Désolé", "מצטער", "Lo siento", "மன்னிக்கவும்", "ごめんなさい", "죄송합니다", "Entschuldigung", "Förlåt"],

    "Friend": ["朋友", "दोस्त", "Ami", "חבר", "Amigo", "நண்பர்", "友達", "친구", "Freund", "Vän"],
    "Family": ["家庭", "परिवार", "Famille", "משפחה", "Familia", "குடும்பம்", "家族", "가족", "Familie", "Familj"],
    "Love": ["爱", "प्यार", "Amour", "אהבה", "Amor", "அன்பு", "愛", "사랑", "Liebe", "Kärlek"],
    "Food": ["食物", "भोजन", "Nourriture", "אוכל", "Comida", "உணவு", "食べ物", "음식", "Essen", "Mat"],
    "Water": ["水", "पानी", "Eau", "מים", "Agua", "தண்ணீர்", "水", "물", "Wasser", "Vatten"],
    "House": ["房子", "घर", "Maison", "בית", "Casa", "வீடு", "家", "집", "Haus", "Hus"],
    "School": ["学校", "स्कूल", "École", "בית ספר", "Escuela", "பள்ளி", "学校", "학교", "Schule", "Skola"],
    "Work": ["工作", "काम", "Travail", "עבודה", "Trabajo", "வேலை", "仕事", "일", "Arbeit", "Arbete"],
    "Money": ["钱", "पैसा", "Argent", "כסף", "Dinero", "பணம்", "お金", "돈", "Geld", "Pengar"],
    "Time": ["时间", "समय", "Temps", "זמן", "Tiempo", "நேரம்", "時間", "시간", "Zeit", "Tid"],

    "Day": ["天", "दिन", "Jour", "יום", "Día", "நாள்", "日", "날", "Tag", "Dag"],
    "Night": ["夜", "रात", "Nuit", "לילה", "Noche", "இரவு", "夜", "밤", "Nacht", "Natt"],
    "Sun": ["太阳", "सूरज", "Soleil", "שמש", "Sol", "சூரியன்", "太陽", "태양", "Sonne", "Sol"],
    "Moon": ["月亮", "चाँद", "Lune", "ירח", "Luna", "நிலா", "月", "달", "Mond", "Måne"],
    "Star": ["星星", "तारा", "Étoile", "כוכב", "Estrella", "நட்சத்திரம்", "星", "별", "Stern", "Stjärna"],
    "Dog": ["狗", "कुत्ता", "Chien", "כלב", "Perro", "நாய்", "犬", "개", "Hund", "Hund"],
    "Cat": ["猫", "बिल्ली", "Chat", "חתול", "Gato", "பூனை", "猫", "고양이", "Katze", "Katt"],
    "Car": ["车", "गाड़ी", "Voiture", "מכונית", "Coche", "கார்", "車", "자동차", "Auto", "Bil"],
    "Book": ["书", "किताब", "Livre", "ספר", "Libro", "புத்தகம்", "本", "책", "Buch", "Bok"],
    "Pen": ["笔", "कलम", "Stylo", "עט", "Bolígrafo", "பேனா", "ペン", "펜", "Stift", "Penna"],

    "Chair": ["椅子", "कुर्सी", "Chaise", "כיסא", "Silla", "நாற்காலி", "椅子", "의자", "Stuhl", "Stol"],
    "Table": ["桌子", "मेज़", "Table", "שולחן", "Mesa", "மேசை", "テーブル", "탁자", "Tisch", "Bord"],
    "Window": ["窗户", "खिड़की", "Fenêtre", "חלון", "Ventana", "ஜன்னல்", "窓", "창문", "Fenster", "Fönster"],
    "Door": ["门", "दरवाज़ा", "Porte", "דלת", "Puerta", "கதவு", "ドア", "문", "Tür", "Dörr"],
    "City": ["城市", "शहर", "Ville", "עיר", "Ciudad", "நகரம்", "都市", "도시", "Stadt", "Stad"],
    "Country": ["国家", "देश", "Pays", "מדינה", "País", "நாடு", "国", "나라", "Land", "Land"],
    "Language": ["语言", "भाषा", "Langue", "שפה", "Idioma", "மொழி", "言語", "언어", "Sprache", "Språk"],
    "Computer": ["电脑", "कंप्यूटर", "Ordinateur", "מחשב", "Computadora", "கணினி", "コンピューター", "컴퓨터", "Computer", "Dator"],
    "Phone": ["电话", "फ़ोन", "Téléphone", "טלפון", "Teléfono", "தொலைபேசி", "電話", "전화", "Telefon", "Telefon"],

    "Music": ["音乐", "संगीत", "Musique", "מוזיקה", "Música", "இசை", "音楽", "음악", "Musik", "Musik"],
    "Movie": ["电影", "फ़िल्म", "Film", "סרט", "Película", "திரைப்படம்", "映画", "영화", "Film", "Film"],
    "Game": ["游戏", "खेल", "Jeu", "משחק", "Juego", "விளையாட்டு", "ゲーム", "게임", "Spiel", "Spel"],
    "Happy": ["快乐", "खुश", "Heureux", "שמח", "Feliz", "மகிழ்ச்சி", "幸せ", "행복한", "Glücklich", "Glad"],
    "Sad": ["难过", "उदास", "Triste", "עצוב", "Triste", "சோகம்", "悲しい", "슬픈", "Traurig", "Ledsen"],
    "Big": ["大", "बड़ा", "Grand", "גדול", "Grande", "பெரியது", "大きい", "큰", "Groß", "Stor"],
    "Small": ["小", "छोटा", "Petit", "קטן", "Pequeño", "சிறியது", "小さい", "작은", "Klein", "Liten"],
    "Hot": ["热", "गर्म", "Chaud", "חם", "Caliente", "சூடு", "暑い", "더운", "Heiß", "Varm"],
    "Cold": ["冷", "ठंडा", "Froid", "קר", "Frío", "குளிர்", "寒い", "추운", "Kalt", "Kall"],
    "Fast": ["快", "तेज़", "Rapide", "מהיר", "Rápido", "வேகமான", "速い", "빠른", "Schnell", "Snabb"],

    "Teacher": ["老师", "शिक्षक", "Professeur", "מורה", "Profesor", "ஆசிரியர்", "先生", "선생님", "Lehrer", "Lärare"],
    "Student": ["学生", "छात्र", "Étudiant", "תלמיד", "Estudiante", "மாணவர்", "学生", "학생", "Student", "Student"],
    "Doctor": ["医生", "डॉक्टर", "Médecin", "רופא", "Médico", "மருத்துவர்", "医者", "의사", "Arzt", "Läkare"],
    "Nurse": ["护士", "नर्स", "Infirmier", "אחות", "Enfermero", "செவிலியர்", "看護師", "간호사", "Krankenschwester", "Sjuksköterska"],
    "Engineer": ["工程师", "इंजीनियर", "Ingénieur", "מהנדס", "Ingeniero", "பொறியாளர்", "エンジニア", "엔지니어", "Ingenieur", "Ingenjör"],
    "Artist": ["艺术家", "कलाकार", "Artiste", "אמן", "Artista", "கலைஞர்", "芸術家", "예술가", "Künstler", "Konstnär"],
    "Driver": ["司机", "चालक", "Conducteur", "נהג", "Conductor", "ஓட்டுநர்", "運転手", "운전사", "Fahrer", "Förare"],
    "Farmer": ["农民", "किसान", "Agriculteur", "חקלאי", "Agricultor", "விவசாயி", "農家", "농부", "Landwirt", "Bonde"],
    "Police": ["警察", "पुलिस", "Police", "משטרה", "Policía", "காவலர்", "警察", "경찰", "Polizei", "Polis"],
    "Fire": ["火", "आग", "Feu", "אש", "Fuego", "நெருப்பு", "火", "불", "Feuer", "Eld"],

    "Air": ["空气", "हवा", "Air", "אוויר", "Aire", "காற்று", "空気", "공기", "Luft", "Luft"],
    "Earth": ["地球", "पृथ्वी", "Terre", "אדמה", "Tierra", "பூமி", "地球", "지구", "Erde", "Jord"],
    "Rain": ["雨", "बारिश", "Pluie", "גשם", "Lluvia", "மழை", "雨", "비", "Regen", "Regn"],
    "Snow": ["雪", "बर्फ", "Neige", "שלג", "Nieve", "பனி", "雪", "눈", "Schnee", "Snö"],
    "Wind": ["风", "हवा", "Vent", "רוח", "Viento", "காற்று", "風", "바람", "Wind", "Vind"],
    "Mountain": ["山", "पहाड़", "Montagne", "הר", "Montaña", "மலை", "山", "산", "Berg", "Berg"],
    "River": ["河", "नदी", "Rivière", "נהר", "Río", "ஆறு", "川", "강", "Fluss", "Flod"],
    "Ocean": ["海洋", "महासागर", "Océan", "אוקיינוס", "Océano", "கடல்", "海洋", "바다", "Ozean", "Hav"],
    "Forest": ["森林", "जंगल", "Forêt", "יער", "Bosque", "காடு", "森", "숲", "Wald", "Skog"],
    "Island": ["岛", "द्वीप", "Île", "אי", "Isla", "தீவு", "島", "섬", "Insel", "Ö"],

    "Breakfast": ["早餐", "नाश्ता", "Petit-déjeuner", "ארוחת בוקר", "Desayuno", "காலை உணவு", "朝食", "아침식사", "Frühstück", "Frukost"],
    "Lunch": ["午餐", "दोपहर का भोजन", "Déjeuner", "ארוחת צהריים", "Almuerzo", "மதிய உணவு", "昼食", "점심식사", "Mittagessen", "Lunch"],
    "Dinner": ["晚餐", "रात का खाना", "Dîner", "ארוחת ערב", "Cena", "இரவு உணவு", "夕食", "저녁식사", "Abendessen", "Middag"],
    "Coffee": ["咖啡", "कॉफ़ी", "Café", "קפה", "Café", "காபி", "コーヒー", "커피", "Kaffee", "Kaffe"],
    "Tea": ["茶", "चाय", "Thé", "תה", "Té", "தேநீர்", "お茶", "차", "Tee", "Te"],
    "Sugar": ["糖", "चीनी", "Sucre", "סוכר", "Azúcar", "சர்க்கரை", "砂糖", "설탕", "Zucker", "Socker"],
    "Salt": ["盐", "नमक", "Sel", "מלח", "Sal", "உப்பு", "塩", "소금", "Salz", "Salt"],
    "Bread": ["面包", "रोटी", "Pain", "לחם", "Pan", "ரொட்டி", "パン", "빵", "Brot", "Bröd"],
    "Rice": ["米饭", "चावल", "Riz", "אורז", "Arroz", "அரிசி", "ご飯", "쌀", "Reis", "Ris"],
    "Fruit": ["水果", "फल", "Fruit", "פרי", "Fruta", "பழம்", "果物", "과일", "Obst", "Frukt"],

    "Vegetable": ["蔬菜", "सब्ज़ी", "Légume", "ירק", "Verdura", "காய்கறி", "野菜", "채소", "Gemüse", "Grönsak"],
    "Hospital": ["医院", "अस्पताल", "Hôpital", "בית חולים", "Hospital", "மருத்துவமனை", "病院", "병원", "Krankenhaus", "Sjukhus"],
    "Airport": ["机场", "हवाई अड्डा", "Aéroport", "שדה תעופה", "Aeropuerto", "விமான நிலையம்", "空港", "공항", "Flughafen", "Flygplats"],
    "Train": ["火车", "रेल गाड़ी", "Train", "רכבת", "Tren", "ரயில்", "電車", "기차", "Zug", "Tåg"],
    "Bus": ["公交车", "बस", "Bus", "אוטובוס", "Autobús", "பேருந்து", "バス", "버스", "Bus", "Buss"],
    "Ticket": ["票", "टिकट", "Billet", "כרטיס", "Boleto", "டிக்கெட்", "切符", "표", "Ticket", "Biljett"],
    "Market": ["市场", "बाज़ार", "Marché", "שוק", "Mercado", "சந்தை", "市場", "시장", "Markt", "Marknad"],
    "Store": ["商店", "दुकान", "Magasin", "חנות", "Tienda", "கடை", "店", "가게", "Geschäft", "Butik"],
    "Restaurant": ["餐厅", "रेस्तरां", "Restaurant", "מסעדה", "Restaurante", "உணவகம்", "レストラン", "식당", "Restaurant", "Restaurang"],
    "Hotel": ["酒店", "होटल", "Hôtel", "מלון", "Hotel", "ஹோட்டல்", "ホテル", "호텔", "Hotel", "Hotell"],

    "What": ["什么", "क्या", "Quoi", "מה", "Qué", "என்ன", "何", "무엇", "Was", "Vad"],
    "Who": ["谁", "कौन", "Qui", "מי", "Quién", "யார்", "誰", "누구", "Wer", "Vem"],
    "Where": ["哪里", "कहाँ", "Où", "איפה", "Dónde", "எங்கே", "どこ", "어디", "Wo", "Var"],
    "When": ["什么时候", "कब", "Quand", "מתי", "Cuándo", "எப்போது", "いつ", "언제", "Wann", "När"],
    "Why": ["为什么", "क्यों", "Pourquoi", "למה", "Por qué", "ஏன்", "なぜ", "왜", "Warum", "Varför"],
    "How": ["怎么", "कैसे", "Comment", "איך", "Cómo", "எப்படி", "どう", "어떻게", "Wie", "Hur"],
    "Which": ["哪个", "कौन सा", "Lequel", "איזה", "Cuál", "எது", "どれ", "어느", "Welcher", "Vilken"],
    "How much": ["多少", "कितना", "Combien", "כמה", "Cuánto", "எவ்வளவு", "いくら", "얼마", "Wie viel", "Hur mycket"],
    "How many": ["多少", "कितने", "Combien", "כמה", "Cuántos", "எத்தனை", "いくつ", "몇", "Wie viele", "Hur många"],
    "Name": ["名字", "नाम", "Nom", "שם", "Nombre", "பெயர்", "名前", "이름", "Name", "Namn"],

    "Address": ["地址", "पता", "Adresse", "כתובת", "Dirección", "முகவரி", "住所", "주소", "Adresse", "Adress"],
    "Age": ["年龄", "उम्र", "Âge", "גיל", "Edad", "வயது", "年齢", "나이", "Alter", "Ålder"],
    "Birthday": ["生日", "जन्मदिन", "Anniversaire", "יום הולדת", "Cumpleaños", "பிறந்தநாள்", "誕生日", "생일", "Geburtstag", "Födelsedag"],
    "Number": ["号码", "नंबर", "Numéro", "מספר", "Número", "எண்", "番号", "번호", "Nummer", "Nummer"],
    "Today": ["今天", "आज", "Aujourd'hui", "היום", "Hoy", "இன்று", "今日", "오늘", "Heute", "Idag"],
    "Tomorrow": ["明天", "कल", "Demain", "מחר", "Mañana", "நாளை", "明日", "내일", "Morgen", "Imorgon"],
    "Yesterday": ["昨天", "कल", "Hier", "אתמול", "Ayer", "நேற்று", "昨日", "어제", "Gestern", "Igår"],
    "Now": ["现在", "अभी", "Maintenant", "עכשיו", "Ahora", "இப்போது", "今", "지금", "Jetzt", "Nu"],
    "Later": ["以后", "बाद में", "Plus tard", "אחר כך", "Más tarde", "பிறகு", "後で", "나중에", "Später", "Senare"],
    "Early": ["早", "जल्दी", "Tôt", "מוקדם", "Temprano", "அதிகாலை", "早い", "이른", "Früh", "Tidigt"],

    "Late": ["晚", "देर", "Tard", "מאוחר", "Tarde", "தாமதம்", "遅い", "늦은", "Spät", "Sent"],
    "Open": ["打开", "खोलना", "Ouvrir", "לפתוח", "Abrir", "திறக்க", "開ける", "열다", "Öffnen", "Öppna"],
    "Close": ["关闭", "बंद करना", "Fermer", "לסגור", "Cerrar", "மூட", "閉める", "닫다", "Schließen", "Stänga"],
    "Start": ["开始", "शुरू करना", "Commencer", "להתחיל", "Empezar", "தொடங்க", "始める", "시작하다", "Starten", "Starta"],
    "Finish": ["结束", "खत्म करना", "Finir", "לסיים", "Terminar", "முடிக்க", "終わる", "끝내다", "Beenden", "Avsluta"],
    "Help": ["帮助", "मदद", "Aide", "עזרה", "Ayuda", "உதவி", "助け", "도움", "Hilfe", "Hjälp"],
    "Call": ["打电话", "फोन करना", "Appeler", "להתקשר", "Llamar", "அழைக்க", "電話する", "전화하다", "Anrufen", "Ringa"],
    "Wait": ["等", "इंतज़ार करना", "Attendre", "לחכות", "Esperar", "காத்திருக்க", "待つ", "기다리다", "Warten", "Vänta"],
    "Understand": ["理解", "समझना", "Comprendre", "להבין", "Entender", "புரிந்துகொள்ள", "理解する", "이해하다", "Verstehen", "Förstå"],
    "Repeat": ["重复", "दोहराना", "Répéter", "לחזור", "Repetir", "மீண்டும் சொல்ல", "繰り返す", "반복하다", "Wiederholen", "Upprepa"],

    "Speak": ["说", "बोलना", "Parler", "לדבר", "Hablar", "பேச", "話す", "말하다", "Sprechen", "Tala"],
    "Listen": ["听", "सुनना", "Écouter", "להקשיב", "Escuchar", "கேட்க", "聞く", "듣다", "Hören", "Lyssna"],
    "Read": ["读", "पढ़ना", "Lire", "לקרוא", "Leer", "படிக்க", "読む", "읽다", "Lesen", "Läsa"],
    "Write": ["写", "लिखना", "Écrire", "לכתוב", "Escribir", "எழுத", "書く", "쓰다", "Schreiben", "Skriva"],
    "Buy": ["买", "खरीदना", "Acheter", "לקנות", "Comprar", "வாங்க", "買う", "사다", "Kaufen", "Köpa"],
    "Sell": ["卖", "बेचना", "Vendre", "למכור", "Vender", "விற்க", "売る", "팔다", "Verkaufen", "Sälja"],
    "Pay": ["支付", "भुगतान करना", "Payer", "לשלם", "Pagar", "செலுத்த", "払う", "지불하다", "Bezahlen", "Betala"],
    "Cost": ["花费", "कीमत", "Coût", "עלות", "Costo", "செலவு", "費用", "비용", "Kosten", "Kosta"],
    "Need": ["需要", "ज़रूरत", "Besoin", "צורך", "Necesitar", "தேவை", "必要", "필요", "Brauchen", "Behöva"],
    "Want": ["想要", "चाहना", "Vouloir", "רוצה", "Querer", "விரும்ப", "欲しい", "원하다", "Wollen", "Vilja"],

    "Like": ["喜欢", "पसंद करना", "Aimer", "לאהוב", "Gustar", "பிடிக்கும்", "好き", "좋아하다", "Mögen", "Gilla"],
    "Dislike": ["不喜欢", "नापसंद करना", "Détester", "לא אוהב", "No gustar", "பிடிக்காது", "嫌い", "싫어하다", "Nicht mögen", "Ogilla"],
    "Different": ["不同", "अलग", "Différent", "שונה", "Diferente", "வேறுபட்ட", "違う", "다른", "Verschieden", "Annorlunda"],
    "Same": ["相同", "समान", "Même", "אותו", "Mismo", "அதே", "同じ", "같은", "Gleich", "Samma"],
    "Easy": ["容易", "आसान", "Facile", "קל", "Fácil", "எளிது", "簡単", "쉬운", "Einfach", "Enkel"],
    "Difficult": ["困难", "मुश्किल", "Difficile", "קשה", "Difícil", "கடினம்", "難しい", "어려운", "Schwierig", "Svår"],
    "Right": ["正确", "सही", "Correct", "נכון", "Correcto", "சரி", "正しい", "맞다", "Richtig", "Rätt"],
    "Wrong": ["错误", "गलत", "Faux", "לא נכון", "Incorrecto", "தவறு", "間違い", "틀리다", "Falsch", "Fel"],
    "Here": ["这里", "यहाँ", "Ici", "כאן", "Aquí", "இங்கே", "ここ", "여기", "Hier", "Här"],
    "There": ["那里", "वहाँ", "Là-bas", "שם", "Allí", "அங்கே", "そこ", "거기", "Dort", "Där"],

    "Because": ["因为", "क्योंकि", "Parce que", "כי", "Porque", "ஏனெனில்", "なぜなら", "왜냐하면", "Weil", "Eftersom"],
    "But": ["但是", "लेकिन", "Mais", "אבל", "Pero", "ஆனால்", "でも", "하지만", "Aber", "Men"],
    "And": ["和", "और", "Et", "ו", "Y", "மற்றும்", "そして", "그리고", "Und", "Och"],
    "Or": ["或者", "या", "Ou", "או", "O", "அல்லது", "または", "또는", "Oder", "Eller"],
    "If": ["如果", "अगर", "Si", "אם", "Si", "என்றால்", "もし", "만약", "Wenn", "Om"],
    "Maybe": ["也许", "शायद", "Peut-être", "אולי", "Quizás", "ஒருவேளை", "たぶん", "아마도", "Vielleicht", "Kanske"],
    "Always": ["总是", "हमेशा", "Toujours", "תמיד", "Siempre", "எப்போதும்", "いつも", "항상", "Immer", "Alltid"],
    "Never": ["从不", "कभी नहीं", "Jamais", "לעולם לא", "Nunca", "ஒருபோதும் இல்லை", "決して", "절대", "Niemals", "Aldrig"],
    "Sometimes": ["有时", "कभी-कभी", "Parfois", "לפעמים", "A veces", "சில நேரங்களில்", "時々", "가끔", "Manchmal", "Ibland"],
    "Usually": ["通常", "आमतौर पर", "Habituellement", "בדרך כלל", "Normalmente", "பொதுவாக", "普通", "보통", "Normalerweise", "Vanligtvis"],

    "Before": ["之前", "पहले", "Avant", "לפני", "Antes", "முன்", "前に", "전에", "Vor", "Före"],
    "After": ["之后", "बाद में", "Après", "אחרי", "Después", "பிறகு", "後で", "후에", "Nach", "Efter"],
    "Inside": ["里面", "अंदर", "À l'intérieur", "בפנים", "Dentro", "உள்ளே", "中", "안에", "Innen", "Inuti"],
    "Outside": ["外面", "बाहर", "À l'extérieur", "בחוץ", "Afuera", "வெளியே", "外", "밖에", "Außen", "Utanför"],
    "Near": ["附近", "पास", "Près", "קרוב", "Cerca", "அருகில்", "近く", "가까이", "Nah", "Nära"],
    "Far": ["远", "दूर", "Loin", "רחוק", "Lejos", "தொலைவில்", "遠い", "멀리", "Weit", "Långt"],
    "Left": ["左", "बायाँ", "Gauche", "שמאל", "Izquierda", "இடது", "左", "왼쪽", "Links", "Vänster"],
    "Right (direction)": ["右", "दायाँ", "Droite", "ימין", "Derecha", "வலது", "右", "오른쪽", "Rechts", "Höger"],
    "Straight": ["直走", "सीधा", "Tout droit", "ישר", "Recto", "நேராக", "まっすぐ", "직진", "Geradeaus", "Rakt fram"],
    "Around": ["周围", "आसपास", "Autour", "מסביב", "Alrededor", "சுற்றிலும்", "周り", "주변", "Herum", "Runt"],

    "Everything": ["一切", "सब कुछ", "Tout", "הכול", "Todo", "எல்லாம்", "すべて", "모든 것", "Alles", "Allt"],
    "Nothing": ["什么都没有", "कुछ नहीं", "Rien", "כלום", "Nada", "எதுவும் இல்லை", "何もない", "아무것도", "Nichts", "Ingenting"],
    "Something": ["某事", "कुछ", "Quelque chose", "משהו", "Algo", "ஏதாவது", "何か", "무언가", "Etwas", "Något"],
    "Someone": ["某人", "कोई", "Quelqu'un", "מישהו", "Alguien", "யாராவது", "誰か", "누군가", "Jemand", "Någon"],
    "Everyone": ["每个人", "सब लोग", "Tout le monde", "כולם", "Todos", "அனைவரும்", "みんな", "모두", "Jeder", "Alla"],
    "All": ["所有", "सब", "Tous", "כל", "Todo", "அனைத்து", "全部", "모든", "Alle", "Alla"],
    "More": ["更多", "अधिक", "Plus", "יותר", "Más", "மேலும்", "もっと", "더", "Mehr", "Mer"],
    "Less": ["更少", "कम", "Moins", "פחות", "Menos", "குறைவு", "より少ない", "덜", "Weniger", "Mindre"],
    "Most": ["大多数", "अधिकांश", "La plupart", "רוב", "La mayoría", "பெரும்பாலான", "ほとんど", "대부분", "Die meisten", "De flesta"],
    "Few": ["很少", "कुछ", "Peu", "מעט", "Pocos", "சில", "少し", "몇", "Wenige", "Få"],

    "First": ["第一", "पहला", "Premier", "ראשון", "Primero", "முதல்", "最初", "첫째", "Erste", "Första"],
    "Second": ["第二", "दूसरा", "Deuxième", "שני", "Segundo", "இரண்டாம்", "二番目", "둘째", "Zweite", "Andra"],
    "Last": ["最后", "आखिरी", "Dernier", "אחרון", "Último", "கடைசி", "最後", "마지막", "Letzte", "Sista"],
    "Next": ["下一个", "अगला", "Suivant", "הבא", "Siguiente", "அடுத்த", "次", "다음", "Nächste", "Nästa"],
    "Important": ["重要", "महत्वपूर्ण", "Important", "חשוב", "Importante", "முக்கியம்", "重要", "중요한", "Wichtig", "Viktig"],
    "Possible": ["可能", "संभव", "Possible", "אפשרי", "Posible", "சாத்தியம்", "可能", "가능한", "Möglich", "Möjlig"],
    "Sure": ["确定", "पक्का", "Sûr", "בטוח", "Seguro", "நிச்சயம்", "確か", "확실한", "Sicher", "Säker"],
    "Ready": ["准备好", "तैयार", "Prêt", "מוכן", "Listo", "தயார்", "準備ができた", "준비된", "Bereit", "Redo"],
    "Busy": ["忙", "व्यस्त", "Occupé", "עסוק", "Ocupado", "பிஸி", "忙しい", "바쁜", "Beschäftigt", "Upptagen"],
    "Free (available)": ["有空", "खाली", "Libre", "פנוי", "Libre", "வெற்று", "暇", "한가한", "Frei", "Ledig"],

    "Problem": ["问题", "समस्या", "Problème", "בעיה", "Problema", "பிரச்சனை", "問題", "문제", "Problem", "Problem"],
    "Idea": ["主意", "विचार", "Idée", "רעיון", "Idea", "யோசனை", "アイデア", "아이디어", "Idee", "Idé"],
    "Reason": ["原因", "कारण", "Raison", "סיבה", "Razón", "காரணம்", "理由", "이유", "Grund", "Anledning"],
    "Example": ["例子", "उदाहरण", "Exemple", "דוגמה", "Ejemplo", "உதாரணம்", "例", "예", "Beispiel", "Exempel"],
    "Truth": ["真相", "सच", "Vérité", "אמת", "Verdad", "உண்மை", "真実", "진실", "Wahrheit", "Sanning"],
    "Lie": ["谎言", "झूठ", "Mensonge", "שקר", "Mentira", "பொய்", "嘘", "거짓말", "Lüge", "Lögn"],
    "Message": ["消息", "संदेश", "Message", "הודעה", "Mensaje", "செய்தி", "メッセージ", "메시지", "Nachricht", "Meddelande"],
    "Information": ["信息", "जानकारी", "Information", "מידע", "Información", "தகவல்", "情報", "정보", "Information", "Information"],
    "Plan": ["计划", "योजना", "Plan", "תוכנית", "Plan", "திட்டம்", "計画", "계획", "Plan", "Plan"],
    "Goal": ["目标", "लक्ष्य", "Objectif", "מטרה", "Meta", "இலக்கு", "目標", "목표", "Ziel", "Mål"],

    "Cool": ["酷", "कूल", "Cool", "מגניב", "Guay", "சூப்பர்", "かっこいい", "멋있어", "Cool", "Cool"],
    "Awesome": ["太棒了", "कमाल", "Génial", "מעולה", "Genial", "அருமை", "最高", "대박", "Großartig", "Grymt"],
    "Wow": ["哇", "वाह", "Wouah", "וואו", "Guau", "ஆஹா", "わあ", "와", "Wow", "Wow"],
    "No way!": ["不会吧", "अरे नहीं", "Pas possible", "אין מצב", "¡No puede ser!", "அப்படி இல்லை", "まさか", "설마", "Auf keinen Fall!", "Ingen chans!"],
    "Seriously?": ["真的？", "सच में?", "Sérieux ?", "באמת?", "¿En serio?", "உண்மையா?", "マジで？", "진짜?", "Ernsthaft?", "Seriöst?"],
    "My bad": ["我的错", "मेरी गलती", "Ma faute", "טעות שלי", "Fue mi culpa", "என் தவறு", "俺のミス", "내 실수야", "Mein Fehler", "Mitt fel"],
    "Whatever": ["随便", "जो भी", "Comme tu veux", "מה שתגיד", "Lo que sea", "எதுவும் சரி", "どうでもいい", "마음대로", "Egal", "Spelar ingen roll"],
    "Deal": ["成交", "पक्का", "Marché conclu", "סגור", "Trato hecho", "ஒப்பந்தம்", "決まり", "콜", "Abgemacht", "Deal"],

    "Mess": ["乱七八糟", "गड़बड़", "Bazaar", "בלגן", "Desastre", "குழப்பம்", "めちゃくちゃ", "엉망", "Chaos", "Röra"],
    "Creepy": ["吓人", "डरावना", "Flippant", "מפחיד", "Raro", "பயங்கரம்", "気持ち悪い", "소름 끼치는", "Unheimlich", "Läskig"],
    "Weird": ["奇怪", "अजीब", "Bizarre", "מוזר", "Raro", "விசித்திரம்", "変", "이상해", "Seltsam", "Konstig"],
    "Lame": ["无聊", "बेकार", "Nul", "דפוק", "Aburrido", "சலிப்பு", "ダサい", "별로야", "Lahm", "Lam"],
    "Shy": ["害羞", "शर्मीला", "Timide", "ביישן", "Tímido", "வெட்கம்", "恥ずかしい", "수줍은", "Schüchtern", "Blyg"],
    "Lazy": ["懒", "आलसी", "Paresseux", "עצלן", "Perezoso", "சோம்பேறி", "怠け者", "게으른", "Faul", "Lat"],
    "Boring": ["无聊", "उबाऊ", "Ennuyeux", "משעמם", "Aburrido", "சலிப்பான", "つまらない", "지루한", "Langweilig", "Tråkig"],
    "Annoying": ["烦人", "परेशान करने वाला", "Énervant", "מעצבן", "Molesto", "எரிச்சலான", "うざい", "짜증나는", "Nervig", "Irriterande"],
    "Gross": ["恶心", "गंदा", "Dégoûtant", "מגעיל", "Asqueroso", "அருவருப்பு", "気持ち悪い", "역겨워", "Eklig", "Äcklig"],

    "Epic": ["史诗级", "महाकाव्य जैसा", "Épique", "אפי", "Épico", "மிக பெரிய", "壮大", "레전드", "Episch", "Episkt"],
    "Fake": ["假", "नकली", "Faux", "מזויף", "Falso", "போலி", "偽物", "가짜", "Falsch", "Falsk"],
    "Real": ["真的", "असली", "Vrai", "אמיתי", "Real", "உண்மையான", "本物", "진짜", "Echt", "Äkta"],
    "Bro": ["兄弟", "भाई", "Mec", "אחי", "Bro", "டா", "兄弟", "형", "Bruder", "Brorsan"],
    "Dude": ["哥们", "यार", "Mec", "אחי", "Tío", "டூட்", "おい", "야", "Alter", "Snubbe"],
    "Shut up": ["闭嘴", "चुप रहो", "Tais-toi", "שתוק", "Cállate", "அமைதி", "黙れ", "닥쳐", "Halt den Mund", "Håll käften"],

    "Go": ["去", "जाना", "Aller", "ללכת", "Ir", "போக", "行く", "가다", "Gehen", "Gå"],
    "Come": ["来", "आना", "Venir", "לבוא", "Venir", "வர", "来る", "오다", "Kommen", "Komma"],
    "Take": ["拿", "लेना", "Prendre", "לקחת", "Tomar", "எடுக்க", "取る", "가져가다", "Nehmen", "Ta"],
    "Bring": ["带来", "लाना", "Apporter", "להביא", "Traer", "கொண்டு வர", "持ってくる", "가져오다", "Bringen", "Ta med"],
    "Give": ["给", "देना", "Donner", "לתת", "Dar", "கொடுக்க", "あげる", "주다", "Geben", "Ge"],
    "Find": ["找到", "ढूँढना", "Trouver", "למצוא", "Encontrar", "கண்டுபிடிக்க", "見つける", "찾다", "Finden", "Hitta"],
    "Look": ["看", "देखना", "Regarder", "להסתכל", "Mirar", "பார்க்க", "見る", "보다", "Schauen", "Titta"],
    "Watch": ["观看", "देखना", "Observer", "לצפות", "Ver", "கவனிக்க", "観る", "지켜보다", "Ansehen", "Titta på"],
    "Use": ["使用", "उपयोग करना", "Utiliser", "להשתמש", "Usar", "பயன்படுத்த", "使う", "사용하다", "Benutzen", "Använda"],
    "Try": ["尝试", "कोशिश करना", "Essayer", "לנסות", "Intentar", "முயற்சிக்க", "試す", "시도하다", "Versuchen", "Försöka"],

    "Ask": ["问", "पूछना", "Demander", "לשאול", "Preguntar", "கேட்க", "聞く", "묻다", "Fragen", "Fråga"],
    "Answer (verb)": ["回答", "उत्तर देना", "Répondre", "לענות", "Responder", "பதில் அளிக்க", "答える", "대답하다", "Antworten", "Svara"],
    "Feel": ["感觉", "महसूस करना", "Sentir", "להרגיש", "Sentir", "உணர", "感じる", "느끼다", "Fühlen", "Känna"],
    "Think": ["认为", "सोचना", "Penser", "לחשוב", "Pensar", "சிந்திக்க", "考える", "생각하다", "Denken", "Tänka"],
    "Believe": ["相信", "विश्वास करना", "Croire", "להאמין", "Creer", "நம்ப", "信じる", "믿다", "Glauben", "Tro"],
    "Remember": ["记得", "याद रखना", "Se souvenir", "לזכור", "Recordar", "நினைவில் கொள்", "覚える", "기억하다", "Sich erinnern", "Komma ihåg"],
    "Forget": ["忘记", "भूलना", "Oublier", "לשכוח", "Olvidar", "மறக்க", "忘れる", "잊다", "Vergessen", "Glömma"],
    "Choose": ["选择", "चुनना", "Choisir", "לבחור", "Elegir", "தேர்வு செய்ய", "選ぶ", "선택하다", "Wählen", "Välja"],
    "Change": ["改变", "बदलना", "Changer", "לשנות", "Cambiar", "மாற்ற", "変える", "바꾸다", "Ändern", "Ändra"],
    "Move": ["移动", "हिलना", "Bouger", "לזוז", "Mover", "நகர", "動く", "움직이다", "Bewegen", "Röra sig"],

    "Turn": ["转", "मुड़ना", "Tourner", "לפנות", "Girar", "திரும்ப", "回る", "돌다", "Drehen", "Vända"],
    "Stop": ["停止", "रुकना", "Arrêter", "לעצור", "Parar", "நிறுத்த", "止まる", "멈추다", "Stoppen", "Stanna"],
    "Continue": ["继续", "जारी रखना", "Continuer", "להמשיך", "Continuar", "தொடர", "続ける", "계속하다", "Fortfahren", "Fortsätta"],
    "Begin": ["开始", "शुरू होना", "Commencer", "להתחיל", "Comenzar", "ஆரம்பிக்க", "始まる", "시작되다", "Beginnen", "Börja"],
    "End": ["结束", "समाप्त होना", "Terminer", "להסתיים", "Terminar", "முடிவடைய", "終わる", "끝나다", "Beenden", "Sluta"],
    "Win": ["赢", "जीतना", "Gagner", "לנצח", "Ganar", "வெற்றி பெற", "勝つ", "이기다", "Gewinnen", "Vinna"],
    "Lose": ["输", "हारना", "Perdre", "להפסיד", "Perder", "இழக்க", "負ける", "지다", "Verlieren", "Förlora"],
    "Meet": ["见面", "मिलना", "Rencontrer", "לפגוש", "Conocer", "சந்திக்க", "会う", "만나다", "Treffen", "Träffa"],
    "Follow": ["跟随", "पीछा करना", "Suivre", "לעקוב", "Seguir", "பின்தொடர", "従う", "따라가다", "Folgen", "Följa"],
    "Lead": ["领导", "नेतृत्व करना", "Diriger", "להוביל", "Liderar", "வழிநடத்த", "導く", "이끌다", "Führen", "Leda"],

    "Sit": ["坐", "बैठना", "S'asseoir", "לשבת", "Sentarse", "உட்கார", "座る", "앉다", "Sitzen", "Sitta"],
    "Stand": ["站", "खड़ा होना", "Se lever", "לעמוד", "Estar de pie", "நிற்க", "立つ", "서다", "Stehen", "Stå"],
    "Walk": ["走路", "चलना", "Marcher", "ללכת ברגל", "Caminar", "நடக்க", "歩く", "걷다", "Gehen", "Gå"],
    "Run": ["跑", "दौड़ना", "Courir", "לרוץ", "Correr", "ஓட", "走る", "달리다", "Rennen", "Springa"],
    "Sleep": ["睡觉", "सोना", "Dormir", "לישון", "Dormir", "தூங்க", "寝る", "자다", "Schlafen", "Sova"],
    "Wake up": ["醒来", "जागना", "Se réveiller", "להתעורר", "Despertar", "எழுந்திரு", "起きる", "일어나다", "Aufwachen", "Vakna"],
    "Eat": ["吃", "खाना", "Manger", "לאכול", "Comer", "சாப்பிட", "食べる", "먹다", "Essen", "Äta"],
    "Drink": ["喝", "पीना", "Boire", "לשתות", "Beber", "குடிக்க", "飲む", "마시다", "Trinken", "Dricka"],
    "Cook": ["做饭", "पकाना", "Cuisiner", "לבשל", "Cocinar", "சமைக்க", "料理する", "요리하다", "Kochen", "Laga mat"],
    "Clean": ["打扫", "साफ करना", "Nettoyer", "לנקות", "Limpiar", "சுத்தம் செய்ய", "掃除する", "청소하다", "Reinigen", "Städa"], 


    "Build": ["建造", "निर्माण करना", "Construire", "לבנות", "Construir", "கட்ட", "建てる", "짓다", "Bauen", "Bygga"],
    "Fix": ["修理", "ठीक करना", "Réparer", "לתקן", "Arreglar", "சரி செய்ய", "直す", "고치다", "Reparieren", "Fixa"],
    "Send": ["发送", "भेजना", "Envoyer", "לשלוח", "Enviar", "அனுப்பு", "送る", "보내다", "Senden", "Skicka"],
    "Receive": ["收到", "प्राप्त करना", "Recevoir", "לקבל", "Recibir", "பெறு", "受け取る", "받다", "Empfangen", "Ta emot"],
    "Learn": ["学习", "सीखना", "Apprendre", "ללמוד", "Aprender", "கற்க", "学ぶ", "배우다", "Lernen", "Lära"],
    "Teach": ["教", "सिखाना", "Enseigner", "ללמד", "Enseñar", "கற்பிக்க", "教える", "가르치다", "Lehren", "Undervisa"],
    "Travel": ["旅行", "यात्रा करना", "Voyager", "לטייל", "Viajar", "பயணம் செய்ய", "旅行する", "여행하다", "Reisen", "Resa"],
    "Work (verb)": ["工作", "काम करना", "Travailler", "לעבוד", "Trabajar", "வேலை செய்ய", "働く", "일하다", "Arbeiten", "Arbeta"],
    "Study": ["学习", "पढ़ाई करना", "Étudier", "ללמוד", "Estudiar", "படிக்க", "勉強する", "공부하다", "Studieren", "Studera"],
    "Practice": ["练习", "अभ्यास करना", "Pratiquer", "להתאמן", "Practicar", "பயிற்சி செய்ய", "練習する", "연습하다", "Üben", "Öva"], 

    "Strong": ["强壮", "मजबूत", "Fort", "חזק", "Fuerte", "வலிமையான", "強い", "강한", "Stark", "Stark"],
    "Weak": ["虚弱", "कमज़ोर", "Faible", "חלש", "Débil", "பலவீனமான", "弱い", "약한", "Schwach", "Svag"],
    "Heavy": ["重", "भारी", "Lourd", "כבד", "Pesado", "கனமான", "重い", "무거운", "Schwer", "Tung"],
    "Light (weight)": ["轻", "हल्का", "Léger", "קל", "Ligero", "இலகுவான", "軽い", "가벼운", "Leicht", "Lätt"],
    "Dark": ["黑暗", "अंधेरा", "Sombre", "חשוך", "Oscuro", "இருள்", "暗い", "어두운", "Dunkel", "Mörk"],
    "Bright": ["明亮", "चमकीला", "Brillant", "בהיר", "Brillante", "பிரகாசமான", "明るい", "밝은", "Hell", "Ljus"],
    "Clean (adj)": ["干净", "साफ", "Propre", "נקי", "Limpio", "சுத்தமான", "きれい", "깨끗한", "Sauber", "Ren"],
    "Dirty": ["脏", "गंदा", "Sale", "מלוכלך", "Sucio", "அழுக்கு", "汚い", "더러운", "Schmutzig", "Smutsig"],
    "Full": ["满", "भरा हुआ", "Plein", "מלא", "Lleno", "நிறைந்த", "いっぱい", "가득한", "Voll", "Full"],
    "Empty": ["空", "खाली", "Vide", "ריק", "Vacío", "காலி", "空", "빈", "Leer", "Tom"], 

    "Young": ["年轻", "युवा", "Jeune", "צעיר", "Joven", "இளம்", "若い", "젊은", "Jung", "Ung"],
    "Old": ["年老", "बूढ़ा", "Vieux", "זקן", "Viejo", "முதிய", "古い", "늙은", "Alt", "Gammal"],
    "New": ["新的", "नया", "Nouveau", "חדש", "Nuevo", "புதிய", "新しい", "새로운", "Neu", "Ny"],
    "Beautiful": ["美丽", "सुंदर", "Beau", "יפה", "Hermoso", "அழகான", "美しい", "아름다운", "Schön", "Vacker"],
    "Ugly": ["丑", "बदसूरत", "Laid", "מכוער", "Feo", "அசிங்கமான", "醜い", "못생긴", "Hässlich", "Ful"],
    "Cheap": ["便宜", "सस्ता", "Bon marché", "זול", "Barato", "மலிவு", "安い", "싼", "Billig", "Billig"],
    "Expensive": ["贵", "महंगा", "Cher", "יקר", "Caro", "விலையுயர்ந்த", "高い", "비싼", "Teuer", "Dyr"],
    "Interesting": ["有趣", "दिलचस्प", "Intéressant", "מעניין", "Interesante", "சுவாரஸ்யமான", "面白い", "흥미로운", "Interessant", "Intressant"],
    "Important (adj)": ["重要的", "महत्वपूर्ण", "Important", "חשוב", "Importante", "முக்கியமான", "重要な", "중요한", "Wichtig", "Viktig"],
    "Necessary": ["必要", "ज़रूरी", "Nécessaire", "נחוץ", "Necesario", "தேவையான", "必要な", "필수적인", "Notwendig", "Nödvändig"], 

    "Health": ["健康", "स्वास्थ्य", "Santé", "בריאות", "Salud", "ஆரோக்கியம்", "健康", "건강", "Gesundheit", "Hälsa"],
    "Body": ["身体", "शरीर", "Corps", "גוף", "Cuerpo", "உடல்", "体", "몸", "Körper", "Kropp"],
    "Head": ["头", "सिर", "Tête", "ראש", "Cabeza", "தலை", "頭", "머리", "Kopf", "Huvud"],
    "Hand": ["手", "हाथ", "Main", "יד", "Mano", "கை", "手", "손", "Hand", "Hand"],
    "Eye": ["眼睛", "आँख", "Œil", "עין", "Ojo", "கண்", "目", "눈", "Auge", "Öga"],
    "Ear": ["耳朵", "कान", "Oreille", "אוזן", "Oreja", "காது", "耳", "귀", "Ohr", "Öra"],
    "Mouth": ["嘴", "मुंह", "Bouche", "פה", "Boca", "வாய்", "口", "입", "Mund", "Mun"],
    "Heart": ["心", "दिल", "Cœur", "לב", "Corazón", "இதயம்", "心臓", "심장", "Herz", "Hjärta"],
    "Mind": ["思想", "मन", "Esprit", "מוח", "Mente", "மனம்", "心", "마음", "Geist", "Sinne"],
    "Face": ["脸", "चेहरा", "Visage", "פנים", "Cara", "முகம்", "顔", "얼굴", "Gesicht", "Ansikte"], 

    "Room": ["房间", "कमरा", "Pièce", "חדר", "Habitación", "அறை", "部屋", "방", "Zimmer", "Rum"],
    "Bed": ["床", "बिस्तर", "Lit", "מיטה", "Cama", "படுக்கை", "ベッド", "침대", "Bett", "Säng"],
    "Bathroom": ["浴室", "बाथरूम", "Salle de bain", "חדר אמבטיה", "Baño", "குளியலறை", "お風呂", "욕실", "Badezimmer", "Badrum"],
    "Kitchen": ["厨房", "रसोई", "Cuisine", "מטבח", "Cocina", "சமையலறை", "台所", "부엌", "Küche", "Kök"],
    "Office": ["办公室", "कार्यालय", "Bureau", "משרד", "Oficina", "அலுவலகம்", "オフィス", "사무실", "Büro", "Kontor"],
    "Job": ["工作", "नौकरी", "Emploi", "עבודה", "Empleo", "வேலை", "職業", "직업", "Job", "Jobb"],
    "Boss": ["老板", "बॉस", "Patron", "בוס", "Jefe", "முதலாளர்", "上司", "상사", "Chef", "Chef"],
    "Customer": ["顾客", "ग्राहक", "Client", "לקוח", "Cliente", "வாடிக்கையாளர்", "客", "고객", "Kunde", "Kund"],
    "Team": ["团队", "टीम", "Équipe", "צוות", "Equipo", "அணி", "チーム", "팀", "Team", "Team"],
    "Company": ["公司", "कंपनी", "Entreprise", "חברה", "Empresa", "நிறுவனம்", "会社", "회사", "Firma", "Företag"],

    "Minute": ["分钟", "मिनट", "Minute", "דקה", "Minuto", "நிமிடம்", "分", "분", "Minute", "Minut"],
    "Hour": ["小时", "घंटा", "Heure", "שעה", "Hora", "மணி", "時間", "시간", "Stunde", "Timme"],
    "Week": ["星期", "सप्ताह", "Semaine", "שבוע", "Semana", "வாரம்", "週", "주", "Woche", "Vecka"],
    "Month": ["月", "महीना", "Mois", "חודש", "Mes", "மாதம்", "月", "달", "Monat", "Månad"],
    "Year": ["年", "साल", "Année", "שנה", "Año", "ஆண்டு", "年", "년", "Jahr", "År"],
    "Morning": ["早晨", "सुबह", "Matin", "בוקר", "Mañana", "காலை", "朝", "아침", "Morgen", "Morgon"],
    "Evening": ["晚上", "शाम", "Soir", "ערב", "Tarde", "மாலை", "夕方", "저녁", "Abend", "Kväll"],
    "Season": ["季节", "मौसम", "Saison", "עונה", "Estación", "பருவம்", "季節", "계절", "Jahreszeit", "Säsong"],
    "North": ["北", "उत्तर", "Nord", "צפון", "Norte", "வடக்கு", "北", "북", "Norden", "Norr"],
    "South": ["南", "दक्षिण", "Sud", "דרום", "Sur", "தெற்கு", "南", "남", "Süden", "Söder"],

    "East": ["东", "पूर्व", "Est", "מזרח", "Este", "கிழக்கு", "東", "동", "Osten", "Öster"],
    "West": ["西", "पश्चिम", "Ouest", "מערב", "Oeste", "மேற்கு", "西", "서", "Westen", "Väster"],
    "Direction": ["方向", "दिशा", "Direction", "כיוון", "Dirección", "திசை", "方向", "방향", "Richtung", "Riktning"],
    "Place": ["地方", "जगह", "Endroit", "מקום", "Lugar", "இடம்", "場所", "장소", "Ort", "Plats"],
    "Area": ["地区", "क्षेत्र", "Zone", "אזור", "Área", "பகுதி", "地域", "지역", "Gebiet", "Område"],
    "Space": ["空间", "स्थान", "Espace", "מרחב", "Espacio", "விண்வெளி", "空間", "공간", "Raum", "Utrymme"],
    "Point": ["点", "बिंदु", "Point", "נקודה", "Punto", "புள்ளி", "点", "점", "Punkt", "Punkt"],
    "Line": ["线", "रेखा", "Ligne", "קו", "Línea", "கோடு", "線", "선", "Linie", "Linje"],
    "Side": ["边", "पक्ष", "Côté", "צד", "Lado", "பக்கம்", "側", "쪽", "Seite", "Sida"],
    "Middle": ["中间", "बीच", "Milieu", "אמצע", "Medio", "நடுத்தரம்", "真ん中", "가운데", "Mitte", "Mitten"],

    "Beginning": ["开始", "शुरुआत", "Début", "התחלה", "Inicio", "தொடக்கம்", "始まり", "시작", "Anfang", "Början"],
    "Ending": ["结尾", "अंत", "Fin", "סוף", "Final", "முடிவு", "終わり", "끝", "Ende", "Slut"], 

    "Chance": ["机会", "मौका", "Chance", "סיכוי", "Oportunidad", "வாய்ப்பு", "チャンス", "기회", "Chance", "Chans"],
    "Choice": ["选择", "चयन", "Choix", "בחירה", "Elección", "தேர்வு", "選択", "선택", "Wahl", "Val"],
    "Decision": ["决定", "निर्णय", "Décision", "החלטה", "Decisión", "முடிவு", "決定", "결정", "Entscheidung", "Beslut"],
    "Result": ["结果", "परिणाम", "Résultat", "תוצאה", "Resultado", "விளைவு", "結果", "결과", "Ergebnis", "Resultat"],
    "Effect": ["影响", "प्रभाव", "Effet", "השפעה", "Efecto", "விளைவு", "効果", "효과", "Effekt", "Effekt"],
    "Cause": ["原因", "कारण", "Cause", "גורם", "Causa", "காரணம்", "原因", "원인", "Ursache", "Orsak"],
    "Situation": ["情况", "स्थिति", "Situation", "מצב", "Situación", "நிலைமை", "状況", "상황", "Situation", "Situation"],
    "Condition": ["条件", "शर्त", "Condition", "תנאי", "Condición", "நிலை", "条件", "조건", "Bedingung", "Villkor"], 

    "Experience": ["经验", "अनुभव", "Expérience", "ניסיון", "Experiencia", "அனுபவம்", "経験", "경험", "Erfahrung", "Erfarenhet"],
    "Memory": ["记忆", "याद", "Mémoire", "זיכרון", "Memoria", "நினைவு", "記憶", "기억", "Gedächtnis", "Minne"],
    "Dream": ["梦", "सपना", "Rêve", "חלום", "Sueño", "கனவு", "夢", "꿈", "Traum", "Dröm"],
    "Hope": ["希望", "आशा", "Espoir", "תקווה", "Esperanza", "நம்பிக்கை", "希望", "희망", "Hoffnung", "Hopp"],
    "Fear": ["恐惧", "डर", "Peur", "פחד", "Miedo", "பயம்", "恐れ", "두려움", "Angst", "Rädsla"],
    "Happiness": ["幸福", "खुशी", "Bonheur", "אושר", "Felicidad", "மகிழ்ச்சி", "幸福", "행복", "Glück", "Lycka"],
    "Anger": ["愤怒", "गुस्सा", "Colère", "כעס", "Enojo", "கோபம்", "怒り", "분노", "Wut", "Ilska"],
    "Love (noun)": ["爱情", "प्रेम", "Amour", "אהבה", "Amor", "காதல்", "愛", "사랑", "Liebe", "Kärlek"],
    "Peace": ["和平", "शांति", "Paix", "שלום", "Paz", "அமைதி", "平和", "평화", "Frieden", "Fred"],
    "War": ["战争", "युद्ध", "Guerre", "מלחמה", "Guerra", "போர்", "戦争", "전쟁", "Krieg", "Krig"],

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

answer_counter = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lost In Translation")
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.SysFont("Times New Roman", 58)
body_font = pygame.font.SysFont("Times New Roman", 25)
button_font = pygame.font.SysFont("Times New Roman", 29)
counter_font = pygame.font.SysFont("Times New Roman", 30)

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
lang_index = 0
language_list = ["Chinese", "Hindi", "French", "Hebrew", "Spanish", "Tamil", "Japanese", "Korean", "German", "Swedish"]
# Game Functions
def get_random_word():
    if len(languages) > 0:
        english_word = random.choice(list(word_bank.keys()))
        lang_num = random.randint(0, len(languages)-1)
        correct_lang = languages[lang_num]
        lang_index = language_to_index[correct_lang]

        # [Chinese, Hindi, French, Hebrew, Spanish, Tamil, Japanese, Korean, German, Swedish]
        correct_translation = word_bank[english_word][lang_index]
        print(lang_index)
        language = language_list[lang_index]
        return english_word, language, correct_translation, lang_index

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

# Load the music file (WAV)
rickroll_sound = pygame.mixer.Sound("rickroll_proper.wav")
rickroll_sound.set_volume(0.5)

# Variable that keeps track if the music is playing
rickroll_playing = False


# Game State Initialization


# language button format
chinese_rect = pygame.Rect(50, 470, 120, 50)
hindi_rect = pygame.Rect(250, 470, 120, 50)
french_rect = pygame.Rect(450, 470, 120, 50)
hebrew_rect = pygame.Rect(650, 470, 120, 50)
spanish_rect = pygame.Rect(50, 520, 120, 50)
tamil_rect = pygame.Rect(250, 520, 120, 50)
japanese_rect = pygame.Rect(450, 520, 120, 50)
korean_rect = pygame.Rect(650, 520, 120, 50)
german_rect = pygame.Rect(550, 470, 120, 50)
swedish_rect = pygame.Rect(550, 520, 120, 50)

# boulder speeds button format
min_speed = pygame.Rect(550, 320, 120, 50)
med_speed = pygame.Rect(550, 370, 120, 50)
max_speed = pygame.Rect(550, 420, 120, 50)

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
                        english_word, language, correct_translation, lang_index = get_random_word()
                        # lang_index = languages.index(language)
                        
                        answers = generate_answers(correct_translation, lang_index)
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
                            english_word, language, correct_translation, lang_index = get_random_word()
                            # lang_index = languages.index(language)
                            answers = generate_answers(correct_translation, lang_index)
                            
                            # Clears all bullets
                            shots.clear()
                            for i, box in enumerate(answer_boxes[:]):
                                boulder_speeds = [random.uniform(0.75, max_boulder_speed) for _ in answer_boxes]
                                # boulder_drift = [random.uniform(-0.6, 0.6) for _ in answer_boxes]
                                box_y = random.randint(0, box_size)
                                box.y = -box_y
                            boulder_angles = [0 for _ in answer_boxes]  # initial rotation for each boulder
                            boulder_rotation_speeds = [random.uniform(-5, 5) for _ in answer_boxes]  # degrees per frame

                        else:
                            # Wrong answer: trigger game over
                            game_on = False
                            game_over = True

                            shots.clear()


    # GAME OVER STATE
    elif game_over:

        if not rickroll_playing:
            # Play music (loops infinitely)
            rickroll_channel = rickroll_sound.play(-1)
            rickroll_playing = True

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

            rickroll_channel.stop()
            rickroll_playing = False # Stops music

            # RESET GAME
            answer_counter = 0
            shots.clear()

            english_word, language, correct_translation, lang_index = get_random_word()
            # lang_index = languages.index(language)
            answers = generate_answers(correct_translation, lang_index)

            player_ufo.rect.x = 300
            player_ufo.rect.y = 470

            for i, box in enumerate(answer_boxes[:]):
                box.y = -box_size
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
