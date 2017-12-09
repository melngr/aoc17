'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day02.py
Purpose:    Advent of Code 2017, Day 2
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import itertools
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader.
:requires:  file 'day02-input.txt' to exist in same directory
:throws:    IOError, if file cannot be opened
:returns:   all info from 'day02-input.txt' as a list of lists

def read_spreadsheet():
    try:
        f = open("day02-input.txt", 'r')
        spreadsheet = []
        for line in f:
            spreadsheet.append( line.strip().split(' ') )
        f.close()
    except IOError as err:
        raise IOError( err )

    return spreadsheet'''

'''
File reader.
:requires:  file 'day02-input.txt' to exist in 'inputs' subdirectory.
:returns:   all info from 'day02-input.txt' as a list of lists.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_spreadsheet():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day02-input.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day02-input.txt' could not be opened." )

    spreadsheet = []
    for line in f:
        spreadsheet.append( line.strip().split() )
    f.close()

    return spreadsheet

'''
List conversion from string to int.
:param:     spreadsheet, a list of list with strings
:requires:  spreadsheet != None
:throws:    ValueError, if list has illegal letter
:returns:   new list of list with ints
'''
def convert(spreadsheet):
    try:
        int_spreadsheet = [list(map(int, x)) for x in spreadsheet]
    except ValueError as err:
        raise ValueError( err )

    return int_spreadsheet

'''
Checksum finding method using max and min of each line.
:param:     spreadsheet, a list of lists with ints
:requires:  spreadsheet != None
:returns:   checksum value of spreadsheet using method from part 'a'
'''
def total_checksum(spreadsheet):
    checksum = 0
    for vals in spreadsheet:
        checksum += ( max(vals, default = 0) - min(vals, default = 0) )
    return checksum

'''
Row sum finding method using evenly divisible numbers.
:param:     spreadsheet, a list of lists with ints
:requires:  spreadsheet != None
:returns:   rowsum value of spreadsheet using method from part 'b'
'''
def even_row_sum(spreadsheet):
    row_sum = 0
    for vals in spreadsheet:
        for x, y in itertools.combinations( sorted(vals), 2 ):
            if ( y % x == 0 ):
                row_sum += ( y // x )

    return row_sum

# --------------------------------------------------------------

'''
Runs part 'a' appropriate functions and prints result.
'''
def part_a():
    spreadsheet = convert( read_spreadsheet() )
    sum = total_checksum(spreadsheet)
    print( "The checksum is {0}.".format(sum) )

'''
Runs part 'b' appropriate functions and prints result.
'''
def part_b():
    spreadsheet = convert( read_spreadsheet() )
    sum = even_row_sum(spreadsheet)
    print( "The row sum is {0}.".format(sum) )

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
            sys.stderr.write( "USAGE: invalid argument\n" )

    else:
        if ( len(sys.argv) < 2 ):
            sys.stderr.write( "USAGE: too few args\n" )
        else:
            sys.stderr.write( "USAGE: too many args\n" )
