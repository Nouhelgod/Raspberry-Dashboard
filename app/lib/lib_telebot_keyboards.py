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


def generic_list(lang, options_list, callback_key, **kwargs):
    markup = telebot.types.InlineKeyboardMarkup()
    
    for num in range(len(options_list)):
        markup.add(telebot.types.InlineKeyboardButton(
            text = str(num + 1),
            callback_data=f'{callback_key}:{options_list[num][0]}:{options_list[num][1]}'
        ))
    
    for key, value in kwargs.items():           
        if key == 'stop' and value == True:
            markup.add(telebot.types.InlineKeyboardButton(
                text = locale.get_line(lang, "button.stop"),
                callback_data=f'stop!'
            ))
            
        if key == 'start' and value == True:
            markup.add(telebot.types.InlineKeyboardButton(
                text = locale.get_line(lang, "button.start"),
                callback_data=f'start!'
            ))
        
    return markup


def rpi_config(lang, start=True):
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
               text = locale.get_line(lang, 'button.config_rpi.components'),
               callback_data='conf_rpi.components!'
               ))
    
    markup.add(telebot.types.InlineKeyboardButton(
               text = locale.get_line(lang, 'button.config_rpi.components_autorun'),
               callback_data='conf_rpi.components_autorun'
               ))
    
    markup.add(telebot.types.InlineKeyboardButton(
               text = locale.get_line(lang, 'button.config_rpi.components_running'),
               callback_data='conf_rpi.components_running'
               ))
    
    if start:
        markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, "button.start"),
        callback_data=f'start!'
    ))
    
    return markup


def start(lang):
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, "button.start"),
        callback_data=f'start!'
    ))
    
    return markup