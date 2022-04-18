# Local modules
from lib import lib_json_wrapper as jsr
from lib.lib_telebot_language import language_controller as locale

#FIXME: remove type. Use type(value) instead.
def add_option(LANG: str, options_list: list, key: str, value: any, type: str='list'):
    """Add option in option list.

    Args:
        options_list (list): options list
        key (str): target option key
        value (any): target option value
        type (str): type of value (list, bool) 

    Returns:
        list: options list.
    """
    if type == 'bool':
        button_tag = get_button_tag_bool(LANG, 'app_settings.json', value)
        
    if type == 'language':
        button_tag = get_button_tag_language(LANG, 'app_settings.json', 'tele_bot.loc.language')
        
    options_list.append([key, value, locale.get_line(LANG, key), button_tag])
    
    return options_list
    

#FIXME: Docstring.   
def get_button_tag_language(LANG: str, filepath: str, key: str):
    """Get language code of tag.

    Args:
        LANG (str): Language
        filepath (str): path to json file  
        key (str): I guess it is language or tag. I forgot 🤔

    Returns:
        _type_: _description_
    """
    language_code = jsr.read(filepath, key)
    
    return locale.get_line(language_code, f'button.select_language.{language_code}')
    

#FIXME: Docstring. Same issue. 
def get_button_tag_bool(LANG, filepath, key):
    if jsr.read(filepath, key) == 'true':
        return locale.get_line(LANG, 'button.settings.true')
    else:
        return locale.get_line(LANG, 'button.settings.false')