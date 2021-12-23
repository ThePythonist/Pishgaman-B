from flask import Flask, request
from mtranslate import translate
import telepot
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "BOT"
bot = telepot.Bot('5061978891:AAFXYC0G3vjeyNKqVsccMrR4x4KpWUxTqSY')
bot.setWebhook("https://thepythonist.pythonanywhere.com/{}".format(secret), max_connections=1)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    message = msg["text"]

    if content_type == 'text':

        if message == "/start" :
            bot.sendMessage(chat_id, "Hello i am Pishgaman Bot ! 😊")

        else :
            output = translate(message,"fa","en")
            bot.sendMessage(chat_id, output)


app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update["message"])
    return "OK"
