
# Tutorial: https://wasimlorgat.com/posts/editor.html

# Buffer class to manage the text being edited. 
class Buffer:
    def __init__(self, lines):
        self.lines = lines

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]

    @property
    def bottom(self):
        return len(self) - 1

# Pop the line under the cursor, split it at the cursor, and concatenate: 1. the before part, 2. the string to be inserted, and 3. the after part.
    def insert(self, cursor, string):
        row, col = cursor.row, cursor.col
        try:
            current = self.lines.pop(row)
        except IndexError:
            current = ''
        new = current[:col] + string + current[col:]
        self.lines.insert(row, new)

# Split the line at the cursor into two lines. Called when Enter is pressed.
    def split(self, cursor):
        row, col = cursor.row, cursor.col
        current = self.lines.pop(row)
        self.lines.insert(row, current[:col])
        self.lines.insert(row + 1, current[col:])

    def delete(self, cursor):
        row, col = cursor.row, cursor.col
        # If the cursor is at the last position in the buffer, don’t do anything.
        if (row, col) < (self.bottom, len(self[row])):
            current = self.lines.pop(row)

            # If the cursor is not at the end of the line, then just delete the character under the cursor.
            if col < len(current):
                new = current[:col] + current[col + 1:]
                self.lines.insert(row, new)

            # If the cursor is at the end of the line, then join the current line to the next.
            else:
                next = self.lines.pop(row)
                new = current + next
                self.lines.insert(row, new)


def clamp(x, lower, upper):
    if x < lower:
        return lower
    if x > upper:
        return upper
    return x
