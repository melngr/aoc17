'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day19.py
Purpose:    Advent of Code 2017, day 19
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:part:      determines whether or not the string should be split.
:requires:  file 'day19.txt' to exist in 'inputs' subdirectory.
:return:    string of groups.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if illegal letter is found in input.
'''
def read_diagram():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day19.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day19.txt' could not be opened." )
        return 1

    diagram = []
    for line in f:
        diagram.append( line )

    f.close()
    return diagram


'''
'''
def follow(diagram):
    path, steps = "", 0
    dirs = { 'u': (0, -1), 'r': (1, 0), 'd': (0, 1), 'l': (-1, 0) }
    curr, move, x, y = '|', 'd', diagram[0].index('|'), 0
    while curr != ' ':
        x, y, steps = (x + dirs[move][0]), (y + dirs[move][1]), steps + 1
        curr = diagram[y][x]

        if ( curr == '+' ):
            if ( move in ('u', 'd') ):
                if ( diagram[y][(x - 1)] != ' ' ):  move = 'l'
                else:  move = 'r'
            elif ( move in ('l', 'r') ):
                if ( diagram[(y - 1)][x] != ' ' ):  move = 'u'
                else:  move = 'd'

        elif ( curr not in ('|', '-', ' ') ):
            path += curr

    return path, steps


'''
Run methods associated with part 'a'.
'''
def part_a():
    diagram = read_diagram()
    path, steps = follow(diagram)
    print( "The packet follows the path {0}.".format(path) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    diagram = read_diagram()
    path, steps = follow(diagram)
    print( "The packet takes {0} to follow the path.".format(steps) )
    return 0


# --------------------------------------------------------------
# --------------------------------------------------------------

if ( __name__ == "__main__" ):
    if ( len(sys.argv) != 2 ):
        if ( len(sys.argv) < 2 ):
            sys.stderr.write( "USAGE: too few args\n" )
        else:
            sys.stderr.write( "USAGE: too many args\n" )

    else:
        part = sys.argv[1]
        if ( part.strip().lower() == 'a' ):
            part_a()
        elif ( part.strip().lower() == 'b' ):
            part_b()
        else:
            sys.stderr.write( "USAGE: invalid argument\n" )
