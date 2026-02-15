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
    "Hello (polite)": ["您好", "nín hǎo"],
    "Excuse me": ["不好意思", "bù hǎo yì si"],
    "May I ask…": ["请问", "qǐng wèn"],
    "See you tomorrow": ["明天见", "míng tiān jiàn"],
    "How are you?": ["你好吗？", "nǐ hǎo ma?"],
    "I'm very well": ["我很好", "wǒ hěn hǎo"],
    "You're welcome": ["不客气", "bú kè qi"],
    "Sorry": ["对不起", "duì bù qǐ"],
    "No problem": ["没关系", "méi guān xi"],
    "Please": ["请", "qǐng"],
    "He / Him": ["他", "tā"],
    "She / Her": ["她", "tā"],
    "I / Me": ["我", "wǒ"],
    "You": ["你", "nǐ"],
    "We / Us": ["我们", "wǒ men"],
    "They": ["他们", "tā men"],
    "You (plural)": ["你们", "nǐ men"],
    "You (formal)": ["您", "nín"],
    "Keep going": ["加油", "jiā yóu"],
    "Goodbye": ["再见", "zài jiàn"],
    "Bye bye": ["拜拜", "bāi bāi"],
    "See you later": ["一会儿见", "yí huìr jiàn"],
    "Good night": ["晚安", "wǎn ān"],
    "Take care": ["保重", "bǎo zhòng"],
    "Welcome": ["欢迎", "huān yíng"],
    "Hobby": ["兴趣", "xìng qù"],
    "Study": ["学习", "xué xí"],
    "Study abroad": ["留学", "liú xué"],
    "University": ["大学", "dà xué"],
    "High school": ["高中", "gāo zhōng"],
    "Name": ["名字", "míng zì"],
    "Surname": ["姓", "xìng"],
    "Currently": ["现在", "xiàn zài"],
    "English name": ["英文名字", "yīng wén míng zì"],
    "Age": ["年龄", "nián líng"],
    "Years old": ["岁", "suì"],
    "Born": ["出生", "chū shēng"],
    "Place of birth": ["出生地", "chū shēng dì"],
    "Come from": ["来自", "lái zì"],
    "Country": ["国家", "guó jiā"],
    "Gender": ["性别", "xìng bié"],
    "Phone number": ["电话号码", "diàn huà hào mǎ"],
    "City": ["城市", "chéng shì"],
    "Live in": ["住在", "zhù zài"],
    "Address": ["地址", "dì zhǐ"],
    "Male": ["男", "nán"],
    "Female": ["女", "nǚ"],
    "Email": ["邮箱", "yóu xiāng"],
    "Graduate": ["毕业", "bì yè"],
    "Hometown": ["家乡", "jiā xiāng"],
    "Company": ["公司", "gōng sī"],
    "Job": ["工作", "gōng zuò"],
    "Like": ["喜欢", "xǐ huan"],
    "Go to work": ["上班", "shàng bān"],
    "Major": ["专业", "zhuān yè"],
    "Dream": ["梦想", "mèng xiǎng"],
    "Language": ["语言", "yǔ yán"],
    "Can speak": ["会说", "huì shuō"],
    "A little": ["一点", "yì diǎn"],
    "Chinese (language)": ["中文", "zhōng wén"],
    "English (language)": ["英文", "yīng wén"],
    "Hobby": ["爱好", "ài hào"],
    "Travel": ["旅游", "lǚ yóu"],
    "Music": ["音乐", "yīn yuè"],
    "Read books": ["看书", "kàn shū"],
    "Listen to music": ["听音乐", "tīng yīn yuè"],
    "Watch movies": ["看电影", "kàn diàn yǐng"],
    "Personality": ["性格", "xìng gé"],
    "Birthday": ["生日", "shēng rì"],
    "Introduce": ["介绍", "jiè shào"],
    "Family": ["家庭", "jiā tíng"],
    "Parents": ["父母", "fù mǔ"],
    "Siblings": ["兄弟姐妹", "xiōng dì jiě mèi"],
    "Strength": ["优点", "yōu diǎn"],
    "Weakness": ["缺点", "quē diǎn"],
    "Here": ["这里", "zhè lǐ"],
    "There": ["那里", "nà lǐ"],
    "Where": ["哪儿", "nǎr"],
    "Above / On": ["上", "shàng"],
    "Below / Under": ["下", "xià"],
    "Left side": ["左边", "zuǒ biān"],
    "Right side": ["右边", "yòu biān"],
    "In front": ["前面", "qián miàn"],
    "Behind": ["后面", "hòu miàn"],
    "Beside": ["旁边", "páng biān"],
    "Middle": ["中间", "zhōng jiān"],
    "Opposite": ["对面", "duì miàn"],
    "Nearby": ["附近", "fù jìn"],
    "Far": ["远", "yuǎn"],
    "Near": ["近", "jìn"],
    "Arrive": ["到", "dào"],
    "Exit": ["出口", "chū kǒu"],
    "Entrance": ["入口", "rù kǒu"],
    "Flower shop": ["花店", "huā diàn"],
    "Pharmacy": ["药店", "yào diàn"],
    "Barber shop": ["理发店", "lǐ fà diàn"],
    "Cinema": ["电影院", "diàn yǐng yuàn"],
    "Zoo": ["动物园", "dòng wù yuán"],
    "Laundry": ["洗衣店", "xǐ yī diàn"],
    "Parking lot": ["停车场", "tíng chē chǎng"],
    "Company": ["公司", "gōng sī"],
    "Swimming pool": ["游泳池", "yóu yǒng chí"],
    "Stadium": ["体育场", "tǐ yù chǎng"],
    "Bus stop": ["公共汽车站", "gōng gòng qì chē zhàn"],
    "Subway station": ["地铁站", "dì tiě zhàn"],
    "Train station": ["火车站", "huǒ chē zhàn"],
    "Airport": ["机场", "jī chǎng"],
    "Overpass": ["天桥", "tiānqiáo"],
    "Market": ["市场", "shìchǎng"],
    "Bank": ["银行", "yín háng"],
    "Supermarket": ["超市", "chāo shì"],
    "Restaurant": ["饭店", "fàn diàn"],
    "Factory": ["工厂", "gōngchǎng"],
    "Temple": ["寺庙", "sìmiào"],
    "Shop": ["商店", "shāng diàn"],
    "Bookstore": ["书店", "shū diàn"],
    "Café": ["咖啡馆", "kā fēi guǎn"],
    "worEateryd": ["饭馆", "fànguǎn"],
    "Park": ["公园", "gōng yuán"],
    "Square": ["广场", "guǎng chǎng"],
    "Embassy": ["大使馆", "dà shǐ guǎn"],
    "Museum": ["博物馆", "bó wù guǎn"],
    "Library": ["图书馆", "tú shū guǎn"],
    "Gymnasium": ["体育馆", "tǐ yù guǎn"],
    "Restroom": ["洗手间", "xǐ shǒu jiān"],
    "Playground": ["游乐场", "yóu lè chǎng"],
    "Elevator": ["电梯", "diàn tī"],
    "Stairs": ["楼梯", "lóu tī"],
    "First floor": ["一楼", "yī lóu"],
    "Second floor": ["二楼", "èr lóu"],
    "Basement": ["地下室", "dì xià shì"],
    "Main road": ["马路", "mǎ lù"],
    "Sidewalk": ["人行道", "rén xíng dào"],
    "Traffic light": ["红绿灯", "hóng lǜ dēng"],
    "Direction": ["方向", "fāng xiàng"],
    "Mountain": ["山", "shān"],
    "River": ["河", "hé"],
    "Lake": ["湖", "hú"],
    "Sea": ["海", "hǎi"],
    "City": ["城市", "chéng shì"],
    "Road": ["路", "lù"],
    "Dormitory": ["宿舍", "sù shè"],
    "House": ["房子", "fáng zi"],
    "Villa": ["别墅", "bié shù"],
    "Customs": ["海关", "hǎi guān"],
    "Office": ["办公室", "bàngōngshì"],
    "School": ["学校", "xuéxiào"],
    "Hospital": ["医院", "yīyuàn"],
    "Church": ["教堂", "jiàotáng"],
    "Supermarket": ["超市", "chāoshì"],
    "Hotel": ["酒店", "jiǔdiàn"],
    "East": ["东", "dōng"],
    "West": ["西", "xī"],
    "South": ["南", "nán"],
    "North": ["北", "běi"],
    "Bar": ["酒吧", "jiǔbā"],
    "Teahouse": ["茶馆", "cháguǎn"],
    "Gym": ["健身房", "jiànshēnfáng"],
    "Academy": ["学院", "xuéyuàn"],
    "Police station": ["派出所", "pàichūsuǒ"],
    "Court": ["法院", "fǎyuàn"],
    "Balcony": ["阳台", "yángtái"],
    "Bakery": ["面包店", "miànbāodiàn"],
    "Beauty salon": ["美容院", "měiróngyuàn"],
    "Law firm": ["律师事务所", "lǜshī shìwùsuǒ"],
    "Doctor": ["医生", "yī shēng"],
    "Nurse": ["护士", "hù shì"],
    "Pharmacist": ["药剂师", "yào jì shī"],
    "Hairdresser": ["理发师", "lǐ fà shī"],
    "Dentist": ["牙医", "yá yī"],
    "Veterinarian": ["兽医", "shòu yī"],
    "Teacher": ["老师", "lǎo shī"],
    "Professor": ["教授", "jiào shòu"],
    "Student": ["学生", "xué shēng"],
    "Principal": ["校长", "xiào zhǎng"],
    "Worker": ["工人", "gōng rén"],
    "Architect": ["建筑师", "jiàn zhù shī"],
    "Engineer": ["工程师", "gōng chéng shī"],
    "Electrician": ["电工", "diàn gōng"],
    "Carpenter": ["木工", "mù gōng"],
    "Plumber": ["水管工", "shuǐ guǎn gōng"],
    "Driver": ["司机", "sī jī"],
    "Psychologist": ["心理医生", "xīn lǐ yī shēng"],
    "Purchasing Officer": ["采购员", "cǎi gòu yuán"],
    "Pilot": ["飞行员", "fēi xíng yuán"],
    "Flight Attendant (Female)": ["空姐", "kōng jiě"],
    "Flight Attendant (Male)": ["空少", "kōng shào"],
    "Businessperson": ["商人", "shāng rén"],
    "Boss": ["老板", "lǎo bǎn"],
    "Manager": ["经理", "jīng lǐ"],
    "Office Worker": ["职员", "zhí yuán"],
    "Secretary": ["秘书", "mì shū"],
    "Accountant": ["会计", "kuài jì"],
    "Cashier": ["出纳", "chū nà"],
    "Chef": ["厨师", "chúshī"],
    "Programmer": ["程序员", "chéng xù yuán"],
    "Animator": ["动画师", "dòng huà shī"],
    "Designer": ["设计师", "shè jì shī"],
    "Barista": ["咖啡师", "kā fēi shī"],
    "Consultant": ["顾问", "gù wèn"],
    "Scientist": ["科学家", "kē xué jiā"],
    "Model": ["模特", "mó tè"],
    "Artist": ["艺术家", "yì shù jiā"],
    "Actor": ["演员", "yǎn yuán"],
    "Singer": ["歌手", "gē shǒu"],
    "Musician": ["音乐家", "yīn yuè jiā"],
    "Dancer": ["舞蹈家", "wǔ dǎo jiā"],
    "Photographer": ["摄影师", "shè yǐng shī"],
    "Painter": ["画家", "huà jiā"],
    "Writer": ["作家", "zuò jiā"],
    "Journalist": ["记者", "jì zhě"],
    "Editor": ["编辑", "biān jí"],
    "Caregiver": ["护理师", "hù lǐ shī"],
    "Host / MC": ["主持人", "zhǔ chí rén"],
    "Director": ["导演", "dǎo yǎn"],
    "Screenwriter": ["编剧", "biān jù"],
    "Translator": ["翻译", "fān yì"],
    "Auditor": ["审计师", "shěn jì shī"],
    "Coach": ["教练", "jiào liàn"],
    "Athlete": ["运动员", "yùn dòng yuán"],
    "Tour Guide": ["导游", "dǎo yóu"],
    "Waiter/Waitress": ["服务员", "fú wù yuán"],
    "Cashier": ["收银员", "shōu yín yuán"],
    "Security Guard": ["保安", "bǎo ān"],
    "Police Officer": ["警察", "jǐng chá"],
    "Firefighter": ["消防员", "xiāo fáng yuán"],
    "Lawyer": ["律师", "lǜ shī"],
    "Judge": ["法官", "fǎ guān"],
    "Civil Servant": ["公务员", "gōng wù yuán"],
    "Politician": ["政治家", "zhèng zhì jiā"],
    "President": ["总统", "zǒng tǒng"],
    "Mayor": ["市长", "shì zhǎng"],
    "Farmer": ["农民", "nóng mín"],
    "Fisherman": ["渔民", "yú mín"],
    "Craftsman": ["工匠", "gōng jiàng"],
    "Cleaner": ["清洁工", "qīng jié gōng"],
    "Mail Carrier": ["邮递员", "yóu dì yuán"],
    "Courier": ["快递员", "kuài dì yuán"],
    "Nanny": ["保姆", "bǎo mǔ"],
    "Soldier": ["军人", "jūn rén"],
    "Forensic Doctor": ["法医", "fǎ yī"],
    "Technician": ["技术员", "jì shù yuán"],
    "Tailor": ["裁缝", "cái féng"],
    "Intern": ["实习生", "shí xí shēng"],
    "Shopping": ["购物", "gòu wù"],
    "Market": ["市场", "shì chǎng"],
    "Shop": ["商店", "shāng diàn"],
    "Supermarket": ["超市", "chāo shì"],
    "Department store": ["百货商店", "bǎi huò shāng diàn"],
    "Shopping mall": ["购物中心", "gòu wù zhōng xīn"],
    "Convenience store": ["便利店", "biàn lì diàn"],
    "Discount": ["折扣", "zhékòu"],
    "Customer": ["顾客", "gù kè"],
    "Price": ["价格", "jià gé"],
    "Sale": ["打折", "dǎ zhé"],
    "Cheap": ["便宜", "pián yi"],
    "worExpensived": ["贵", "guì"],
    "Large size": ["大号", "dà hào"],
    "Medium size": ["中号", "zhōng hào"],
    "Small size": ["小号", "xiǎo hào"],
    "Payment": ["付款", "fù kuǎn"],
    "Cash": ["现金", "xiàn jīn"],
    "Credit card": ["信用卡", "xìn yòng kǎ"],
    "Alipay": ["支付宝", "zhī fù bǎo"],
    "WeChat Pay": ["微信支付", "wēi xìn zhī fù"],
    "Give change": ["找钱", "zhǎo qián"],
    "Receipt": ["收据", "shōu jù"],
    "Invoice": ["发票", "fā piào"],
    "Return goods": ["退货", "tuì huò"],
    "Exchange goods": ["换货", "huàn huò"],
    "Warranty": ["保修", "bǎo xiū"],
    "Promotion": ["促销", "cù xiāo"],
    "Packaging": ["包装", "bāo zhuāng"],
    "Label": ["标签", "biāo qiān"],
    "Product": ["商品", "shāng pǐn"],
    "Quality": ["质量", "zhì liàng"],
    "Review": ["评价", "píng jià"],
    "Online shopping": ["网购", "wǎng gòu"],
    "Express delivery": ["快递", "kuài dì"],
    "Shipping fee": ["运费", "yùn fèi"],
    "Arrival of goods": ["到货", "dào huò"],
    "Out of stock": ["缺货", "quē huò"],
    "New arrivals": ["上新", "shàng xīn"],
    "Size": ["尺码", "chǐ mǎ"],
    "Try on": ["试穿", "shì chuān"],
    "Style": ["款式", "kuǎn shì"],
    "Colour": ["颜色", "yán sè"],
    "Quantity": ["数量", "shù liàng"],
    "Style": ["风格", "fēng gé"],
    "Brand": ["品牌", "pǐn pái"],
    "Place an order": ["下单", "xià dān"],
    "Member": ["会员", "huì yuán"],
    "Reward points": ["积分", "jī fēn"],
    "Gift": ["礼品", "lǐ pǐn"],
    "Jogging": ["跑步", "pǎo bù"],
    "Walking": ["散步", "sàn bù"],
    "Swimming": ["游泳", "yóu yǒng"],
    "Cycling": ["骑车", "qí chē"],
    "Driving": ["开车", "kāi chē"],
    "Walking": ["走路", "zǒu lù"],
    "Playing basketball": ["打篮球", "dǎ lán qiú"],
    "Playing soccer": ["踢足球", "tī zú qiú"],
    "Playing badminton": ["打羽毛球", "dǎ yǔ máo qiú"],
    "Playing tennis": ["打网球", "dǎ wǎng qiú"],
    "Hiking": ["爬山", "pá shān"],
    "Camping": ["露营", "lù yíng"],
    "Fishing": ["钓鱼", "diào yú"],
    "Singing": ["唱歌", "chàng gē"],
    "Dancing": ["跳舞", "tiào wǔ"],
    "Drawing": ["画画", "huà huà"],
    "Watching movies": ["看电影", "kàn diàn yǐng"],
    "Watching TV": ["看电视", "kàn diàn shì"],
    "Listening to music": ["听音乐", "tīng yīn yuè"],
    "Reading books": ["看书", "kàn shū"],
    "Writing": ["写字", "xiě zì"],
    "Studying": ["学习", "xué xí"],
    "Doing homework": ["做作业", "zuò zuò yè"],
    "Attending class": ["上课", "shàng kè"],
    "Finishing class": ["下课", "xià kè"],
    "Working": ["工作", "gōng zuò"],
    "Overtime": ["加班", "jiā bān"],
    "Having a meeting": ["开会", "kāi huì"],
    "Cooking": ["做饭", "zuò fàn"],
    "Eating": ["吃饭", "chī fàn"],
    "Drinking water": ["喝水", "hē shuǐ"],
    "Sleeping": ["睡觉", "shuì jiào"],
    "Getting up": ["起床", "qǐ chuáng"],
    "Taking a shower": ["洗澡", "xǐ zǎo"],
    "Brushing teeth": ["刷牙", "shuā yá"],
    "Washing face": ["洗脸", "xǐ liǎn"],
    "Doing laundry": ["洗衣服", "xǐ yī fú"],
    "Visiting": ["参观", "cān guān"],
    "Tidying up": ["收拾", "shōu shi"],
    "Shopping": ["买东西", "mǎi dōng xi"],
    "Surfing the Internet": ["上网", "shàng wǎng"],
    "Chatting": ["聊天", "liáo tiān"],
    "Taking photos": ["拍照", "pāi zhào"],
    "Using the phone": ["玩手机", "wán shǒu jī"],
    "Playing games": ["玩游戏", "wán yóu xì"],
    "Shopping": ["购物", "gòu wù"],
    "Traveling": ["旅游", "lǚ yóu"],
    "Filming videos": ["拍视频", "pāi shì pín"],
    "Exercising": ["做运动", "zuò yùn dòng"],
    "Eat": ["吃", "chī"],
    "Drink": ["喝", "hē"],
    "Cook": ["做饭", "zuò fàn"],
    "Boil": ["煮", "zhǔ"],
    "Stir-fry": ["炒", "chǎo"],
    "Braise": ["烧", "shāo"],
    "Roast": ["烤", "kǎo"],
    "Steam": ["蒸", "zhēng"],
    "Stew": ["炖", "dùn"],
    "Cut": ["切", "qiē"],
    "Peel": ["剥", "bāo"],
    "Stir": ["搅拌", "jiǎo bàn"],
    "Pour": ["倒", "dào"],
    "Hungry": ["饿", "è"],
    "Full": ["饱", "bǎo"],
    "Thirsty": ["渴", "kě"],
    "Delicious": ["好吃", "hǎo chī"],
    "Order food": ["点菜", "diǎn cài"],
    "Pay bill": ["结账", "jié zhàng"],
    "Takeout": ["外卖", "wài mài"],
    "Menu": ["菜单", "cài dān"],
    "Sweet": ["甜", "tián"],
    "Salty": ["咸", "xián"],
    "Sour": ["酸", "suān"],
    "Spicy": ["辣", "là"],
    "Bitter": ["苦", "kǔ"],
    "Light taste": ["淡", "dàn"],
    "Mild": ["清淡", "qīng dàn"],
    "Snacks": ["零食", "líng shí"],
    "Beverage": ["饮料", "yǐn liào"],
    "Water": ["水", "shuǐ"],
    "Tea": ["茶", "chá"],
    "Coffee": ["咖啡", "kā fēi"],
    "Juice": ["果汁", "guǒ zhī"],
    "Milk": ["牛奶", "niú nǎi"],
    "Beer": ["啤酒", "pí jiǔ"],
    "Rice/meal": ["饭", "fàn"],
    "White rice": ["米饭", "mǐ fàn"],
    "Noodles": ["面条", "miàn tiáo"],
    "Porridge": ["粥", "zhōu"],
    "Soup": ["汤", "tāng"],
    "Steamed bun": ["包子", "bāo zi"],
    "Dumplings": ["饺子", "jiǎo zi"],
    "Bread": ["面包", "miàn bāo"],
    "Egg": ["鸡蛋", "jī dàn"],
    "Chicken": ["鸡肉", "jī ròu"],
    "Beef": ["牛肉", "niú ròu"],
    "Pork": ["猪肉", "zhū ròu"],
    "Fish": ["鱼", "yú"],
    "Shrimp": ["虾", "xiā"],
    "Vegetables": ["蔬菜", "shū cài"],
    "Potato": ["土豆", "tǔ dòu"],
    "Carrot": ["胡萝卜", "hú luó bo"],
    "Tomato": ["西红柿", "xī hóng shì"],
    "Onion": ["洋葱", "yáng cōng"],
    "Chili": ["辣椒", "là jiāo"],
    "Soy sauce": ["酱油", "jiàng yóu"],
    "Vinegar": ["醋", "cù"],
    "Salt": ["盐", "yán"],
    "Sugar": ["糖", "táng"],
    "Hotpot": ["火锅", "huǒ guō"],
    "Barbecue": ["烧烤", "shāo kǎo"],
    "Fried chicken": ["炸鸡", "zhà jī"],
    "Chocolate": ["巧克力", "qiǎo kè lì"],
    "Ice cream": ["冰淇淋", "bīng qí lín"],
    "Fresh": ["新鲜", "xīn xiān"],
    "Chopsticks": ["筷子", "kuài zi"],
    "Spoon": ["勺子", "sháo zi"],
    "Taste": ["味道", "wèi dào"],
    "Fragrant": ["香", "xiāng"],
    "Family": ["家庭", "jiā tíng"],
    "Family members": ["家人", "jiā rén"],
    "Father (formal)": ["父亲", "fù qīn"],
    "Mother (formal)": ["母亲", "mǔ qīn"],
    "Dad": ["爸爸", "bà ba"],
    "Mom": ["妈妈", "mā ma"],
    "Grandfather (paternal)": ["爷爷", "yé ye"],
    "Grandmother (paternal)": ["奶奶", "nǎi nai"],
    "Grandfather (maternal)": ["外公", "wài gōng"],
    "Grandmother (maternal)": ["外婆", "wài pó"],
    "Older brother": ["哥哥", "gē ge"],
    "Younger brother": ["弟弟", "dì di"],
    "Older sister": ["姐姐", "jiě jie"],
    "Younger sister": ["妹妹", "mèi mei"],
    "Brothers": ["兄弟", "xiōng dì"],
    "Sisters": ["姐妹", "jiě mèi"],
    "Son": ["儿子", "ér zi"],
    "Daughter": ["女儿", "nǚ ér"],
    "Grandson (paternal)": ["孙子", "sūn zi"],
    "Granddaughter (paternal)": ["孙女", "sūn nǚ"],
    "Grandson (maternal)": ["外孙", "wài sūn"],
    "Granddaughter (maternal)": ["外孙女", "wài sūn nǚ"],
    "Husband": ["丈夫", "zhàng fū"],
    "Wife": ["妻子", "qī zi"],
    "Uncle (father's older brother)": ["伯伯", "bó bo"],
    "Uncle (father's younger brother)": ["叔叔", "shū shu"],
    "Aunt (mother's sister)": ["阿姨", "ā yí"],
    "Uncle (mother's brother)": ["舅舅", "jiù jiu"],
    "Aunt (father's sister)": ["姑姑", "gū gu"],
    "Cousins (paternal side)": ["堂兄弟姐妹", "táng xiōng dì jiě mèi"],	
    "Colour": ["颜色", "yán sè"],
    "Red": ["红色", "hóng sè"],
    "Blue": ["蓝色", "lán sè"],
    "Yellow": ["黄色", "huáng sè"],
    "Green": ["绿色", "lǜ sè"],
    "Black": ["黑色", "hēi sè"],
    "White": ["白色", "bái sè"],
    "Gray": ["灰色", "huī sè"],
    "Brown": ["棕色", "zōng sè"],
    "Orange": ["橙色", "chéng sè"],
    "Purple": ["紫色", "zǐ sè"],
    "Pink": ["粉红色", "fěn hóng sè"],
    "Silver": ["银色", "yín sè"],
    "Gold": ["金色", "jīn sè"],
    "Dark colour": ["深色", "shēn sè"],
    "Light colour": ["浅色", "qiǎn sè"],
    "Multicolored": ["彩色", "cǎi sè"],
    "Beige": ["米色", "mǐ sè"],
    "Cyan (classical)": ["青色", "qīng sè"],
    "Sky blue": ["天蓝色", "tiān lán sè"],
    "Cobalt blue": ["宝蓝色", "bǎo lán sè"],
    "Olive green": ["橄榄绿", "gǎn lǎn lǜ"],
    "Coffee colour": ["咖啡色", "kā fēi sè"],
    "Camel color": ["驼色", "tuó sè"],
    "Bright color": ["亮色", "liàng sè"],
    "Dark color": ["暗色", "àn sè"],
    "Lemon yellow": ["柠檬黄", "níng méng huáng"],
    "Coral red": ["珊瑚红", "shān hú hóng"],
    "Wine red": ["酒红色", "jiǔ hóng sè"],
    "Smoky gray": ["烟灰色", "yān huī sè"],
    "Fruit": ["水果", "shuǐ guǒ"],
    "Apple": ["苹果", "píng guǒ"],
    "Banana": ["香蕉", "xiāng jiāo"],
    "Watermelon": ["西瓜", "xī guā"],
    "Grape": ["葡萄", "pú táo"],
    "Orange": ["橙子", "chéng zi"],
    "Lemon": ["柠檬", "níng méng"],
    "Pomelo": ["柚子", "yòu zi"],
    "Mango": ["芒果", "máng guǒ"],
    "Strawberry": ["草莓", "cǎo méi"],
    "Blueberry": ["蓝莓", "lán méi"],
    "Cherry": ["樱桃", "yīng táo"],
    "Lychee": ["荔枝", "lì zhī"],
    "Longan": ["龙眼", "lóng yǎn"],
    "Durian": ["榴莲", "liú lián"],
    "Dragon fruit": ["火龙果", "huǒ lóng guǒ"],
    "Pomegranate": ["石榴", "shí liú"],
    "Kiwi": ["猕猴桃", "mí hóu táo"],
    "Hami melon": ["哈密瓜", "hā mì guā"],
    "Papaya": ["木瓜", "mù guā"],
    "Pear": ["梨", "lí"],
    "Coconut": ["椰子", "yē zi"],
    "Plum": ["梅子", "méi zi"],
    "Pineapple": ["菠萝", "bōluó"],
    "Raspberry": ["覆盆子", "fù pén zi"],
    "Sugarcane": ["甘蔗", "gān zhè"],
    "Tangerine": ["桔子", "jú zi"],
    "Mangosteen": ["山竹", "shān zhú"],
    "Mulberry": ["桑葚", "sāng shèn"],
    "Jujube": ["枣子", "zǎo zi"],
    "Persimmon": ["柿子", "shì zi"],
    "Yellow peach": ["黄桃", "huáng táo"],
    "Passion fruit": ["百香果", "bǎi xiāng guǒ"],
    "Jackfruit": ["菠萝蜜", "bō luó mì"],
    "Date (fruit)": ["椰枣", "yē zǎo"],
    "Grapefruit": ["葡萄柚", "pú táo yòu"],
    "Rambutan": ["红毛丹", "hóng máo dān"],
    "Avocado": ["牛油果", "niú yóu guǒ"],
    "Guava": ["番石榴", "fān shí liú"],
    "Starfruit": ["杨桃", "yáng táo"],
    "Honeydew melon": ["香瓜", "xiāng guā"],
    "Custard apple": ["释迦果", "shì jiā guǒ"],
    "Apricot": ["杏子", "xìng zi"],
    "Dried blueberry": ["蓝莓干", "lán méi gān"],
    "Sapodilla": ["人心果", "rén xīn guǒ"],
    "Year": ["年", "nián"],
    "Month": ["月", "yuè"],
    "Day (formal)": ["日", "rì"],
    "Day (common)": ["号", "hào"],
    "Week": ["星期", "xīng qī"],
    "Monday": ["星期一", "xīng qī yī"],
    "Tuesday": ["星期二", "xīng qī èr"],
    "Wednesday": ["星期三", "xīng qī sān"],
    "Thursday": ["星期四", "xīng qī sì"],
    "Friday": ["星期五", "xīng qī wǔ"],
    "Saturday": ["星期六", "xīng qī liù"],
    "Sunday": ["星期天 / 星期日", "xīng qī tiān / rì"],
    "Today": ["今天", "jīn tiān"],
    "Tomorrow": ["明天", "míng tiān"],
    "Yesterday": ["昨天", "zuó tiān"],
    "Day after tomorrow": ["后天", "hòu tiān"],
    "Day before yesterday": ["前天", "qián tiān"],
    "Every day": ["每天", "měi tiān"],
    "Every month": ["每月", "měi yuè"],
    "Every year": ["每年", "měi nián"],
    "This year": ["今年", "jīn nián"],
    "Next year": ["明年", "míng nián"],
    "Last year": ["去年", "qù nián"],
    "Last month": ["上个月", "shàng ge yuè"],
    "Next month": ["下个月", "xià ge yuè"],
    "Beginning of the month": ["月初", "yuè chū"],
    "Middle of the month": ["月中", "yuè zhōng"],
    "End of the month": ["月底", "yuè dǐ"],
    "Calendar": ["日历", "rì lì"],
    "Time": ["时间", "shí jiān"],
    "Date": ["日期", "rì qī"],
    "When?": ["什么时候", "shén me shí hòu"],
    "What month and day?": ["几月几号", "jǐ yuè jǐ hào"],
    "What time?": ["几点", "jǐ diǎn"],
    "Clock": ["时钟", "shí zhōng"],
    "one": ["一", "yī"],
    "two": ["二", "èr"],
    "three": ["三", "sān"],
    "four": ["四", "sì"],
    "five": ["五", "wǔ"],
    "six": ["六", "liù"],
    "seven": ["七", "qī"],
    "eight": ["八", "bā"],
    "nine": ["九", "jiǔ"],
    "ten": ["十", "shí"],
    "hundred": ["百", "bǎi"],
    "thousand": ["千", "qiān"],
    "ten thousand": ["万", "wàn"],
    "hundred million": ["亿", "yì"],
    "prefix for ordinal numbers": ["第", "dì"],
    "zero": ["零", "líng"],
    "half": ["一半", "yíbàn"],
    "pair": ["双", "shuāng"],
    "two": ["两", "liǎng"],
    "half": ["半", "bàn"],
    "many": ["多", "duō"],
    "few": ["少", "shǎo"],
    "how many/ several": ["幾", "jǐ"],
    "thousands upon thousands": ["成千上万", "chéng qiān shàng wàn"],
    "happy": ["开心", "kāixīn"],
    "sad": ["难过", "nánguò"],
    "angry": ["生气", "shēngqì"],
    "nervous": ["紧张", "jǐnzhāng"],
    "uneasy": ["不安", "bù'ān"],
    "excited": ["兴奋", "xīngfèn"],
    "disappointed": ["失望", "shīwàng"],
    "satisfied": ["满意", "mǎnyì"],
    "afraid": ["害怕", "hàipà"],
    "surprised": ["惊讶", "jīngyà"],
    "in pain": ["痛苦", "tòngkǔ"],
    "sorrowful": ["悲伤", "bēishāng"],
    "happy (blessed)": ["幸福", "xìngfú"],
    "worried": ["忧虑", "yōulǜ"],
    "at ease": ["安心", "ānxīn"],
    "furious": ["愤怒", "fènnù"],
    "lonely": ["孤单", "gūdān"],
    "troubled": ["烦恼", "fánnǎo"],
    "ashamed": ["羞愧", "xiūkuì"],
    "regret": ["后悔", "hòuhuǐ"],
    "sympathetic": ["同情", "tóngqíng"],
    "bored": ["无聊", "wúliáo"],
    "jealous": ["嫉妒", "jídù"],
    "melancholic": ["惆怅", "chóuchàng"],
    "look forward to": ["期待", "qīdài"],
    "miss (someone/something)": ["想念", "xiǎngniàn"],
    "sorrowful": ["忧伤", "yōushāng"],
    "touched (emotionally)": ["感动", "gǎndòng"],
    "terrified": ["恐惧", "kǒngjù"],
    "content": ["满足", "mǎnzú"],
    "embarrassed": ["难堪", "nánkān"],
    "anxious": ["焦虑", "jiāolǜ"],
    "dissatisfied": ["不满", "bùmǎn"],
    "panic": ["惊恐", "jīngkǒng"],
    "comforted": ["欣慰", "xīnwèi"],
    "lost (emotionally)": ["失落", "shīluò"],
    "annoyed": ["恼火", "nǎohuǒ"],
    "desperate": ["绝望", "juéwàng"],
    "bitter (emotionally)": ["心酸", "xīnsuān"],
    "nauseated / disgusted": ["恶心", "ěxīn"],
    "stirred / excited": ["激动", "jīdòng"],
    "moved (emotionally)": ["心动", "xīndòng"],
    "dislike": ["讨厌", "tǎoyàn"],
    "doubt": ["怀疑", "huáiyí"],
    "enthusiastic": ["热情", "rèqíng"],
    "calm": ["冷静", "lěngjìng"],
    "Sports": ["体育", "tǐyù"],
    "Soccer": ["足球", "zúqiú"],
    "Basketball": ["篮球", "lánqiú"],
    "Volleyball": ["排球", "páiqiú"],
    "Tennis": ["网球", "wǎngqiú"],
    "Table Tennis": ["乒乓球", "pīngpāngqiú"],
    "Badminton": ["羽毛球", "yǔmáoqiú"],
    "Baseball": ["棒球", "bàngqiú"],
    "Golf": ["高尔夫球", "gāo'ěrfūqiú"],
    "Swimming": ["游泳", "yóuyǒng"],
    "Running": ["跑步", "pǎobù"],
    "Long Jump": ["跳远", "tiàoyuǎn"],
    "High Jump": ["跳高", "tiàogāo"],
    "Weightlifting": ["举重", "jǔzhòng"],
    "Boxing": ["拳击", "quánjī"],
    "Wrestling": ["摔跤", "shuāijiāo"],
    "Ice Skating": ["滑冰", "huábīng"],
    "Skiing": ["滑雪", "huáxuě"],
    "Archery": ["射箭", "shèjiàn"],
    "Gymnastics": ["体操", "tǐcāo"],
    "Bicycle": ["自行车", "zìxíngchē"],
    "Marathon": ["马拉松", "mǎlāsōng"],
    "Racing": ["赛车", "sàichē"],
    "Race Walking": ["竞走", "jìngzǒu"],
    "Diving": ["跳水", "tiàoshuǐ"],
    "Shooting": ["射击", "shèjī"],
    "Surfing": ["冲浪", "chōnglàng"],
    "To Host (Event)": ["举办", "jǔbàn"],
    "Sports Meet": ["运动会", "yùndònghuì"],
    "Track and Field": ["田径", "tiánjìng"],
    "Referee": ["裁判", "cáipàn"],
    "Sports Team": ["球队", "qiúduì"],
    "Match": ["比赛", "bǐsài"],
    "Score a Goal": ["进球", "jìnqiú"],
    "Lose": ["输", "shū"],
    "Win": ["赢", "yíng"],
    "Draw (Tie)": ["平局", "píngjú"],
    "Endurance": ["耐力", "nàilì"],
    "Speed": ["速度", "sùdù"],
    "Warm-up": ["热身", "rèshēn"],
    "Stretch": ["拉伸", "lāshēn"],
    "Exercise": ["锻炼", "duànliàn"],
    "Training": ["训练", "xùnliàn"],
    "Champion": ["冠军", "guànjūn"],
    "Runner-up": ["亚军", "yàjūn"],
    "Third Place": ["季军", "jìjūn"],
    "Gold Medal": ["金牌", "jīnpái"],
    "Silver Medal": ["银牌", "yínpái"],
    "Bronze Medal": ["铜牌", "tóngpái"],
    "World Cup": ["世界杯", "shìjièbēi"],
    "Olympic Games": ["奥运会", "àoyùnhuì"],
    "Relay Race": ["接力赛", "jiēlìsài"],
    "Obstacle Race": ["障碍赛", "zhàng'àisài"],
    "Score": ["比分", "bǐfēn"],
    "Audience": ["观众", "guānzhòng"],
    "Overtime": ["加时赛", "jiāshísài"],
    "Penalty Kick": ["点球", "diǎnqiú"],
    "Red Card": ["红牌", "hóngpái"],
    "Yellow Card": ["黄牌", "huángpái"],
    "Sports Field": ["球场", "qiúchǎng"],
    "Big": ["大", "dà"],
    "Small": ["小", "xiǎo"],
    "Long": ["长", "cháng"],
    "Short": ["短", "duǎn"],
    "Tall / High": ["高", "gāo"],
    "Low": ["低", "dī"],
    "Wide": ["宽", "kuān"],
    "Narrow": ["狭窄", "xiázhǎi"],
    "Heavy": ["重", "zhòng"],
    "Light (weight)": ["轻", "qīng"],
    "Deep": ["深", "shēn"],
    "Shallow": ["浅", "qiǎn"],
    "Bright": ["亮", "liàng"],
    "Dark": ["暗", "àn"],
    "Clear": ["清晰", "qīngxī"],
    "Blurry": ["模糊", "móhú"],
    "Soft": ["软", "ruǎn"],
    "Hard": ["硬", "yìng"],
    "Thin": ["瘦", "shòu"],
    "Fat": ["胖", "pàng"],
    "Beautiful (female)": ["美丽", "měilì"],
    "Ugly": ["丑", "chǒu"],
    "Appearance": ["模样", "múyàng"],
    "Rough": ["粗糙", "cūcāo"],
    "Pretty": ["漂亮", "piàoliang"],
    "Cute": ["可爱", "kě'ài"],
    "Easy": ["容易", "róngyì"],
    "Difficult": ["难", "nán"],
    "Fast": ["快", "kuài"],
    "Slow": ["慢", "màn"],
    "Hot": ["热", "rè"],
    "Cold": ["冷", "lěng"],
    "Coarse": ["粗", "cū"],
    "Wet": ["湿", "shī"],
    "Dry": ["干", "gān"],
    "Straight": ["直", "zhí"],
    "Curved": ["弯", "wān"],
    "Flat": ["平坦", "píngtǎn"],
    "Slope": ["坡", "pō"],
    "Transparent": ["透明", "tòumíng"],
    "Fresh": ["新鲜", "xīnxiān"],
    "Bad Tasting": ["难吃", "nán chī"],
    "Fluent": ["流畅", "liúchàng"],
    "Healthy": ["健康", "jiànkāng"],
    "Smart": ["聪明", "cōngmíng"],
    "Fresh (feeling)": ["清新", "qīngxīn"],
    "Dirty": ["肮脏", "āngzāng"],
    "Safe": ["安全", "ānquán"],
    "Dangerous": ["危险", "wēixiǎn"],
    "Noble": ["高贵", "gāoguì"],
    "Stable": ["稳定", "wěndìng"],
    "Exquisite": ["精致", "jīngzhì"],
    "Strange": ["奇怪", "qíguài"],
    "Precise": ["精密", "jīngmì"],
    "Complex": ["复杂", "fùzá"],
    "Simple": ["简单", "jiǎndān"],
    "Noisy": ["喧闹", "xuānnào"],
    "Quiet": ["安静", "ānjìng"],
    "Handsome": ["英俊", "yīngjùn"],
    "Graceful": ["端庄", "duānzhuāng"],
    "Traditional": ["传统", "chuántǒng"],
    "Modern": ["现代", "xiàndài"],
    "Ordinary": ["平凡", "píngfán"],
    "Magnificent": ["壮丽", "zhuànglì"],
    "Wealthy": ["富有", "fùyǒu"],
    "Poor": ["贫穷", "pínqióng"],
    "Hazy": ["朦胧", "ménglóng"],
    "Bright and Clear": ["明朗", "mínglǎng"],
    "Strong": ["强壮", "qiángzhuàng"],
    "Weak": ["虚弱", "xūruò"],
    "China": ["中国", "Zhōngguó"],
    "Vietnam": ["越南", "Yuènán"],
    "Japan": ["日本", "Rìběn"],
    "South Korea": ["韩国", "Hánguó"],
    "North Korea": ["朝鲜", "Cháoxiǎn"],
    "Thailand": ["泰国", "Tàiguó"],
    "Laos": ["老挝", "Lǎowō"],
    "Cambodia": ["柬埔寨", "Jiǎnpǔzhài"],
    "Myanmar": ["缅甸", "Miǎndiàn"],
    "India": ["印度", "Yìndù"],
    "Malaysia": ["马来西亚", "Mǎláixīyà"],
    "Singapore": ["新加坡", "Xīnjiāpō"],
    "Indonesia": ["印度尼西亚", "Yìndùníxīyà"],
    "Philippines": ["菲律宾", "Fēilǜbīn"],
    "Australia": ["澳大利亚", "Àodàlìyà"],
    "New Zealand": ["新西兰", "Xīnxīlán"],
    "United States": ["美国", "Měiguó"],
    "Canada": ["加拿大", "Jiānádà"],
    "Mexico": ["墨西哥", "Mòxīgē"],
    "Brazil": ["巴西", "Bāxī"],
    "Argentina": ["阿根廷", "Āgēntíng"],
    "Chile": ["智利", "Zhìlì"],
    "Peru": ["秘鲁", "Bìlǔ"],
    "Colombia": ["哥伦比亚", "Gēlúnbǐyà"],
    "United Kingdom": ["英国", "Yīngguó"],
    "France": ["法国", "Fǎguó"],
    "Germany": ["德国", "Déguó"],
    "Italy": ["意大利", "Yìdàlì"],
    "Spain": ["西班牙", "Xībānyá"],
    "Portugal": ["葡萄牙", "Pútáoyá"],
    "Netherlands": ["荷兰", "Hélán"],
    "Switzerland": ["瑞士", "Ruìshì"],
    "Austria": ["奥地利", "Àodìlì"],
    "Belgium": ["比利时", "Bǐlìshí"],
    "Norway": ["挪威", "Nuówēi"],
    "Sweden": ["瑞典", "Ruìdiǎn"],
    "Finland": ["芬兰", "Fēnlán"],
    "Denmark": ["丹麦", "Dānmài"],
    "Greece": ["希腊", "Xīlà"],
    "Poland": ["波兰", "Bōlán"],
    "Czech Republic": ["捷克", "Jiékè"],
    "worHungaryd": ["匈牙利", "Xiōngyálì"],
    "Russia": ["俄罗斯", "Éluósī"],
    "Ukraine": ["乌克兰", "Wūkèlán"],
    "Turkey": ["土耳其", "Tǔ'ěrqí"],
    "Egypt": ["埃及", "Āijí"],
    "South Africa": ["南非", "Nánfēi"],
    "Morocco": ["摩洛哥", "Móluògē"],
    "Algeria": ["阿尔及利亚", "Ā'ěrjílìyà"],
    "Nigeria": ["尼日利亚", "Nírìlìyà"],
    "Dog": ["狗", "gǒu"],
    "Cat": ["猫", "māo"],
    "Bird": ["鸟", "niǎo"],
    "Fish": ["鱼", "yú"],
    "Horse": ["马", "mǎ"],
    "Cow": ["牛", "niú"],
    "Sheep": ["羊", "yáng"],
    "Chicken": ["鸡", "jī"],
    "Pig": ["猪", "zhū"],
    "Tiger": ["老虎", "lǎohǔ"],
    "Lion": ["狮子", "shīzi"],
    "Elephant": ["大象", "dàxiàng"],
    "Bear": ["熊", "xióng"],
    "Wolf": ["狼", "láng"],
    "Snake": ["蛇", "shé"],
    "Rabbit": ["兔子", "tùzi"],
    "Frog": ["青蛙", "qīngwā"],
    "Tortoise": ["乌龟", "wūguī"],
    "Duck": ["鸭子", "yāzi"],
    "Goose": ["鹅", "é"],
    "Monkey": ["猴子", "hóuzi"],
    "Squirrel": ["松鼠", "sōngshǔ"],
    "Python": ["蟒蛇", "mǎngshé"],
    "Owl": ["猫头鹰", "māotóuyīng"],
    "Dolphin": ["海豚", "hǎitún"],
    "Whale": ["鲸鱼", "jīngyú"],
    "Shark": ["鲨鱼", "shāyú"],
    "Octopus": ["章鱼", "zhāngyú"],
    "Crab": ["螃蟹", "pángxiè"],
    "Lobster": ["龙虾", "lóngxiā"],
    "Bee": ["蜜蜂", "mìfēng"],
    "Butterfly": ["蝴蝶", "húdié"],
    "Ant": ["蚂蚁", "mǎyǐ"],
    "Mosquito": ["蚊子", "wénzi"],
    "Fly": ["苍蝇", "cāngying"],
    "Cockroach": ["蟑螂", "zhāngláng"],
    "Hippopotamus": ["河马", "hémǎ"],
    "Rhinoceros": ["犀牛", "xīniú"],
    "Donkey": ["驴", "lǘ"],
    "Camel": ["骆驼", "luòtuo"],
    "Mouse": ["老鼠", "lǎoshǔ"],
    "Bat": ["蝙蝠", "biānfú"],
    "Spider": ["蜘蛛", "zhīzhū"],
    "Starfish": ["海星", "hǎixīng"],
    "Seahorse": ["海马", "hǎimǎ"],
    "Coral": ["珊瑚", "shānhú"],
    "Sea Turtle": ["海龟", "hǎiguī"],
    "Crane": ["鹤", "hè"],
    "Peacock": ["孔雀", "kǒngquè"],
    "Lizard": ["蜥蜴", "xīyì"],
    "Weather": ["天气", "tiānqì"],
    "Sunny day": ["晴天", "qíngtiān"],
    "Cloudy day": ["阴天", "yīntiān"],
    "Overcast": ["多云", "duōyún"],
    "Rain": ["雨", "yǔ"],
    "Air": ["空气", "kōngqì"],
    "Drought": ["干旱", "gānhàn"],
    "Thunderstorm": ["雷雨", "léiyǔ"],
    "Typhoon": ["台风", "táifēng"],
    "Wind": ["风", "fēng"],
    "Breeze": ["微风", "wēifēng"],
    "Strong wind": ["强风", "qiángfēng"],
    "Snow": ["雪", "xuě"],
    "Ocean": ["海洋", "hǎiyáng"],
    "Tropics": ["热带", "rèdài"],
    "Warm": ["暖和", "nuǎnhuo"],
    "Cold": ["寒冷", "hánlěng"],
    "Sun": ["太阳", "tàiyáng"],
    "Moon": ["月亮", "yuèliàng"],
    "Sky": ["天空", "pinytiānkōngin"],
    "Star": ["星", "xīng"],
    "Storm": ["风暴", "fēngbào"],
    "Lightning": ["闪电", "shǎndiàn"],
    "Thunder": ["雷声", "léishēng"],
    "Rainbow": ["彩虹", "cǎihóng"],
    "Fog": ["雾", "wù"],
    "Frost": ["霜", "shuāng"],
    "Lava": ["熔岩", "róngyán"],
    "Temperature": ["温度", "wēndù"],
    "Earthquake": ["地震", "dìzhèn"],
    "Climate": ["气候", "qìhòu"],
    "Aurora": ["极光", "jíguāng"],
    "Flood": ["洪水", "hóngshuǐ"],
    "Spring (season)": ["春天", "chūntiān"],
    "Summer": ["夏天", "xiàtiān"],
    "Autumn": ["秋天", "qiūtiān"],
    "Winter": ["冬天", "dōngtiān"],
    "Desert": ["沙漠", "shāmò"],
    "Grassland": ["草原", "cǎoyuán"],
    "Island": ["岛屿", "dǎoyǔ"],
    "House": ["房子", "fángzi"],
    "Home, family": ["家", "jiā"],
    "Living room": ["客厅", "kètīng"],
    "Bedroom": ["卧室", "wòshì"],
    "Kitchen": ["厨房", "chúfáng"],
    "Bathroom": ["浴室", "yùshì"],
    "Dining room": ["餐厅", "cāntīng"],
    "Study room": ["书房", "shūfáng"],
    "Balcony": ["阳台", "yángtái"],
    "Hallway": ["走廊", "zǒuláng"],
    "Door": ["门", "mén"],
    "Window": ["窗户", "chuānghù"],
    "Roof": ["屋顶", "wūdǐng"],
    "Floor": ["地板", "dìbǎn"],
    "Wall": ["墙", "qiáng"],
    "Carpet": ["地毯", "dìtǎn"],
    "Furniture": ["家具", "jiājù"],
    "Sofa": ["沙发", "shāfā"],
    "Chair": ["椅子", "yǐzi"],
    "Table": ["桌子", "zhuōzi"],
    "Bed": ["床", "chuáng"],
    "Wardrobe": ["衣柜", "yīguì"],
    "Dining table": ["餐桌", "cānzhuō"],
    "Coffee table": ["茶几", "chájī"],
    "TV": ["电视", "diànshì"],
    "Air conditioner": ["空调", "kōngtiáo"],
    "Fan": ["风扇", "fēngshàn"],
    "Refrigerator": ["冰箱", "bīngxiāng"],
    "Microwave": ["微波炉", "wēibōlú"],
    "Washing machine": ["洗衣机", "xǐyījī"],
    "Dishwasher": ["洗碗机", "xǐwǎnjī"],
    "Oven": ["烤箱", "kǎo xiāng"],
    "Electric stove": ["电炉", "diànlú"],
    "Gas stove": ["炉子", "lúzi"],
    "Sink": ["水槽", "shuǐcáo"],
    "Water heater": ["热水器", "rèshuǐqì"],
    "Toilet": ["厕所", "cè suǒ"],
    "Bathtub": ["浴缸", "yùgāng"],
    "Toilet bowl": ["马桶", "mǎtǒng"],
    "Washbasin": ["洗手池", "xǐshǒuchí"],
    "Mirror": ["镜子", "jìngzi"],
    "Towel": ["毛巾", "máojīn"],
    "Toothbrush": ["牙刷", "yáshuā"],
    "Toothpaste": ["牙膏", "yágāo"],
    "Soap": ["香皂", "xiāngzào"],
    "Toilet paper": ["手纸", "shǒuzhǐ"],
    "Shampoo": ["洗发水", "xǐfàshuǐ"],
    "Body wash": ["沐浴露", "mùyùlù"],
    "Hugging pillow": ["抱枕", "bàozhěn"],
    "Blanket": ["被子", "bèizi"],
    "Bedsheet": ["床单", "chuángdān"],
    "Pillow": ["枕头", "zhěntou"],
    "TV remote": ["电视遥控器", "diànshì yáokòngqì"],
    "Telephone": ["电话", "diànhuà"],
    "Bookshelf": ["书架", "shūjià"],
    "Lamp": ["灯", "dēng"],
    "Camera": ["照相机", "zhàoxiàngjī"],
    "Computer": ["电脑", "diànnǎo"],
    "Book": ["书", "shū"],
    "Cup": ["杯子", "bēizi"],
    "Bowl": ["碗", "wǎn"],
    "Plate": ["盘子", "pánzi"],
    "Knife": ["刀子", "dāozi"],
    "Spoon": ["勺子", "sháozi"],
    "Fork": ["叉子", "chāzi"],
    "Pot": ["锅", "guō"],
    "Tissue, napkin": ["纸巾", "zhǐjīn"],
    "Comb": ["梳子", "shūzi"],
    "Iron": ["熨斗", "yùndǒu"],
    "Trash bin": ["垃圾桶", "lājītǒng"],
    "Clothes": ["衣服", "yīfú"],
    "Shirt": ["衬衫", "chènshān"],
    "T-shirt": ["T恤", "T-xù"],
    "Skirt": ["裙子", "qúnzi"],
    "Pants": ["裤子", "kùzi"],
    "Coat": ["外套", "wàitào"],
    "Down jacket": ["羽绒服", "yǔróngfú"],
    "Dress": ["连衣裙", "liányīqún"],
    "Suit": ["西装", "xīzhuāng"],
    "Outfit": ["套装", "tàozhuāng"],
    "Jeans": ["牛仔裤", "niúzǎikù"],
    "Sneakers": ["运动鞋", "yùndòngxié"],
    "Leather shoes": ["皮鞋", "píxié"],
    "Boots": ["靴子", "xuēzi"],
    "Slippers/Sandals": ["拖鞋", "tuōxié"],
    "Hat": ["帽子", "màozi"],
    "Scarf": ["围巾", "wéijīn"],
    "Gloves": ["手套", "shǒutào"],
    "Socks": ["袜子", "wàzi"],
    "Underwear": ["内衣", "nèiyī"],
    "Bra": ["胸罩", "xiōngzhào"],
    "Underpants": ["内裤", "nèikù"],
    "Pajamas": ["睡衣", "shuìyī"],
    "Sleep pants": ["睡裤", "shuìkù"],
    "Tank top": ["背心", "bèixīn"],
    "Windbreaker": ["夹克", "jiákè"],
    "Sweatpants": ["运动裤", "yùndòng kù"],
    "Swimsuit": ["游泳衣", "yóuyǒng yī"],
    "Bathrobe": ["睡袍", "shuìpáo"],
    "Denim jacket": ["牛仔外套", "niúzǎi wàitào"],
}
hindi_word_bank = {
    "Hello": "नमस्ते",
    "Goodbye": "अलविदा",
    "Please": "कृपया",
    "Thank you": "धन्यवाद",
    "Yes": "हाँ",
    "No": "नहीं",
    "Excuse me": "माफ़ कीजिए",
    "Sorry": "माफ़ करना"
}
french_word_bank = {
    "Eat": "Bouffer",
    "Flirt" : "Draguer",
    "Steal" : "Piquer",
    "Guy" : "Mec",
    "Chick" : "Meuf",
    "Money" : "Blé",
    "Book" : "Bouquin",
    "Bro/sis" : "Frangin(e)",
    "Car" : "Bagnole",
    "Clothes" : "Fringes",
    "Drink alcohol" : "Picoler",
    "Police" : "Flic",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot",
    "word" : "argot"
}
hebrew_word_bank = {
    "Hello": "שלום",
    "Goodbye": "להתראות",
    "Please": "אָנָא",
    "Thank you": "תודה לך",
    "You're welcome": "אתה מוזמן",
}
spanish_word_bank = {
    "Hello": "Hola",
    "Good morning": "Buenos días",
    "Good afternoon": "Buenas tardes",
    "Good night": "Buenas noches",
    "Goodbye": "Adiós",
    "Please": "Por favor",
    "Thank you": "Gracias",
    "You're welcome": "De nada",
    "Excuse me": "Perdón"
}
tamil_word_bank = {
    "Hello": "வணக்கம்",
    "Thank you": "நன்றி",
    "How are you?": "எப்படி இருக்கீங்க ?",
    "Excuse me/ sorry": "மன்னிக்கவும்",
    "Are you happy?": "சந்தோஷமா?",
    "I'll be back": "போயிட்டு வர்றேன்",
    "Goodmorning": "காலை வணக்கம்",
    "Good evening": "மாலை வணக்கம்",
    "Good night": "இரவுக்கு வணக்கம்",
    "Mom": "அம்மா",
    "Dad": "அப்பா",
    "Older brother": "அண்ணன்",
    "Older sister": "அக்கா",
    "Younger brother": "தம்பி",
    "Younger sister": "தங்கை",
    "Grandma": "பாட்டி",
    "Grandpa": "தாத்தா",
    "maternal uncle": "மாமா",
    "paternal aunt": "அத்தை",
    "House": "வீடு",
    "Shop": "கடை",
    "Food": "சாப்பாடு",
    "Water": "தண்ணி",
    "Clothes": "உடை",
    "Book": "புத்தகம்",
    "Food": "சாப்பாடு",
    "Meat/ curry": "கறி",
    "lentil soup (sambar)": "சாம்பார்"

}
japanese_word_bank = {
    "Yes": "はい",
    "No": "いいえ",
    "Friend": "友達",
    "Dad": "お父さん",
    "Mom": "お母さん",
    "Water": "水"
}
korean_word_bank = {
    "Hello": "안녕하세요",
    "Please": "주세요",
    "Sorry": "죄송합니다",
    "Thank you": "고맙습니다",
    "Yes": "네",
    "No": "아니요",
    "I don't know": "모르겠어요"

}
german_word_bank = {
    "Hello": "Hallo",
    "Good morning": "Guten Morgen",
    "Good evening": "Guten Abend",
    "Goodbye": "Auf Wiedersehen",
    "Excuse me": "Entschuldigung",
    "You're welcome": "Gern geschehen",
    "How are you?": "Wie geht es Ihnen?",
    "I am fine": "Mir geht es gut",
    "Where is the bathroom?": "Wo ist die Toilette?",
    "How much does this cost?": "Wie viel kostet das?",
    "Help!": "Hilfe!"
}
swedish_word_bank = {
    "Hello": "Hej",
    "Good morning": "God morgon",
    "Good night": "God natt",
    "Goodbye": "Hej då",
    "Please": "Snälla",
    "Thank you": "Tack",
    "You're welcome": "Varsågod",
    "Excuse me": "Ursäkta",
    "How are you?": "Hur mår du?",
    "I don't understand": "Jag förstår inte",
    "See you later": "Vi ses senare"
}
russian_word_bank = {
    "Hello": "привет",
    "bye": "пока",
    "language": "язык",
    "morning": "утро"
}
sinhala_word_bank = {
    "Hello": "ආයුබෝවන්",
    "bye": "සමුගන්නවා",
    "language": "භාෂාව",
    "morning": "උදෑසන"
}
latin_word_bank = {
    "Hello": "salve",
    "bye": "vale",
    "language": "lingua",
    "morning": "mane"
}
greek_word_bank = {
    "Hello": "Γειά σου",
    "bye": "αντίο",
    "language": "γλώσσα",
    "morning": "πρωί"
}
arabic_word_bank = {
    "Hello": "مرحبًا",
    "bye": "الوداع",
    "language": "لغة",
    "morning": "صباح"
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
language_list = ["Chinese", "Hindi", "French", "Hebrew", "Spanish", "Tamil", "Japanese", "Korean", "German", "Swedish", "Russian", "Sinhala", "Latin", "Greek", "Arabic"]


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
    font_sinhala = pygame.font.Font("NotoSansSinhala-VariableFont_wdth.ttf", 25)
    font_arabic = pygame.font.Font("NotoSansArabic-VariableFont_wdth.ttf", 25)
except pygame.error as e:
    print(f"Warning: Missing language fonts - {e}")
    font_chinese = font_hindi = font_hebrew = font_tamil = font_japanese = font_korean = font_sinhala = font_arabic = pygame.font.SysFont("arial", 25)


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
        elif language == "Russian":
            english_word = random.choice(list(russian_word_bank.keys()))
            correct_translation = russian_word_bank[english_word]
        elif language == "Sinhala":
            english_word = random.choice(list(sinhala_word_bank.keys()))
            correct_translation = sinhala_word_bank[english_word]
        elif language == "Latin":
            english_word = random.choice(list(latin_word_bank.keys()))
            correct_translation = latin_word_bank[english_word]
        elif language == "Greek":
            english_word = random.choice(list(greek_word_bank.keys()))
            correct_translation = greek_word_bank[english_word]
        elif language == "Arabic":
            english_word = random.choice(list(arabic_word_bank.keys()))
            correct_translation = arabic_word_bank[english_word]
        
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
        elif language == "Russian":
            random_word = random.choice(list(russian_word_bank.keys()))
            wrong_translation = russian_word_bank[random_word]
        elif language == "Sinhala":
            random_word = random.choice(list(sinhala_word_bank.keys()))
            wrong_translation = sinhala_word_bank[random_word]
        elif language == "Latin":
            random_word = random.choice(list(latin_word_bank.keys()))
            wrong_translation = latin_word_bank[random_word]
        elif language == "Greek":
            random_word = random.choice(list(greek_word_bank.keys()))
            wrong_translation = greek_word_bank[random_word]
        elif language == "Arabic":
            random_word = random.choice(list(arabic_word_bank.keys()))
            wrong_translation = arabic_word_bank[random_word]
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
    elif language == "Sinhala":
        return font_sinhala
    elif language == "Arabic":
        return font_arabic
    else:
        return font_latin



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


sad_song_files = ["meow.wav", "rickroll_proper.wav", "communism.wav", "orphans.wav", "loser.wav"]

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
russian_rect = pygame.Rect(400, 530, 120, 50)
sinhala_rect = pygame.Rect(530, 410, 120, 50)
latin_rect = pygame.Rect(530, 470, 120, 50)
greek_rect = pygame.Rect(530, 530, 120, 50)
arabic_rect = pygame.Rect(660, 410, 120, 50)

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
                elif russian_rect.collidepoint(event.pos):
                    if "Russian" not in languages:
                        languages.append("Russian")
                        print(languages)
                    else:
                        languages.remove("Russian")
                        print(languages)
                elif sinhala_rect.collidepoint(event.pos):
                    if "Sinhala" not in languages:
                        languages.append("Sinhala")
                        print(languages)
                    else:
                        languages.remove("Sinhala")
                        print(languages)
                elif latin_rect.collidepoint(event.pos):
                    if "Latin" not in languages:
                        languages.append("Latin")
                        print(languages)
                    else:
                        languages.remove("Latin")
                        print(languages)
                elif greek_rect.collidepoint(event.pos):
                    if "Greek" not in languages:
                        languages.append("Greek")
                        print(languages)
                    else:
                        languages.remove("Greek")
                        print(languages)
                elif arabic_rect.collidepoint(event.pos):
                    if "Arabic" not in languages:
                        languages.append("Arabic")
                        print(languages)
                    else:
                        languages.remove("Arabic")
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

        if "Russian" in languages:
            russian_colour = (25, 25, 25)
        elif russian_rect.collidepoint(mouse_pos):
            russian_colour = (180, 0, 180)
        else: 
            russian_colour = PURPLE
        draw_button(screen, russian_rect, "Russian", button_font, russian_colour, WHITE)

        if "Sinhala" in languages:
            sinhala_colour = (25, 25, 25)
        elif sinhala_rect.collidepoint(mouse_pos):
            sinhala_colour = (180, 0, 180)
        else: 
            sinhala_colour = PURPLE
        draw_button(screen, sinhala_rect, "Sinhala", button_font, sinhala_colour, WHITE)

        if "Latin" in languages:
            latin_colour = (25, 25, 25)
        elif latin_rect.collidepoint(mouse_pos):
            latin_colour = (180, 0, 180)
        else: 
            latin_colour = PURPLE
        draw_button(screen, latin_rect, "Latin", button_font, latin_colour, WHITE)

        if "Greek" in languages:
            greek_colour = (25, 25, 25)
        elif greek_rect.collidepoint(mouse_pos):
            greek_colour = (180, 0, 180)
        else: 
            greek_colour = PURPLE
        draw_button(screen, greek_rect, "Greek", button_font, greek_colour, WHITE)

        if "Arabic" in languages:
            arabic_colour = (25, 25, 25)
        elif arabic_rect.collidepoint(mouse_pos):
            arabic_colour = (180, 0, 180)
        else: 
            arabic_colour = PURPLE
        draw_button(screen, arabic_rect, "Arabic", button_font, arabic_colour, WHITE)

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
