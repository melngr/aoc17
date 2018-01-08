'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day17.py
Purpose:    Advent of Code 2017, day 17
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day17.txt' to exist in 'inputs' subdirectory.
:return:    step value taken from input file.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, is letter found as step value.
'''
def read_step():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day17.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day17.txt' could not be opened." )
        return 1

    try:
        step = int( f.readline().strip() )
    except ValueError:
        raise ValueError( "Illegal letter found as number." )

    f.close()
    return step


'''
Spinlock simulation.
:param:     step, step value taken from input file.
            moment, number of values to add to buffer.
:return:    list of numbers after spinlock.
'''
def gen_spinlock(step, moment):
    c_buffer = [0]
    curr = 0
    for i in range(1, (moment + 1)):
        pos = (curr + step) % len(c_buffer)
        c_buffer.insert( (pos + 1), i )
        curr = pos + 1

    return c_buffer


'''
Track value immediately following '0'.
:param:     step, step value taken from input file.
            moment, number of values to add to buffer.
:return:    final value tracked after zero.
'''
def track_zero(step, moment):
    final, curr = 0, 0
    for i in range(1, (moment + 1)):
        pos = (curr + step) % i
        if ( pos == 0 ):
            final = i
        curr = pos + 1

    return final


'''
Find value after '2017'.
:param:     c_buffer, list of numbers after spinlock.
'''
def find_post_17(c_buffer):
    return c_buffer[ (c_buffer.index(2017) + 1) ]


'''
Run methods associated with part 'a'.
'''
def part_a():
    step = read_step()
    c_buffer = gen_spinlock(step, 2017)
    post = find_post_17(c_buffer)
    print( "The value immediately succeeding '2017' is {0}.".format(post) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    step = read_step()
    post = track_zero(step, 50000000)
    print( "The value immediately succeeding '0' is {0}.".format(post) )
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
