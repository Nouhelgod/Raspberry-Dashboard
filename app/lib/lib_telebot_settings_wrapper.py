# Local modules
from lib import lib_json_wrapper as jsr
from lib.lib_telebot_language import language_controller as locale


def add_option(LANG, options_list, key, value, type='list'):
    """Add option in option list.

    Args:
        options_list (list): options list
        key (str): target option key
        value (str): target option value
        type (str): type of value (list, bool) 

    Returns:
        list: options list
    """
    if type == 'bool':
        button_tag = get_button_tag_bool(LANG, 'app_settings.json', value)
        
    if type == 'language':
        button_tag = get_button_tag_language(LANG, 'app_settings.json', 'telebot.loc.language')
        
    options_list.append([key, value, locale.get_line(LANG, key), button_tag])
    
    return options_list
    
    
def get_button_tag_language(LANG, filepath, key):
    language_code = jsr.read(filepath, key)
    
    return locale.get_line(language_code, f'button.select_language.{language_code}')
    
    
    
def get_button_tag_bool(LANG, filepath, key):
    if jsr.read(filepath, key) == 'true':
        return locale.get_line(LANG, 'button.settings.true')
    else:
        return locale.get_line(LANG, 'button.settings.false')