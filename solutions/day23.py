'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day23.py
Purpose:    Advent of Code 2017, day 23
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from collections import defaultdict
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

class Registers:

    # ----------------------------------------------------------
    # Constructors

    '''
    Default constructor.
    :modifies:  self._store
    :effects:   initializes defaultdict.
    '''
    def __init__(self):
        self._store = defaultdict( int )


    # ----------------------------------------------------------
    # Modifiers

    '''
    Add method (equal to set, but used to improve readability).
    :param:     key, dictionary key.
                val, int used as value of key.
    :throws:    ValueError, if letter is passed as val.
    :modifies:  self._store
    :effects:   adds dictionary pair of 'key: val'.
    '''
    def add(self, key, val=0):
        try:
            self._store[key] = int( val )
        except ValueError:
            raise ValueError( "Illegal letter assigned for register value." )


    '''
    Set method (equal to add, but used to improve readability).
    :param:     key, dictionary key.
                val, int used as value of key.
    :requires:  key in self._store.keys()
    :throws:    ValueError, if letter is passed as val.
    :modifies:  self._store
    :effects:   sets dictionary pair of 'key: val'.
    '''
    def set(self, key, val):
        try:
            self._store[key] = int( val )
        except ValueError:
            raise ValueError( "Illegal letter assigned for register value." )


    # ----------------------------------------------------------
    # Accessors

    '''
    Get method used to determine whether to use int of existing value.
    :param:     key, int to convert or pull from self._store.
    :return:    int of key if no error, or value of key if error.
    '''
    def get(self, key):
        try:
            return int( key )
        except ValueError:
            return self._store[key]


    # ----------------------------------------------------------
    # Overridden methods

    '''
    String representation.
    :return:    alphabetical String of all key-value pairs on new lines.
    '''
    def __str__(self):
        str_rep = ""
        for key in sorted( self._store.keys() ):
            str_rep += "{0}: {1}\n".format( key, self._store[key] )

        return str_rep[ :-1 ]


    '''
    Repr representation.
    :return:    raw alphabetical String of defaultdict.
    '''
    def __repr__(self):
        repr_rep = "defaultdict(<type 'int'>, {"
        for key in sorted( self._store.keys() ):
            repr_rep += "'{0}': {1}, ".format( key, self._store[key] )

        return repr_rep[ :-2 ] + "})"


# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day23.txt' to exist in 'inputs' subdirectory.
:return:    list of lists with instructions in input file.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_instructions():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day23.txt"
    path = os.path.join( pwd, input_file )

    try:    f = open( path, 'r' )
    except: raise RuntimeError( "Input file 'day23.txt' could not be opened." )

    instructions = []
    for line in f:
        instructions.append( [ block.strip() for block in line.strip().split() ] )

    f.close()
    return instructions


'''
Instruction simulation method.
:param:     regs, Registers object holding value of each register.
            instructions, list of lists with instructions in input file.
:return:    count of times 'mul' is called.
:throws:    RuntimeError, if illegal instruction is called.
:modifies:  regs._store
:effects:   applies instructions to shallow copy.
'''
def sim(regs, instructions):
    count = 0
    store = regs._store

    i = 0
    while 0 <= i < len( instructions ):
        instr = instructions[i]

        if ( instr[0] == "set" ):   store[ instr[1] ] = regs.get( instr[2] )
        elif ( instr[0] == "sub" ): store[ instr[1] ] -= regs.get( instr[2] )

        elif ( instr[0] == "mul" ):
            store[ instr[1] ] *= regs.get( instr[2] )
            count += 1

        elif ( instr[0] == "jnz" ):
            if ( regs.get( instr[1] ) != 0 ):
                i += regs.get( instr[2] )
                continue

        else:   raise RuntimeError( "Illegal instruction found." )
        i += 1

    return count


'''
Fancy way to find value of 'h'.
:return:    value of 'h' based on composites.
'''
def find_h():
    h = 0
    for x in range( 107900, (124900 + 1), 17 ):
        for i in range(2, x):
            if ( x % i == 0 ):
                h += 1
                break

    return h

'''
Run methods associated with part 'a'.
'''
def part_a():
    instructions = read_instructions()
    regs = Registers()
    for instr in instructions:
        if ( instr[1].isalpha() ):  regs.add( instr[1] )

    mul_count = sim(regs, instructions, 'a')
    print( "'mul' is called {0} times.".format(mul_count) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    h = find_h()
    print( "The value of register 'h' is {0}.".format(h) )
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
