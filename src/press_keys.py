import sys
from window import Window, left, right


def press_keys(window, buffer, cursor, key_pressed):
    # Exit program if 'q' is pressed. Need to implement a save function later.
        if key_pressed == "q":
            sys.exit(0)

        # Movement keys
        elif key_pressed == "KEY_LEFT":
            left(window, buffer, cursor)

        elif key_pressed == "KEY_DOWN":
            cursor.down(buffer)
            window.down(buffer, cursor)
            window.horizontal_scroll(cursor)

        elif key_pressed == "KEY_UP":
            cursor.up(buffer)
            window.up(cursor)
            window.horizontal_scroll(cursor)

        elif key_pressed == "KEY_RIGHT":
            right(window, buffer, cursor)

        # Insert a new line when enter is pressed.
        elif key_pressed == "\n":
            buffer.split(cursor)
            right(window, buffer, cursor)

        # The second condition in this and the next elif is for MAC compatibility. 
        elif key_pressed in ("KEY_DELETE", "\x04"):
            buffer.delete(cursor)
        
        # Move left and delete if backspace is pressed and the cursor is not at the beginning of the file.
        elif key_pressed in ("KEY_BACKSPACE", "\x7f"):
            if (cursor.row, cursor.col) > (0, 0):
                left(window, buffer, cursor)
                buffer.delete(cursor)
        else:
            buffer.insert(cursor, key_pressed)
            for _ in key_pressed:
                right(window, buffer, cursor)
