import argparse
import curses
import sys
from CONSTANTS import START_MENU_FILE
from buffer import Buffer
from loading import load_buffer_into_window, load_file_into_buffer
from cursor import Cursor
from window import Window, left, right
from press_keys import press_key_logic
from modes import Mode

# Tutorial: https://wasimlorgat.com/posts/editor.html

# curses_window is stdscr renamed for clarity.
# Initial insertion point. Was the 'main' function in the tutorial. 
def start_menu(
        curses_window: curses.window
    ):

    # start_menu_buffer: Buffer = load_file_into_buffer()
    buffer: Buffer = load_file_into_buffer()
    
    window: Window = Window(curses.LINES - 1, curses.COLS - 1)
    cursor: Cursor = Cursor()

    mode: Mode = Mode.NORMAL
    
    # curses_window.erase()

    while True:
        curses_window.erase()

        load_buffer_into_window(buffer, window, cursor, curses_window)

        # Call translate. This converts the cursor position in the buffer to the corresponding position in the window. 
        curses_window.move(*window.translate(cursor))

        # Asks for the user to press a key on the keyboard.
        key_pressed = curses_window.getkey()

        # Handle the key press logic in a separate function.
        mode = press_key_logic(window, buffer, cursor, key_pressed)