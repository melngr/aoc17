'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day01.py
Purpose:    Advent of Code 2017, Day 1
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader.
:requires:  file 'day01.txt' to exist in 'inputs' subdirectory.
:returns:   all info from 'day01.txt' as a string.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_captcha():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day01.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day01.txt' could not be opened." )

    captcha = f.read().strip()
    f.close()

    return captcha


'''
Next step summing method.
:param:     captcha, the string read in using method 'read_captcha()'
:throws:    IndexError, if attempt to access value is outside of list
:returns:   sum using method defined in part 'a'
'''
def next_sum(captcha):
    total = 0

    for i in range(0, len(captcha)):
        j = ( i + 1 ) % len( captcha )

        try:
            at_i = captcha[i]
            at_j = captcha[j]
        except IndexError as err:
            raise IndexError( err )

        if ( at_i == at_j ):
            total += int(at_i)

    return total


'''
Half circle summing method.
:param:     captcha, the string read in using method 'read_captcha()'
:throws:    IndexError, if attempt to access value is outside of list
:returns:   sum using method defined in part 'b'
'''
def half_sum(captcha):
    total = 0
    full = len(captcha)
    half = int(full / 2)

    for i in range(0, full):
        j = ((i + half) % full)

        try:
            at_i = captcha[i]
            at_j = captcha[j]
        except IndexError as err:
            raise IndexError( err )

        if ( at_i == at_j ):
            total += int(at_i)

    return total


'''
Runs part 'a' appropriate functions and prints result.
'''
def part_a():
    captcha = read_captcha()
    total = next_sum(captcha)
    print( "The CAPTCHA sum is {0}.".format(total) )


'''
Runs part 'b' appropriate functions and prints result.
'''
def part_b():
    captcha = read_captcha()
    total = half_sum(captcha)
    print( "The CAPTCHA sum is {0}.".format(total) )

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
