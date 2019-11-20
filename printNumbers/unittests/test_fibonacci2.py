# -*- coding: utf-8 -*-
#
# test_fibonacci.py
#
# This file is part of PrintNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# PrintNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PrintNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrintNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Unit tests: 'fibonacci'.
#

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.fibonacci import *

class TestFibonacci2(unittest.TestCase):

    def test_value_1(self):
        print("Doesnt it work beautifully?")
        self.assertTrue(FibonacciSequence(20)[-1] > 20 )


def suite():
    suite = unittest.makeSuite(TestFibonacci2, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
