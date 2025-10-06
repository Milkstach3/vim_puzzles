import curses

def vim_puzzles_start(stdscr):
    command_buffer = ""
    command_mode = False

    height, width = stdscr.getmaxyx()

    while True:
        ch = stdscr.getch()

        # Command mode behavior
        if command_mode:
            if ch in (27,):  # ESC key
                # Cancel command mode
                command_mode = False
                command_buffer = ""
                curses.curs_set(0)
                stdscr.move(height - 1, 0)
                stdscr.clrtoeol()
                stdscr.refresh()
                continue

            elif ch in (10, 13):  # Enter key
                # Execute command
                if command_buffer == "q!":
                    break  # exit program
                else:
                    # Unknown command feedback
                    stdscr.addstr(height - 1, 0, f":{command_buffer}  (Unknown command)")
                    stdscr.refresh()
                    curses.napms(1000)  # pause briefly
                    stdscr.move(height - 1, 0)
                    stdscr.clrtoeol()
                    command_buffer = ""
                    command_mode = False
                    curses.curs_set(0)

            elif ch in (curses.KEY_BACKSPACE, 127, 8):
                # Handle backspace
                if command_buffer:
                    command_buffer = command_buffer[:-1]
                    stdscr.move(height - 1, 0)
                    stdscr.clrtoeol()
                    stdscr.addstr(height - 1, 0, ":" + command_buffer)
                    stdscr.refresh()
                else:
                    command_mode = False
                    curses.curs_set(0)
                    stdscr.move(height - 1, 0)
                    stdscr.clrtoeol()
                    stdscr.refresh()

            else:
                # Regular character input
                try:
                    c = chr(ch)
                except ValueError:
                    continue
                command_buffer += c
                stdscr.move(height - 1, 0)
                stdscr.clrtoeol()
                stdscr.addstr(height - 1, 0, ":" + command_buffer)
                stdscr.refresh()

        # Normal mode behavior
        else:
            if ch == ord(':'):
                # Enter command mode
                command_mode = True
                command_buffer = ""
                curses.curs_set(1)  # show cursor in command mode
                stdscr.move(height - 1, 0)
                stdscr.clrtoeol()
                stdscr.addstr(height - 1, 0, ":")
                stdscr.refresh()
            # You can add more normal mode key handling here if needed