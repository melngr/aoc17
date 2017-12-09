'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day03.py
Purpose:    Advent of Code 2017, day 3
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

input_port = 265149

import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
Run methods associated with part 'a'.
'''
def part_a():
    return 0


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
