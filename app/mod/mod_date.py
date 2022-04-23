# Global modules
import datetime
import curses

# Local modules
from lib.lib_calendar import calendar
from lib import lib_drawing as drw


def draw(stdscr, cp: int, date_format: str, lang: str):
    """Draw date on screen.

    Args:
        stdscr (stdscr): stdscr
        cp (int): number of color pair
        date_format (str): EU (DD month YYYY) / US (Month DD YYYY)
        lang (str): Language
    """
    h, w = stdscr.getmaxyx()
    
    month = datetime.datetime.now().strftime('%m')
    year = datetime.datetime.now().strftime('%y')
    day = datetime.datetime.now().strftime('%d')

    if day[0] == '0':
        day = day[1]

    if date_format == 'EU':
        datestr = f'{day} {calendar.get_month(month, lang)} 20{year}'

    elif date_format == 'US':
        month = calendar.get_month(month, lang)
        head = month[0]
        body = month[1:]
        datestr = f'{head.upper()}{body} {day} 20{year}'

    weekday = datetime.datetime.today().weekday()
    weekdaystr = f'{calendar.get_weekday(weekday, lang)}'

    stdscr.attron(curses.color_pair(drw.invert_cp(cp)))
    stdscr.addstr((h // 2) + 4, drw.get_center(w, datestr), datestr)
    stdscr.addstr((h // 2) + 5, drw.get_center(w, weekdaystr), weekdaystr)
    stdscr.attroff(curses.color_pair(drw.invert_cp(cp)))