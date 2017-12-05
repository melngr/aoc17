'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day03.py
Purpose:    Advent of Code, day 3
'''

import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day05-input.txt' exist in directory.
:return:    list of ints will all values for input file.
:throws:    IOError, if file cannot be opened.
            ValueError, if file contains illegal letter.
'''
def read_instructions():
    try:
        f = open( "day05-input.txt", 'r' )
        instructions = []
        for line in f:
            try:
                instructions.append( int(line.strip()) )
            except ValueError:
                raise ValueError( "Illegal letter found in file." )

    except IOError:
        raise IOError( "Input file 'day05-input.txt' could not be opened." )

    return instructions


'''
Instruction tracking method for part 'a'.
:param:     instructions, list of ints with instructions to follow.
:requires:  instructions != None
:return:    number of steps taken to exit list
:throws:    IndexError, if list cannot be parsed.
'''
def follow_plain(instructions):
    steps = 0
    i = 0
    try:
        while i in range(0, len(instructions)):
            val = instructions[i]
            instructions[i] += 1
            i += val
            steps += 1

    except IndexError as err:
        raise IndexError( err )

    return steps


'''
Instruction tracking method for part 'b'.
:param:     instructions, list of ints with instructions to follow.
:requires:  instructions != None
:return:    number of steps taken to exit list
:throws:    IndexError, if list cannot be parsed.
'''
def follow_strange(instructions):
    steps = 0
    i = 0
    try:
        while i in range(0, len(instructions)):
            val = instructions[i]
            if ( val >= 3 ):
                instructions[i] -= 1
            else:
                instructions[i] += 1
            i += val
            steps += 1

    except IndexError as err:
        raise IndexError( err )

    return steps


'''
Run methods associated with part 'a'.
'''
def part_a():
    instructions = read_instructions()
    steps = follow_plain(instructions)
    print( "It takes {0} steps to exit the maze.".format(steps) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    instructions = read_instructions()
    steps = follow_strange(instructions)
    print( "It takes {0} steps to exit the maze.".format(steps) )


# --------------------------------------------------------------
# --------------------------------------------------------------

if ( __name__ == "__main__" ):

    if ( len(sys.argv) != 2 ):
        if ( len(sys.argv) < 2 ):
            raise IndexError( "USAGE => too few args" )
        else:
            raise IndexError( "USAGE => too many args" )

    else:
        part = sys.argv[1]
        if ( part.strip() == 'a' ):
            part_a()
        elif ( part.strip() == 'b' ):
            part_b()
        else:
            raise RuntimeError( "USAGE => invalid argument" )
