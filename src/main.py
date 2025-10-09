import curses
from start_menu import start_menu

def main(
        stdscr: curses.window
    ):
    
    # curses.curs_set(0)  # hide cursor in normal mode
    stdscr.clear()
    stdscr.refresh()
    start_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
