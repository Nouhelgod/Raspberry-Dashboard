# Global modules
import curses


def get_center(width: int, line: str):
    """Get position of text line centered in screen.

    Args:
        width (int): screen width
        line (str): line of text

    Returns:
        int: position
    """
    return int((width // 2) - (len(line) // 2) - len(line) % 2)

def invert_cp(cp: int):
    """Switch two color pairs

    Args:
        cp (int): number of current color pair

    Returns:
        int: number of next color pair
    """
    if cp == 1:
        return 2
    else:
        return 1
    

def fill_bg(stdscr, cp: int, height: int, width: int):
    """Fill background with COLOR_BG

    Args:
        stdscr (stdscr): curses screen
        cp (int): color pair in curses format
        height (int): screen height
        width (int): screen width
    """
    for i in range(height):
            for j in range(width - 1):
                stdscr.attron(curses.color_pair(invert_cp(cp)))
                stdscr.addstr(i, j, ' ')
                stdscr.attroff(curses.color_pair(invert_cp(cp)))