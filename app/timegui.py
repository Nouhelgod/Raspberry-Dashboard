# Global modules
import curses

# Local modules
from lib import lib_curses_colors as cols
from lib import lib_json_reader as jsr
from lib import lib_drawing as drw

from mod import mod_clock
from mod import mod_date

# Initialzation    
LANG = jsr.read('settings.json', 'language')
DATE_FORMAT = jsr.read('settings.json', 'date_format')
COLOR_FG = cols.get_color(jsr.read('settings.json', 'color_foreground'))
COLOR_BG = cols.get_color(jsr.read('settings.json', 'color_background'))

def wrapped_main():
    curses.wrapper(main)


# Main loop
def main(stdscr):

    # Initialization
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
        mod_date.draw(stdscr, DATE_FORMAT, LANG, cp)

        curses.curs_set(0)
        stdscr.refresh()



if __name__ == '__main__':
    wrapped_main()