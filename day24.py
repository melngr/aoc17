'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day24.py
Purpose:    Advent of Code 2017, day 24
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day24.txt' to exist in 'inputs' subdirectory.
:return:    list of tuples with port types.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if letter found for port type.
'''
def read_ports():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day24.txt"
    path = os.path.join( pwd, input_file )

    try:    f = open( path, 'r' )
    except: raise RuntimeError( "Input file 'day24.txt' could not be opened." )

    ports = []
    for line in f:
        try:
            ports.append( tuple([ int(x) for x in line.strip().split('/') ]) )
        except ValueError:
            raise ValueError( "Illegal letter found in port types." )

    f.close()
    return ports


'''
Bridge building generator.
:param:     bridge, tuple of list to int.
            ports, list of tuples with port types.
'''
def build(bridge, ports):
    available = [ x for x in ports if bridge[1] in x ]
    if ( len(available) == 0 ): yield bridge
    else:
        for x in available:
            c_ports = ports.copy()
            c_ports.remove(x)
            for y in build( (bridge[0] + [x], x[0] if bridge[1] == x[1] else x[1]), c_ports ):
                yield y


'''
Run methods associated with part 'a'.
'''
def part_a():
    ports = read_ports()
    bridge = ([], 0)
    strength = max( map( lambda bridge: sum(x + y for x, y in bridge[0]), build(bridge, ports) ) )
    print( "The strongest bridge has a strength of {0}.".format(strength) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    ports = read_ports()
    bridge = ([], 0)

    length = max( map( lambda bridge: len(bridge[0]), build(bridge, ports) ) )
    longest = filter( lambda bridge: (len(bridge[0]) == length), build(bridge, ports) )
    strength = max( map( lambda bridge: sum(x + y for x, y in bridge[0]), longest ) )

    print( "The strongest, longest bridge has a strength of {0}.".format(strength) )
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
