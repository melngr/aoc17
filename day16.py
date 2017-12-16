'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day16.py
Purpose:    Advent of Code 2017, day 16
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

memo = {}

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day16.txt' to exist in 'inputs' subdirectory.
:return:    list of dance moves from input.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_dance():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day16.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day16.txt' could not be opened." )
        return 1

    dance = f.readline().strip().split(',')

    f.close()
    return dance


'''
Program list building method.
:return:    list of letters from 'a' to 'p'.
'''
def gen_programs():
    return ''.join( [ chr(i) for i in range(97, 113) ] )


'''
Dance simulation method.
:param:     dance, list of dance moves from input.
            letters, list of letters from 'a' to 'p'.
:return:    final position of all letters after dance.
:throws:    RuntimeError, if illegal instruction is found in dance.
            ValueError, if location in instruction is not numeric.
:modifies:  letters
:effects:   applies dance to letters.
'''
def sim_dance(dance, letters):
    if ( letters in memo.keys() ):
        return memo[letters]

    else:
        start, letters = letters, list( letters )
        for move in dance:
            if ( move[0] == 's' ):
                try:
                    sub_len = int( move[ 1: ] )
                except ValueError:
                    raise ValueError( "Illegal letter in list location." )

                letters = letters[ -sub_len: ] + letters[ :-sub_len ]

            elif ( move[0] == 'x' ):
                locs = move[ 1: ].split('/')
                try:
                    loc1, loc2 = int( locs[0] ), int( locs[1] )
                except ValueError:
                    raise ValueError( "Illegal letter in list location." )

                letters[loc1], letters[loc2] = letters[loc2], letters[loc1]

            elif ( move[0] == 'p' ):
                progs = move[ 1: ].split('/')
                loc1, loc2 = letters.index(progs[0]), letters.index(progs[1])
                letters[loc1], letters[loc2] = letters[loc2], letters[loc1]

            else:
                raise RuntimeError( "Illegal instruction in dance moves." )

    memo[start] = ''.join( [ letter for letter in letters ] )
    return memo[start]


'''
Run methods associated with part 'a'.
'''
def part_a():
    dance = read_dance()
    programs = gen_programs()
    final = sim_dance(dance, programs)
    print( "The final string after dance is {0}.".format(final) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    dance = read_dance()
    programs = gen_programs()
    final = sim_dance(dance, programs)
    for _ in range(999999999):
        final = sim_dance(dance, final)
    print( "The final string after a billion dances is {0}.".format(final) )
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
