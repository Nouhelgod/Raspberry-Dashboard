# Global modules
import json
import os

# Local modules
from lib import lib_json_reader as jsr

def get_month(month, lang = 'en_US'):
    """
    Args:
        month (str): '01' -- Number of month with 0 if not oct. nov. dec. 
        lang (str, optional): -- Language. Defaults to 'en_US'.

    Returns:
        str: name of month.
    """
    file = os.path.join(os.path.dirname(__file__), f'lang/{lang}.json')
    months = jsr.read(file, 'months')
        
    return months[month]
    

def get_weekday(weekday, lang = 'en_US'):
    """
    Args:
        weekday (str): '1' -- Number of weekday .
        lang (str, optional): -- Language. Defaults to 'en_US'.

    Returns:
        str: name of weekday.
    """
    file = os.path.join(os.path.dirname(__file__), f'lang/{lang}.json')
    
    weekdays = jsr.read(file, 'weekdays')
        
    return weekdays[str(weekday)]