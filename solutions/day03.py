'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day03.py
Purpose:    Advent of Code 2017, day 3
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day03.txt' to exist in 'inputs' subdirectory.
:return:    number in file.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if number cannot be cast to int.
'''
def read_num():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day03.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day03.txt' could not be opened." )
        return 1

    try:
        num = int( f.readline().strip() )
    except ValueError:
        raise ValueError( "Illegal letter found as number." )
        return 1

    f.close()
    return num


'''
Run methods associated with part 'a'.
'''
def part_a():
    num = read_num()
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    num = read_num()
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
