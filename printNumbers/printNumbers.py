# -*- coding: utf-8 -*-
#
# printNumbers.py
#
# This file is part of printNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# printNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# printNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with printNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Software Development in Science Workshop 2017
#        Python GitHub project example
#

"""
Usage:
  printNumbers.py -h --help
  printNumbers.py [--fibonacci|--factorial] <operand>

Options:
  -h --help       Print usage.
  --fibonacci     Print the fibonacci sequence.
  --factorial     Print the factorial.
"""

from docopt import docopt
from parameters import *
from functions.fibonacci import *
from functions.factorial import *
from numpy.random import randint

# INSULTS TABLE
insults = ('NOW F$#! OFF YOU GIT','YOUR MOTHER WAS A HAMSTER AND YOUR FATHER SMELT OF ELDERBERRIES','YOU SMELL OF ROTTEN MEATBALLS','YOU MOVE LIKE A PREGNANT COW')

#
# FUNCTION TABLE
#
functionTable = { CONST_FUNC_CODE_FIBONACCI : FibonacciSequence,
                  CONST_FUNC_CODE_FACTORIAL : Factorial,
                }

#
# MAIN ENTRY
#
if __name__ == '__main__':
    print('Conflict 1')
    print('')
    print(CONST_VERSION_STRING)
    print('')
    print('Problem?')

    # Process command line arguments.
    params = Parameters(docopt(__doc__, version = CONST_VERSION))
    params.PrintParameters()

    # Call corresponding function with <functionIndex> from <functionTable>.
    result = functionTable[params.functionIndex](params.operand)

    # Print results depending on the executed function.
    if params.functionIndex == CONST_FUNC_CODE_FIBONACCI:
        print('fib(' + str(params.operand) + ') =', result)
    elif params.functionIndex == CONST_FUNC_CODE_FACTORIAL:
        print(str(params.operand) + '! =', str(result))
    print(insults[randint(0,len(insults))])
