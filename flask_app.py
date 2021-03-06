from flask import Flask, request
import telepot
import urllib3
import interface
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "8075c1e3-d76a-4148-b316-c066010911f5"
bot = telepot.Bot('575838275:AAEXJ3laI0GqwP5CHeTc9x_ifydI4d6ZL0M')
bot.setWebhook("https://SamolevarKilusov.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if text.lower() == "Start".lower() or text.lower() == "/Start".lower() or text.lower() == "Вы умерли... Начать сначала".lower() or text.lower() == "Ну, дальше будет дальше, а пока с победой! Начинай с начала!".lower() or text.lower() == "Вы спились, начать сначала... Ик".lower() :
            bot.sendMessage(chat_id, "Вы начинаете ваше путешествие перед башней", reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Войти в башню")]]))
        else:
            bot.sendMessage(chat_id, "%s" % interface.game(text), reply_markup = interface.keyboard(text))
    return "OK"