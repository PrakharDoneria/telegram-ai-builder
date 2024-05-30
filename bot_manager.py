from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from g4f.client import Client

client = Client()

class BotManager:
    def __init__(self):
        self.bots = {}

    def start_bot(self, token: str):
        if token in self.bots:
            return self.bots[token]

        updater = Updater(token, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CommandHandler("ai", self.ai))
        dispatcher.add_handler(CommandHandler("img", self.img))

        updater.start_polling()

        self.bots[token] = updater
        return updater

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("Hello! I'm your bot originally made and owned by @codewithprakhar .")

    def ai(self, update: Update, context: CallbackContext):
        text = ' '.join(context.args)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": text}]
        )
        ai_response = response.choices[0].message.content
        update.message.reply_text(ai_response)

    def img(self, update: Update, context: CallbackContext):
        prompt = ' '.join(context.args)
        response = client.images.generate(
            model="gemini",
            prompt=prompt,
        )
        image_url = response.data[0].url
        update.message.reply_photo(image_url)

    def stop_bot(self, token: str):
        if token in self.bots:
            self.bots[token].stop()
            del self.bots[token]

bot_manager = BotManager()
