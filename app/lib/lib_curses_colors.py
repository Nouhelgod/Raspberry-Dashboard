import curses

colors = {'white' : curses.COLOR_WHITE,
           'black' : curses.COLOR_BLACK,
           'red' : curses.COLOR_RED,
           'green' : curses.COLOR_GREEN,
           'yellow' : curses.COLOR_YELLOW,
           'blue' : curses.COLOR_BLUE,
           'magenta' : curses.COLOR_MAGENTA,
           'cyan' : curses.COLOR_CYAN
           }

def get_color(color):
    return colors[color]