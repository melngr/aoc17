'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day09.py
Purpose:    Advent of Code 2017, day 9
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day09.txt' to exist in 'inputs' subdirectory.
:return:    string of groups.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_groups():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day09.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day09.txt' could not be opened." )

    groups = f.readline().strip()
    f.close()

    return groups


'''
:param:     groups, strong of data from input file.
            part, 'a' or 'b' to determine return value.
:requires:  groups != None
:return:    total score of all groups.
:throws:    RuntimeError, if groups is no usable.
'''
def score_groups(groups, part):
    if ( len(groups) < 1 ):
        raise RuntimeError( "Input data is not usable." )

    score, depth, g_score = 0, 0, 0
    garbage, skip = False, False
    for char in groups:
        if ( garbage ):
            if ( skip ):
                skip = False
            elif ( char == '!' ):
                skip = True
            elif ( char == '>' ):
                garbage = False
            else:
                g_score += 1
        else:
            if ( char == '{' ):
                depth += 1
            elif ( char == '}' ):
                score += depth
                depth -= 1
            elif ( char == '<' ):
                garbage = True
            else:
                continue

    if ( part == 'a' ):
        return score
    elif ( part == 'b' ):
        return g_score


'''
Run methods associated with part 'a'.
'''
def part_a():
    groups = read_groups()
    score = score_groups(groups, 'a')
    print( "The score of the groups is {0}.".format(score) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    groups = read_groups()
    g_score = score_groups(groups, 'b')
    print( "The number of non-canceled characters is {0}.".format(g_score) )


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
