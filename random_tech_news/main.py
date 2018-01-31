import feedparser
import random
import time
import telepot
from telepot.loop import MessageLoop

from config import settings

TOKEN = settings.BOT_TOKEN


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    feed = feedparser.parse(settings.NEWS_RSS)
    entry_number = random.randint(0, 19)
    news_link = feed['entries'][entry_number]
    message = "[{}]({})".format(news_link['title'], news_link['link'])
    if msg['text'].lower() == "boring":
        bot.sendMessage(chat_id, message)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
