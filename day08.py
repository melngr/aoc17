'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day08.py
Purpose:    Advent of Code 2017, day 8
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day08-input.txt' to exist in 'inputs' subdirectory.
:return:    list of list with instructions and conditionals.
:throws:    RuntimeError, if file cannot be opened.
            RuntimeError, if illegal operation is called in instructions.
'''
def read_instructions():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day08-input.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day08-input.txt' could not be opened." )

    instructions = []
    registers = {}
    for line in f:
        instructions.append( line.strip() )

        line = line.strip().split()
        registers[ line[0] ], registers[ line[4] ] = 0, 0

    f.close()
    return instructions, registers


'''
Modifying function.
:param:     instructions, list of instructions.
            registers, dictionary of registers mapped to value.
            part, 'a' or 'b' to denote which return value is needed.
:requires:  instructions != None
            registers != None
:return:    highest value among registers / highest value ever in registers.
:modifies:  registers
:effects:   applies instructions to each register.
'''
def modify(instructions, registers, part):
    overall_max = 0
    for inst in instructions:
        reg, op, val, c, c_reg, c_op, c_val = inst.split()
        if ( eval( "registers[c_reg]" + c_op + c_val ) ):
            if ( op == "inc" ):
                registers[reg] += int( val )
                overall_max = max( registers[reg], overall_max )
            elif ( op == "dec" ):
                registers[reg] -= int( val )
            else:
                raise RuntimeError( "Illegal operator." )

    if ( part == 'a' ):
        return max( list(registers.values()) )
    else:
        return overall_max


'''
Run methods associated with part 'a'.
'''
def part_a():
    instructions, registers = read_instructions()
    max_value = modify(instructions, registers, 'a')
    print( "The max value through the registers is {0}.".format( max_value ) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    instructions, registers = read_instructions()
    max_value = modify(instructions, registers, 'b')
    print( "The max value ever through the registers is {0}.".format( max_value ) )


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
