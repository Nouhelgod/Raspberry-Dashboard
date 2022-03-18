# Third-party modules
import telebot

# Local modules
from lib import lib_json_wrapper as jsr
from lib.lib_telebot_language import language_controller as locale


def generic_yn(lang: str, callback_key: str):
    """Generic yes / no.

    Args:
        lang (str): language
        callback_key (str): special keyword to parse callback

    Returns:
        telebot.types.InlineKeyboardMarkup: [yes][no].
    """
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


def select_language(lang: str, settings_file: str):
    """Generic language list

    Args:
        lang (str): Language
        settings_file (str): path to json file with 'app.languages' object

    Returns:
        telebot.types.InlineKeyboardMarkup: [English][Russian][And][So][On]
    """
    markup = telebot.types.InlineKeyboardMarkup()    
    language_list = jsr.read(settings_file, 'app.languages')
    
    for language in language_list:
        markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, f'button.select_language.{language}'),
        callback_data=f'set_language.{language}'
    ))
    
    
    return markup


def start_message(lang: str):
    """Keyboard of default (start) message

    Args:
        lang (str): Language

    Returns:
        telebot.types.InlineKeyboardMarkup: [Bot config][RPi config][About]
    """
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


# FIXME: RENAME. Might be useful in other cases.
def about(lang: str):
    """Keyboard of about section.

    Args:
        lang (str): Language

    Returns:
        telebot.types.InlineKeyboardMarkup: [Back]
    """
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, 'button.back'),
        callback_data='about.back'
    ))

    return markup


def generic_list(lang: str, options_list: list, callback_key: str, **kwargs):
    """Generic list keyboard. Optional keyword arguments: stop (bool), start (bool).

    Args:
        lang (str): Language
        options_list (list): List of options. Using lib_telebot_settings_wrapper is highly recommended.
        callback_key (str): special keyword to parse callback

    Returns:
        telebot.types.InlineKeyboardMarkup: [1][2]...[len(options_list)] [Stop]*[Start]*
        *optional
    """
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


def rpi_config(lang: str, start: bool=True):
    """RPi config keyboard.

    Args:
        lang (str): Language
        start (bool, optional): Add [Start] if True. Defaults to True.

    Returns:
        telebot.types.InlineKeyboardMarkup: [Components list][Autorun config][Active components]
    """
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


def start(lang: str):
    """Just start button.

    Args:
        lang (str): Language

    Returns:
        telebot.types.InlineKeyboardMarkup: [Start]
    """
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(
        text = locale.get_line(lang, "button.start"),
        callback_data=f'start!'
    ))
    
    return markup