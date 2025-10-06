import curses
from vim_puzzles import vim_puzzles_start
from editor import editor

def main(stdscr):
    
    
    curses.curs_set(0)  # hide cursor in normal mode
    stdscr.clear()
    # stdscr.addstr(0, 0, "Normal mode. Press ':' to enter command mode. Type ':q!' to quit.")
    stdscr.refresh()
    editor(stdscr)
    

    # vim_puzzles_start(stdscr)
    

curses.wrapper(main)
