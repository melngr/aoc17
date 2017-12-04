'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day03.py
Purpose:    Advent of Code, day 3
'''

input_port = 265149

import math
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------




'''
Run methods associated with part 'a'.
'''
def part_a():
    distance = count_steps( input_port )
    print( "Port {0} is {1} steps from the start.".format( input_port, distance ) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    return 0


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
