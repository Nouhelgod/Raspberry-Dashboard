# Third-party modules
import telebot

# Local modules
from lib import lib_json_wrapper as jsr
from lib.lib_telebot_language import language_controller as locale


def generic_yn(lang, callback_key):
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.confirm_stop.positive'),
        callback_data=f'set:{callback_key}:positive'
    ))
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.confirm_stop.negative'),
        callback_data=f'set:{callback_key}:negative'
    ))
    
    return markup


def select_language(lang, settings_file):
    markup = telebot.types.InlineKeyboardMarkup()    
    language_list = jsr.read(settings_file, 'app.languages')
    
    for language in language_list:
        markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, f'button.select_language.{language}'),
        callback_data=f'set_language.{language}'
    ))
    
    
    return markup


def start_message(lang):
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.start_message.settings_bot'),
        callback_data='config.bot'
    ))
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.start_message.settings_rpi'),
        callback_data='config.rpi'
    ))
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.start_message.about'),
        callback_data='start_message.about'
    ))
    
    return markup


def about(lang):
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.back'),
        callback_data='about.back'
    ))

    return markup


def generic_list(lang, options_list, callback_key, start=False):
    markup = telebot.types.InlineKeyboardMarkup()
    
    for num in range(len(options_list)):
        markup.add(telebot.types.InlineKeyboardButton(
        text = str(num + 1),
        callback_data=f'{callback_key}:{options_list[num][0]}:{options_list[num][1]}'
    ))
        
    if start:
        markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, "button.start"),
        callback_data=f'start!'
    ))
        
    return markup