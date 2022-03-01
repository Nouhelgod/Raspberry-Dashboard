# Global modules
import os

# Local modules
from lib import lib_json_wrapper as jsr

def get_line(lang, line, **kwargs):
    """Get text line for telebot

    Args:
        lang (str): language
        line (str): text line key

    Returns:
        str: text line.
    """
    file = os.path.join(os.path.dirname(__file__), f'lang/{lang}.json')
        
    return jsr.read(file, line)
