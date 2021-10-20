#!/usr/bin/env python3
"""ANSI Terminal Functions"""

__author__ = "Jason Rebuck"
__copyright__ = "2021"
__version__ = "0.10"

import io

class Term:
    """ANSI Terminal Functions"""

    esc = "\033["

    def __init__(self):
        """Init"""
        pass

    def _wrap(self, attr="", end=""):
        """Wrap with ANSI codes"""
        io.write(f"{self.esc}{attr}{end}")
        io.flush()

    #Cursor Pos
    def up(num=1):
        """Cursor Up N"""
        self._wrap(num, "A")

    def down(num=1):
        """Cursor Down N"""
        self._wrap(num, "B")

    def left(num=1):
        """Cursor Forward N"""
        self._wrap(num, "C")

    def right(num=1):
        """Cursor Back N"""
        self._wrap(num, "D")

    def next(num=1):
        """Cursor Back N"""
        self._wrap(num, "E")

    def prev(num=1):
        """Cursor Back N"""
        self._wrap(num, "F")

    def col(col=0):
        """Cursor to Horizontal Pos"""
        self._wrap(col, "G")

    def goto(row=0, col=0):
        """Cursor to Screen Pos"""
        self._wrap(f"{row};{col}", "H")

    def row(row=0):
        """Cursor to Vertical Pos"""
        self._wrap(row, "f")

    def pg_up(row=1):
        """Cursor to Vertical Pos"""
        self._wrap(row, "S")

    def pg_down(row=1):
        """Cursor to Vertical Pos"""
        self._wrap(row, "T")

    #Status
    def status():
        """Request Status Position of Cursor"""
        #NOTE: returns answer: "esc[n;mR"
         self._wrap("6", "n")

    #Color
    #This is for total control of color and style
    #Use Color class for anything complex..."
    def color(num=0):
        """Start Color Code"""
        self._wrap(f"3{num}", "m")

    def bg(num=0):
        """Start Background Code"""
        self._wrap(f"4{num}", "m")

    def style(num=0):
        """Start Style Code"""
        self._wrap(num, "m")

    # Clear
    def erase():
        """Clear Screen"""
        self._wrap("2","J")

    def eraseln(num=0):
        """Clear Line"""
        self._wrap(num, "K")

    def reset():
        """Reset Term"""
        self._wrap("", "c")

    #Cursor Vis
    def hide():
        """Hide Cursor"""
        self._wrap("?25", "l")

    def show():
        """Show Cursor"""
        self._wrap("?25", "h")

    #Save/Restore
    def save():
        """Save Cursor Pos"""
        self._wrap("", "s")

    def restore():
        """Restore Cursor Pos"""
        self._wrap("", "u")


if __name__ == "__main__":
    pass

