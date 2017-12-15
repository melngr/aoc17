'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day13.py
Purpose:    Advent of Code 2017, day 13
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from itertools import count
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day13.txt' to exist in 'inputs' subdirectory.
:return:    dictionary with layers mapped to depths.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if illegal letter is found in file.
'''
def read_firewall():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day13.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day13.txt' could not be opened." )
        return 1

    lines = [ line.strip().split(": ") for line in f ]
    try:
        firewall = { int(layer): int(depth) for layer, depth in lines }
    except ValueError:
        raise ValueError( "Illegal letter found as depth and/or range." )

    f.close()
    return firewall


'''
Severity check method.
:param:     layer, layer accessed in firewall.
            depth, range of scanner in layer.
:return:    value of severity check.
'''
def check_severity(layer, depth):
    off = layer % ((depth - 1) * 2)
    return ( (2 * (depth - 1)) - off ) if off > (depth - 1) else off


'''
Run methods associated with part 'a'.
'''
def part_a():
    firewall = read_firewall()
    severity = sum( layer * firewall[layer] for layer in firewall if \
        (check_severity(layer, firewall[layer]) == 0) )
    print( "The severity of all catches is {0}.".format(severity) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    firewall = read_firewall()
    offset_time = next( hold for hold in count() if not \
        any(check_severity((hold + layer), firewall[layer]) == 0 for layer in firewall) )
    print( "The offset to move uncaught is {0}.".format(offset_time) )
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
