# Global modules
import json
import os

# Local modules
from lib import lib_json_wrapper as jsr


def get_month(month: str, lang: str = 'en_GB'):
    """
    Args:
        month (str): '01' -- Number of month with 0 if not oct. nov. dec. 
        lang (str, optional): -- Language. Defaults to 'en_GB'.

    Returns:
        str: name of month.
    """
    file = os.path.join(os.path.dirname(__file__), f'lang/{lang}.json')
    months = jsr.read(file, 'months')
        
    return months[month]
    

def get_weekday(weekday: str, lang: str = 'en_GB'):
    """
    Args:
        weekday (str): '1' -- Number of weekday .
        lang (str, optional): -- Language. Defaults to 'en_GB'.

    Returns:
        str: name of weekday.
    """
    file = os.path.join(os.path.dirname(__file__), f'lang/{lang}.json')
    
    weekdays = jsr.read(file, 'weekdays')
        
    return weekdays[str(weekday)]