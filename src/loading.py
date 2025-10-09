import curses
import sys
from CONSTANTS import START_MENU_FILE
from buffer import Buffer

def load_buffer_into_window(buffer, window, cursor, curses_window): 
    for row, line in enumerate(buffer[window.row:window.row + window.n_rows]):
            # Add indicators ('<<' or '>>') to show that there is more text off-screen.
            if row == cursor.row - window.row and window.col > 0:
                line = "«" + line[window.col + 1:]
            if len(line) > window.n_cols:
                line = line[:window.n_cols - 1] + "»"

            curses_window.addstr(row, 0, line)

def load_file_into_buffer(filename = START_MENU_FILE):
    buffer = None
    with open(file=filename) as file:
        # The contents of the file are stored in-memory until they’re ready to be rewritten into a file, hence the name 'buffer'.
        buffer = Buffer(file.read().splitlines())
    return buffer