from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

roomname = 'Кабинет лорда'


def description():
    return 'Вы поднимаетесь по узкой винтовой лестнице и упираетесь в охранника преграждающего вам путь к двери в комнату. Крупный мужчина в форме городской стражи и с алебардой в руках. Охранник: Кто идет, чаво нать?'

def dialog_answer_buttons_1():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Я расследую пропажу лорда Винздора *показываете ему бумагу от мастера Торхилда*")]])
    return keyboard

def dialog_1():
    return 'Охранник: А, ну так бы сразу. Интересной чавой-та ты там сможешь отыскать, чего не нашли наши. Он отходит в сторону и вы, пройдя через довольно низкий дверной проем, вам даже пришлось пригнуться, чтобы не удариться головой, оказываетесь в небольшом помещении. Обстановка довольно простая, здесь совсем нет лишней мебели, перед вами стоит массивный стол и справа от вас шкаф с книгами.'

def find_1():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Осмотреть стол')], [KeyboardButton(text='Осмотреть книжный шкаф')]])
    return keyboard

def result_find_1():
    return 'Вы осматриваете стол: На столе нет ни бумаг, ни чего-то другого, что могло привлечь ваш взгляд, кроме портера молодой женщины с подписью «с любовью от Элании». Кажется, на самой поверхности все уже было осмотрено до вас.'

def find_2():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Осмотреть внимательно')], [KeyboardButton(text='Перейти к изучению шкафа')]])
    return keyboard

def result_find_2():
    return 'Осматривая внимательно стол: Вы простукиваете боковую стенку и вам кажется, что там, что-то скрыто. Вы отодвигаете одну из панелей стенки и находите там амулет в виде когтя, от него слегка веет магией.'

def find_3():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Надеть амулет')], [KeyboardButton(text='Спрятать амулет в карман и перейти к шкафу')]])
    return keyboard

def result_find_3():
    return 'Вы осматривайте шкаф: Здесь полно книг о стихийной магии и истории страны, все они выглядят примерно одинаково, но одна книга кажется вам тут неуместной. Это потрёпанный томик в черной коже, на обложке нет никаких надписей, которые давали бы вам понять, о чем эта книга. Внутри она и вовсе выглядит как записная книжка, со странными надписями, на незнакомом вам языке и странных рисунках и символах.'

def find_4():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Положить книгу в карман и выйти из кабинета')]])
    return keyboard

def end_room():
    return 'Вы проходите мимо ошарашенного стражника, который как вы заметили с любопытством поглядывал на ваши действия в кабинете и, спустившись в приемную вновь оказываетесь перед дверьми.'

def end_room_buttons():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="В библиотеку")], [KeyboardButton(text="На площадь ")]])
    return keyboard