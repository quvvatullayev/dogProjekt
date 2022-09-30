from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,InlineQueryHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import requests

class Dok:
    def __init__(self) -> None:
        self.ip = 'https://random.dog/'

    def start(self, update:Update, context:CallbackContext):
        id = update.message.chat.id
        uz = 'uz'
        ru = 'ru'
        en = 'en'
        keyboard = [[InlineKeyboardButton('O\'Z 🇺🇿', callback_data=f'🟢{uz}'), InlineKeyboardButton('RU 🇷🇺', callback_data=f'🟢{ru}'),InlineKeyboardButton('EN 🇬🇧', callback_data=f'🟢{en}')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        updater.bot.sendMessage(id, 'Assalomu alaykum bizning botga hush kelibsiz!')
        updater.bot.sendMessage(id, 'O\'zingizga qulay tilni tanlang!', reply_markup=reply_markup)
    
    def quere_start(self, update:Update, context:CallbackContext):
        query = update.callback_query
        data = query.data[1:]
        id = query.from_user.id
        query.edit_message_reply_markup(reply_markup=None)
        if data == 'en':
            reply_markup  = ReplyKeyboardMarkup([[KeyboardButton('picture')]], resize_keyboard=True)
            updater.bot.sendMessage(id, 'take a picture', reply_markup=reply_markup)
        elif data == 'ru':
            reply_markup  = ReplyKeyboardMarkup([[KeyboardButton('картина')]], resize_keyboard=True)
            updater.bot.sendMessage(id, 'сделать фото', reply_markup=reply_markup)
        elif data == 'uz':
            reply_markup  = ReplyKeyboardMarkup([[KeyboardButton('rasim')]], resize_keyboard=True)
            updater.bot.sendMessage(id, 'rasim chiqarish', reply_markup=reply_markup)

    def dok(self, update:Update, context:CallbackContext):
        id = update.message.chat.id
        url = requests.get('https://random.dog/woof.json')
        r = url.json()
        imeg = r['url']
        updater.bot.sendPhoto(id,imeg)

dok = Dok()

updater = Updater('5100473241:AAHvJxj6Ccvn3mL8Xivvdqj6nOyV-n_xSk4')
updater.dispatcher.add_handler(CommandHandler('start', dok.start))
updater.dispatcher.add_handler(CallbackQueryHandler(dok.quere_start, pattern='🟢'))
updater.dispatcher.add_handler(MessageHandler(Filters.text, dok.dok))

updater.start_polling()
updater.idle()
