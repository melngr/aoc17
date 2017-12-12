'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day11.py
Purpose:    Advent of Code 2017, day 11
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
:requires:  file 'day11.txt' to exist in 'inputs' subdirectory.
:return:    string of groups.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_steps():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day11.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day11.txt' could not be opened." )

    steps = f.readline().strip().split(',')

    f.close()
    return steps


'''
Method to find endpoint of path.
:param:     path, list of directions.
:return:    list of three-tuples of path followed.
:throws:    RuntimeError, if path contains illegal direction.
'''
def run(steps):
    path, x, y, z = [], 0, 0, 0
    for step in steps:
        if ( step == 'n' ):
            y += 1
            z -= 1
        elif ( step == "ne" ):
            x += 1
            z -= 1
        elif ( step == "se" ):
            x += 1
            y -= 1
        elif ( step == 's' ):
            y -= 1
            z += 1
        elif ( step == "sw" ):
            x -= 1
            z += 1
        elif ( step == "nw" ):
            x -= 1
            y += 1
        else:
            raise RuntimeError( "Illegal direction found in path." )

        path.append( tuple( (x, y, z) ) )

    return path


'''
Hexagonal distance calculation.
:param:     final, endpoint of which to find the distance from the origin.
:return:    distance using the hexagonal grid distance formula.
'''
def find_dist(final):
    return ( (abs(final[0]) + abs(final[1]) + abs(final[2])) // 2 )


'''
Run methods associated with part 'a'.
'''
def part_a():
    steps = read_steps()
    path = run(steps)
    dist = find_dist( path[ len(path) - 1 ] )
    print( "The distance of the endpoint from the origin is {0}.".format(dist) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    steps = read_steps()
    path = run(steps)
    max_dist = find_dist( path[0] )
    for tup in path[ 1: ]:
        max_dist = max( max_dist, find_dist(tup) )
    print( "The maximum distance from the origin is {0}.".format(max_dist) )
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
