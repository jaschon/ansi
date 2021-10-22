#!/usr/bin/env python3
"""ANSI Terminal Editor Example"""

__author__ = "Jason Rebuck"
__copyright__ = "2021"
__version__ = "0.05"

import sys, tty
try:
    from ansi import Ansi
except ImportError:
    from ansi.ansi import Ansi


class Editor:

    commands = {
            3 : 'quit_key', #cmd-c
            10 : 'enter_key', #press enter
            13 : 'enter_key', #press enter
            127 : 'delete_key', #press delete
            'default' : 'default_key', #65-90 = A-Z, 97-122 = a-z
            49 : 'color_key',
            50 : 'color_key',
            51 : 'color_key',
            52 : 'color_key',
            53 : 'color_key',
            54 : 'color_key',
            55 : 'color_key',
            56 : 'color_key',


            #arrow keys
            27 : 'check_next', #check next for left, right keys
            "27-91" : 'check_next', #check next for arrows
            "27-91-65" : 'up_key',
            "27-91-66" : 'down_key',
            "27-91-68" : 'left_key',
            "27-91-67" : 'right_key',
    }


    def __init__(self):
        self.set_tty()
        self.ansi = Ansi()

    #Setup
    def clear_var(self):
        """Setup Vars"""
        self.index = 0
        self.text = ""
        self.char = ""

    def set_tty(self):
        """Set tty to raw mode"""
        tty.setraw(sys.stdin)

    def return_tty(self):
        """Return from raw mode"""
        tty.setcbreak(sys.stdin)

    #IO Functions
    def flush_buffer(self):
        """Flush Buffer"""
        sys.stdout.flush()

    def read_char(self):
        """Read char and return char code"""
        return ord(sys.stdin.read(1))

    def write_text(self, text=""):
        """Write text to screen"""
        sys.stdout.write(text)

    def write_output(self):
        """Set cursor and output"""
        self.ansi.right(1000)
        self.ansi.cleareol()
        self.write_text(self.check_syntax())
        self.ansi.right(1000)
        self.check_advance_cursor()
        self.flush_buffer()

    #Checks
    def check_advance_cursor(self):
        """Advance the cursor"""
        if self.index > 0:
            self.ansi.left(self.index)

    def check_syntax(self):
        """Syntax Highlight...TO DO"""
        return self.text

    def check_keyboard(self, default=""):
        method = self.commands.get(self.char, default)
        try:
            getattr(self, method)()
        except (TypeError, AttributeError):
            pass

    def check_next(self):
        """get next input char and run check_keyboard again"""
        next_char = self.read_char()
        self.char = f"{self.char}-{next_char}"
        self.check_keyboard()

    #Keyboard press methods...
    def quit_key(self):
        """Quit!"""
        self.return_tty()
        self.ansi.reset()
        sys.exit()

    def default_key(self):
        if 32 <= self.char <= 126:
            self.char_key()

    def color_key(self):
        self.ansi.color(50-self.char)

    def char_key(self):
        """Alpha Keyboard Press"""
        self.text = f"{self.text[:self.index]}{chr(self.char)}{self.text[self.index:]}" 
        self.index +=1

    def delete_key(self):
        """Delete Key Press"""
        self.text = f"{self.text[:self.index-1]}{self.text[self.index:]}"
        self.index -= 1

    def enter_key(self):
        """Enter Key Press"""
        self.ansi.next()
        self.ansi.right(1000)
        self.clear_var()

    def left_key(self):
        """Left Key Press"""
        self.index = max(0, self.index - 1)

    def right_key(self):
        """Right Key Press"""
        self.index = min(len(self.text), self.index + 1)

    def up_key(self):
        """Up Key Press"""
        pass

    def down_key(self):
        """Up Key Press"""
        pass

    # Loop Modes
    def test(self):
        """Echo Key Press"""
        while True:
            char = self.read_char()
            if char == 3: 
                self.quit_key()
            self.write_text(f"{str(char)} = '{chr(char)}'")
            self.flush_buffer()
            self.enter_key()

    def run(self):
        """Main Loop"""
        self.ansi.clear()
        self.ansi.goto(0,0)
        while True: #each line loop
            self.clear_var() #clear input vars
            while True: #loop for each char
                self.char = self.read_char() #get char
                self.check_keyboard("default_key") #do keyboard stuff
                self.write_output() #output


if __name__ == "__main__":
    c = Editor().run()
