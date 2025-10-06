import curses

def insert_mode(stdscr):
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, 0, "Insert mode. Press 'Esc' to return to normal mode.")
    stdscr.refresh()
    while True:
        ch = stdscr.getch()
        if ch == 27:  # ESC key
            break
        elif ch in (10, 13):  # Enter key
            stdscr.addstr("\n")
        elif ch in (curses.KEY_BACKSPACE, 127, 8):
            y, x = stdscr.getyx()
            if x > 0:
                stdscr.move(y, x - 1)
                stdscr.delch()
        else:
            try:
                c = chr(ch)
                stdscr.addstr(c)
            except ValueError:
                continue
        stdscr.refresh()