#!/usr/bin/env python3
"""ANSI Terminal Functions"""

__author__ = "Jason Rebuck"
__copyright__ = "2021"
__version__ = "0.10"

import sys

class Term:
    """ANSI Terminal Functions"""

    esc = "\033["

    def __init__(self):
        """Init"""
        pass

    def _wrap(self, attr="", end=""):
        """Wrap with ANSI codes"""
        sys.stdout.write(f"{self.esc}{attr}{end}")
        sys.stdout.flush()

    #Cursor Pos
    def up(self, num=1):
        """Cursor Up N"""
        self._wrap(num, "A")

    def down(self, num=1):
        """Cursor Down N"""
        self._wrap(num, "B")

    def left(self, num=1):
        """Cursor Forward N"""
        self._wrap(num, "C")

    def right(self, num=1):
        """Cursor Back N"""
        self._wrap(num, "D")

    def next(self, num=1):
        """Cursor Back N"""
        self._wrap(num, "E")

    def prev(self, num=1):
        """Cursor Back N"""
        self._wrap(num, "F")

    def col(self, col=0):
        """Cursor to Horizontal Pos"""
        self._wrap(col, "G")

    def goto(self, row=0, col=0):
        """Cursor to Screen Pos"""
        self._wrap(f"{row};{col}", "H")

    def row(self, row=0):
        """Cursor to Vertical Pos"""
        self._wrap(row, "f")

    def pg_up(self, row=1):
        """Cursor to Vertical Pos"""
        self._wrap(row, "S")

    def pg_down(self, row=1):
        """Cursor to Vertical Pos"""
        self._wrap(row, "T")

    #Color
    #This is for total control of color and style
    #Use Color class for anything complex..."
    def color(self, num=0):
        """Start Color Code"""
        self._wrap(f"3{num}", "m")

    def bg(self, num=0):
        """Start Background Code"""
        self._wrap(f"4{num}", "m")

    def style(self, num=0):
        """Start Style Code"""
        self._wrap(num, "m")

    # Clear
    def erase(self):
        """Clear Screen"""
        self._wrap("2","J")

    def eraseln(self, num=0):
        """Clear Line"""
        self._wrap(num, "K")

    def reset(self):
        """Reset Term"""
        self._wrap("", "c")

    #Cursor Vis
    def hide(self):
        """Hide Cursor"""
        self._wrap("?25", "l")

    def show(self):
        """Show Cursor"""
        self._wrap("?25", "h")

    #Save/Restore
    def save(self):
        """Save Cursor Pos"""
        self._wrap("", "s")

    def restore(self):
        """Restore Cursor Pos"""
        self._wrap("", "u")


if __name__ == "__main__":
    pass

