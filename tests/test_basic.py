#!/usr/bin/env python3
"""Unittest Ansi Class"""

import sys
import unittest
try:
    from ansi import Ansi
except ImportError:
    from ansi.ansi import Ansi

class AnsiTest(Ansi):
    """Ansi Class for Testing"""

    test = ""

    def _wrap(self, attr="", end=""):
        self.test = f"{self.esc}{attr}{end}"


class TestBasic(unittest.TestCase):

    def setUp(self):
        """Setup Class"""
        self.ansi = AnsiTest()


    def test_one_param(self):
        #method, param?, compare string
        tests = (
                ("up", "1", "\x1b1A"),
                ("down", "1", "\x1b1B"),
                ("left", "1", "\x1b1C"),
                ("right", "1", "\x1b1D"),
                ("next", "1", "\x1b1E"),
                ("prev", "1", "\x1b1F"),
                ("col", "1", "\x1b1G"),
                ("pg_up", "1", "\x1b1S"),
                ("pg_down", "1", "\x1b1T"),

                ("hide", "", "\x1b?25l"),
                ("show", "", "\x1b?25h"),

                ("save", "", "\x1bs"),
                ("restore", "", "\x1bu"),

                ("clear", "", "\x1b2J"),
                ("cleareol", "", "\x1b0K"),
                ("clearbol", "", "\x1b2K"),
                ("clearln", "", "\x1b2K"),


                ("color", "5", "\x1b35m"),
                ("style", "6", "\x1b6m"),
                ("background", "7", "\x1b47m"),
                )

        for test in tests:
            self.ansi.test = ""
            if test[1]:
                getattr(self.ansi, test[0])(test[1])
            else:
                getattr(self.ansi, test[0])()
            self.assertEqual(test[2], self.ansi.test)


if __name__ == "__main__":
    unittest.main()

