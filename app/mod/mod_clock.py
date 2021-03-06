# Global modules
import curses
import datetime

# Local modules
from lib import lib_digits as digits
from lib import lib_special_symbols as spec


def get_time():
    """Get current time formated HH:MM:SS

    Returns:
        str: time formated HH:MM:SS
    """
    return datetime.datetime.now().strftime('%H:%M:%S')

def draw_symbol(stdscr, pos, smb, height, width, color):
    """Draw large symbol on the screen.

    Args:
        stdscr (stdscr): curses screen
        pos (int): 1..5 -- position
        smb (list): list formatted symbol
        height (int): screen height
        width (int): screen width
        color (curses.color_pair): color pair in curses format
    """
    stdscr.attron(color)

    for i in range(len(smb)):
        for j in range(len(smb[i])):
            if smb[i][j]:
                stdscr.addstr((height // 2) - 3 + i, (((width // 5) * pos)-(width // 5 // 2) - 3 + j), ' ')
    
def draw(stdscr, cp: int, semicolon_state: bool, time_last: str):
    """Draw clock on display.

    Args:
        stdscr (stdscr): stdscr
        cp (int): number of color pair
        semicolon_state (bool): draw semicolon if True
        time_last (str): last time (previous second)

    Returns:
        time (str): actual time
        semicolon_state (bool): actual semicolon state
    """

    time = get_time()
    time_H = time[0] + time[1]
    time_M = time[3] + time[4]

    h, w = stdscr.getmaxyx()
    
    draw_symbol(stdscr, 1, digits.get_digit(time_H[0]), h, w, curses.color_pair(cp))
    draw_symbol(stdscr, 2, digits.get_digit(time_H[1]), h, w, curses.color_pair(cp))
    draw_symbol(stdscr, 4, digits.get_digit(time_M[0]), h, w, curses.color_pair(cp))
    draw_symbol(stdscr, 5, digits.get_digit(time_M[1]), h, w, curses.color_pair(cp))
    
    if time != time_last:
        time_last = time
                 
        if semicolon_state:
            draw_symbol(stdscr, 3, spec.get_symbol(':'), h, w, curses.color_pair(cp))
        
        semicolon_state = not semicolon_state
    
    return time, semicolon_state