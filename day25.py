'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day25.py
Purpose:    Advent of Code 2017, day 25
'''

from collections import defaultdict
import sys

steps = 12861455
states = {
    'a': ( (1, +1, 'b'),    (0, -1, 'b') ),
    'b': ( (1, -1, 'c'),    (0, +1, 'e') ),
    'c': ( (1, +1, 'e'),    (0, -1, 'd') ),
    'd': ( (1, -1, 'a'),    (1, -1, 'a') ),
    'e': ( (0, +1, 'a'),    (0, +1, 'f') ),
    'f': ( (1, +1, 'e'),    (1, +1, 'a') ),
}

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
YAML instruction interpretation.
:return:    sum of values in dictionary.
'''
def follow_yaml():
    tape = defaultdict( int )
    pos, state = 0, 'a'

    for _ in range(steps):
        val = tape[pos]
        write, move, state = states[state][val]
        tape[pos] = write
        pos += move

    return sum( tape.values() )


'''
Run methods associated with part 'a'.
'''
def part_a():
    checksum = follow_yaml()
    print( "The diagnostic checksum is {0}.".format(checksum) )
    return 0


# --------------------------------------------------------------
# --------------------------------------------------------------

if ( __name__ == "__main__" ):
    part_a()
