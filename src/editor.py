import argparse
import curses
import sys
from CONSTANTS import MAIN_MENU_FILE
from buffer import Buffer
from loading import load_buffer_into_window, load_file_into_buffer
from cursor import Cursor
from window import Window, left, right
from press_keys import press_key_logic

# Tutorial: https://wasimlorgat.com/posts/editor.html


# Initial insertion point. Was the 'main' function in the tutorial. 
def editor(stdscr):

    buffer = load_file_into_buffer()
    
    window = Window(curses.LINES - 1, curses.COLS - 1)
    cursor = Cursor()

    while True:
        stdscr.erase()

        load_buffer_into_window(buffer, window, cursor, stdscr)

        # Call translate. This converts the cursor position in the buffer to the corresponding position in the window. 
        stdscr.move(*window.translate(cursor))

        # Asks for the user to press a key.
        key_pressed = stdscr.getkey()

        # Handle the key press logic in a separate function.
        press_key_logic(window, buffer, cursor, key_pressed)