# Tutorial: https://wasimlorgat.com/posts/editor.html

# Window class sets dimensions for the size of the window to avoid the error "_curses.error: addwstr() returned ERR" for especially large windows.
class Window:
    def __init__(self, n_rows, n_cols, row=0, col=0):
        self.n_rows = n_rows
        self.n_cols = n_cols

        #  Top-left position of the window in the buffer. Tracking this lets us move the window (our view of the buffer) independently of the cursor.
        self.row = row
        self.col = col

    @property
    def bottom(self):
        return self.row + self.n_rows - 1

    def up(self, cursor):
        if cursor.row == self.row - 1 and self.row > 0:
            self.row -= 1

    def down(self, buffer, cursor):
        if cursor.row == self.bottom + 1 and self.bottom < len(buffer) - 1:
            self.row += 1

# Horizontal scrolling. left_margin and right_margin are the number of columns to leave empty on the left and right sides of the window.
    def horizontal_scroll(self, cursor, left_margin=5, right_margin=2):
        page_n_cols = self.n_cols - left_margin - right_margin
        n_pages = max((cursor.col - left_margin) // page_n_cols, 0)
        self.col = n_pages * page_n_cols

# Moves the cursor to the correct position on the screen relative to the window.
    def translate(self, cursor):
        return cursor.row - self.row, cursor.col - self.col


def left(window, buffer, cursor):
    cursor.left(buffer)
    window.up(cursor)
    window.horizontal_scroll(cursor)


def right(window, buffer, cursor):
    cursor.right(buffer)
    window.down(buffer, cursor)
    window.horizontal_scroll(cursor)