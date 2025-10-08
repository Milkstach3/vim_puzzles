


# Class to manage the cursor position (not to be confused with 'curses', the library imported to handle terminal display and input).
class Cursor:
    def __init__(self, row=0, col=0, col_hint=None):
        self.row = row
        self._col = col
        # _col_hint remembers what position the cursor was previously in and sets the cursor back to that position if moving back to a visited column. This is to handle cases where when the cursor moves up or down to a line shorter than the previous line, the cursor should return to the previous column if the user moves back to that line.
        self._col_hint = col if col_hint is None else col_hint

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, col):
        self._col = col
        self._col_hint = col

# Restrict the cursor's column position to at most the length of the current line.
    def _clamp_col(self, buffer):
        self._col = min(self._col_hint, len(buffer[self.row]))

# Movement methods for the cursor.
# self.row/col >< 0 prevents the cursor from going out of bounds.
    def up(self, buffer):
        if self.row > 0:
            self.row -= 1
            self._clamp_col(buffer)

    def down(self, buffer):
        if self.row < len(buffer) - 1:
            self.row += 1
            self._clamp_col(buffer)

    def left(self, buffer):
        if self.col > 0:
            self.col -= 1
        elif self.row > 0:
            self.row -= 1
            self.col = len(buffer[self.row])

    def right(self, buffer):
        if self.col < len(buffer[self.row]):
            self.col += 1
        elif self.row < len(buffer) - 1:
            self.row += 1
            self.col = 0