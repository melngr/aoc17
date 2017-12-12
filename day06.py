'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day06.py
Purpose:    Advent of Code 2017, day 6
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day06.txt' exist in directory.
:return:    list of ints will all values from input file.
:throws:    IOError, if file cannot be opened.
            ValueError, if file contains illegal letter.
'''
def read_banks():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day06.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day06.txt' could not be opened." )

    banks = f.readline().strip().split(' ')
    for i in range( len(banks) ):
        try:
            banks[i] = int( banks[i] )
        except ValueError:
            raise ValueError( "Illegal letter found in file." )

    f.close()
    return banks


'''
Duplicate counting method.
:param:     banks, list of ints needing balancing.
:requires:  banks != None
:return:    map of steps taken to find duplicate.
:throws:    IndexError, if list cannot be parsed.
:modifies:  banks.
:effects:   applies balancing method and changes values.
'''
def find_duplicate(banks):
    cycles = 0
    history = {}

    try:
        while tuple( banks ) not in history:
            history[ tuple(banks) ] = cycles

            maximum = max( banks )
            curr = banks.index( maximum )

            banks[ curr ] = 0
            while maximum > 0:
                curr = ( curr + 1 ) % len( banks )
                banks[ curr ] += 1
                maximum -= 1

            cycles += 1

    except IndexError as err:
        raise IndexError( err )

    return cycles, (cycles - history[ tuple(banks) ])


'''
Run methods associated with part 'a'.
'''
def part_a():
    banks = read_banks()
    cycles, diff = find_duplicate(banks)
    print( "It takes {0} cycles to find a duplicate.".format(cycles) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    banks = read_banks()
    cycles, diff = find_duplicate(banks)
    print( "There are {0} steps between when the pattern is seen, and when it repeats.".format(diff) )


# --------------------------------------------------------------
# --------------------------------------------------------------

if ( __name__ == "__main__" ):

    if ( len(sys.argv) != 2 ):
        if ( len(sys.argv) < 2 ):
            raise IndexError( "USAGE => too few args" )
        else:
            raise IndexError( "USAGE => too many args" )

    else:
        part = sys.argv[1]
        if ( part.strip() == 'a' ):
            part_a()
        elif ( part.strip() == 'b' ):
            part_b()
        else:
            raise RuntimeError( "USAGE => invalid argument" )
