# Global modules
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

def get_color(color: str):
    """Get color in curses format

    Args:
        color (str): color name -> white, black, red, green, yellow, blue, magenta, cyan

    Returns:
        curses.A_COLOR: Color in curses format
    """
    return colors[color]


# TODO: Rework this system