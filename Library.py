roomname = 'Библиотека'

description = (
    'Пройдя в зал библиотеки и оглядевшись на первый взгляд вы никого здесь не замечаете, но ваш взгляд отделяет от стены, сидящую в дальнем углу фигуру в сером балахоне, которая скрюченно сидит над каким-то фолиантом.')

person = (
    'Глава гильдии мастер Торхилд – А, Добро пожаловать! Как вы уже наверняка знаете, в городе Размиран произошла большая беда. Бесследно исчез Винздор - лорд-протектор города. Никто не видел его с минувшей среды, а когда хватились и начали поиски, сложилось такое чувство, что лорд просто провалился сквозь землю. Абсолютно всем кажется, что дело тут нечисто, городская стража исчерпала свои ресурсы и казна готова платить любому за помощь в поисках лорда. Вы можете посещать любые места, связанные с лордом, если вам поможет это в поисках. Несколько людей выдели его последними: это его невеста баронесса Элания, Ученик Ри и преданный слуга Логен.')


def dialog():
    reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Где я могу найти их?')]])

    where = 'Где я могу найти их?'

    if where == 'Где я могу найти их?':
        print(
            'Глава гильдии мастер Торхилд – Леди Элания, сегодня должна была устраивать праздник в честь помолвки с лордом в своем имении, недалеко от центральное площади. Бедная девочка.. Логена, думаю проще всего найти в таверне «Кровавый кабан», она находится непосредственно на площади. После того как его благородный хозяин пропал, бедняга сел на стакан. Ученика я сам давненько не видел, однако.. Возможно стоит начать с библиотеки. Городок у нас совсем небольшой, вы не заблудитесь. А теперь, я так понимаю главная часть нашего договора. Вознаграждение. 100 золотых за то, что вы вернете покой жителям города Размиран и найдет лорда. 50 сейчас, остальное после завершения вашей работы.')


def ok():
    reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='По рукам')]])

    where = 'По рукам'

    if where == 'По рукам':
        print(
            '*Увесистый кошель падает на стол.* Глава гильдии мастер Торхилд – Чтож, мне необходимо приступить к обязанностям возложенным на меня в отсутствие лорда. Да помогут Вам Боги! Вы оглядываете приемную и замечаете две двери, помимо той которая привела вас сюда.')