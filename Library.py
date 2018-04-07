from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

roomname = 'Библиотека'

def description():
    return """Пройдя в зал библиотеки и оглядевшись на первый взгляд вы никого здесь не замечаете, но ваш взгляд 
    		отделяет от стены, сидящую в дальнем углу фигуру в сером балахоне, которая скрюченно сидит над каким-то 
    		фолиантом."""

def initiate():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Подойти к человеку")]])
	return keyboard

def dialog_start():
    return """Подойдя к человеку в сером, вы разглядываете его лицо: это уставшее лицо молодого человека с легкой 
		   		порослью на щеках и давно не мытыми волосам, которые свисают из-под капюшона. Он поднимаете на вас 
		   		затравленный взгляд. К-к-к-кто в-вы? П-п-первый раз вижу!"""

def dialog_answer_buttons_1():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Я расследую исчезновение лорда. А ты случайно не Ри?")]])
	return keyboard

def dialog_1():
	return """Ученик Ри: Д-да. Все в-в-верно. Но в-в-вот толь-к-ко лорда я не видел еще с прошлой среды. И все что знал
		   		уже рассказал страже. *Вы замечаете, как Он ежится и отводит взгляд*"""

def dialog_answer_buttons_2():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Эти байки для стражи можешь и оставить, а мне 
																  расскажи-ка лучше про это *кладете перед ним книгу 
																  в черной обложке*""")]])
	return keyboard

def dialog_2():
	return """Глаза парня округляются, он берет книгу трясущимся руками и поднимает на вас взгляд. Ученик Ри: Значит 
		   вы тоже поняли, что это как-то связано! Надеюсь вы не доложили об этом? *хватается руками за голову*
		   Наш герой! Лорд-защитник, занимающийся некромантией!! Представляете какую тень это бросает на его имя??"""

def dialog_answer_buttons_3():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Тише-тише, я даже не понимаю, что здесь написано.")]])
	return keyboard

def dialog_end():
	return """Ученик Ри: хорошо-хорошо.. я сам искал эту книгу.. в ней должны быть ответы, где искать лорда, но мне 
		   потребуется время, чтобы перевести некоторые страницы… Выясните пока у остальных, возможно лорд, говорил 
		   им о каких-то местах.. возможно они что-то знают. Встречаемся на площади через 3 часа! И да помогут нам 
		   всем Боги! *Он начинает хаотично бегать между полок, бормоча и ища, что-то одному ему известное*"""

def dialog_end_buttons():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Хм.. ну ладно")]])
	return keyboard

def end_room():
	return 'Вы сразу же выходите из приемной в башне лорда и попадаете на главную торговую площадь города. Надо ' \
		   'сказать, что торговля идет не бойко и несмотря на середину дня, площадь выглядит пустой.'

def end_room_buttons():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Здесь же расположена таверна «Кровавый кабан» ")],
											 [KeyboardButton(text="""Поднявщись немного вверх по улице вы попадете в 
											 						имение	Баронессы Элании""")]])
	return keyboard