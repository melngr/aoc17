'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day01.py
Purpose:    Advent of Code 2017, Day 1
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader.
:requires:  file 'captcha.txt' to exist in same directory
:throws:    IOError, if file cannot be opened
:returns:   all info from 'captcha.txt' as a string
'''
def read_captcha():
    try:
        f = open("captcha.txt", 'r')
        captcha = f.read().strip()
        f.close()
    except IOError as err:
        raise IOError( err )

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
        if ( i != (len(captcha) - 1) ):
            j = i + 1
        else:
            j = 0

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

# --------------------------------------------------------------

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

if __name__ == "__main__":
    if ( len(sys.argv) == 2 ):
        day = sys.argv[1]
        if ( day.strip() == 'a' ):
            part_a()

        elif ( day.strip() == 'b' ):
            part_b()

        else:
            sys.stderr.write( "USAGE: invalid argument" )

    else:
        if ( len(sys.argv) < 2 ):
            sys.stderr.write( "USAGE: too few args" )
        else:
            sys.stderr.write( "USAGE: too many args" )
