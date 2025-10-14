import curses
from start_menu import start_menu

def main(
        stdscr: curses.window
    ):
    curses_window = stdscr

    height, width = curses_window.getmaxyx()

    mid_x = width // 2

    # curses_window.resize(height, mid_x)
       # Get screen size

    # Create two windows
    left_win: curses.window = curses.newwin(height, mid_x, 0, 0)
    right_win: curses.window = curses.newwin(height, width - mid_x, 0, mid_x)

    # Enable special keys for both
    left_win.keypad(True)
    right_win.keypad(True)

    # Draw borders
    left_win.box()
    right_win.box()

    left_win.addstr(1, 1, "Left window: use arrows, 'q' to quit")
    right_win.addstr(1, 1, "Right window")

    left_win.refresh()
    right_win.refresh()

    # current_win = left_win

    # current_win.getkey()

    # curses_window.clear()
    # curses_window.refresh()
    start_menu(left_win, right_win)

if __name__ == "__main__":
    curses.wrapper(main)
    
