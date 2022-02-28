# Global modules
import curses

# Local modules
from lib import lib_curses_colors as cols
from lib import lib_json_wrapper as jsr
from lib import lib_drawing as drw

from mod import mod_clock
from mod import mod_date


def wrapped_main():
    """Curses wrapper"""
    curses.wrapper(main)


# Initialzation
def init():
    global LANG, DATE_FORMAT, COLOR_FG, COLOR_BG    
    LANG = jsr.read('app_settings.json', 'timegui.loc.language')
    DATE_FORMAT = jsr.read('app_settings.json', 'timegui.loc.date_format')
    COLOR_FG = cols.get_color(jsr.read('app_settings.json', 'timegui.color.foreground'))
    COLOR_BG = cols.get_color(jsr.read('app_settings.json', 'timegui.color.background'))


# Main loop
def main(stdscr):
    init()
    
    curses.start_color()
    curses.init_pair(1, COLOR_BG, COLOR_FG)
    curses.init_pair(2, COLOR_FG, COLOR_BG)

    cp = 1

    semicolon_state = True
    time_last = mod_clock.get_time()

    while True:
        stdscr.erase()
        
        h, w = stdscr.getmaxyx()

        drw.fill_bg(stdscr, cp, h, w)       
    
        time_last, semicolon_state = mod_clock.draw(stdscr, cp, semicolon_state, time_last)
        mod_date.draw(stdscr, cp, DATE_FORMAT, LANG)

        curses.curs_set(0)
        stdscr.refresh()


if __name__ == '__main__':
    wrapped_main()