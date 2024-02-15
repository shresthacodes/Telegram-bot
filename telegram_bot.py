
import telebot
import wikipedia

from api_key import api_key


bot = telebot.Telebot(api_key)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Ask me anything, I wikipedia it")


@bot.message_handler()
def send_reply(message):
    reply = "info not found"
    try:
        reply = wikipedia.summary(message.text)
    except Exception:
        pass
    finally:
        bot.reply_to(message, reply)


print("Loading...")
bot.infinity_polling()
print("Stopped")
