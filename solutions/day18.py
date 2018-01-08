'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day18.py
Purpose:    Advent of Code 2017, day 18
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from collections import defaultdict, deque
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
:requires:  file 'day18.txt' to exist in 'inputs' subdirectory.
:return:    list of lists with instructions in input file.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_instructions():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day18.txt"
    path = os.path.join( pwd, input_file )

    try:    f = open( path, 'r' )
    except: raise RuntimeError( "Input file 'day18.txt' could not be opened." )

    instructions = []
    for line in f:
        instructions.append( [ block.strip() for block in line.strip().split() ] )

    f.close()
    return instructions


'''
:param:     regs, Registers object holding value of each register.
            instructions, list of lists with instructions in input file.
:return:    value of last sound frequency greater than zero played.
:throws:    RuntimeError, if illegal instruction is called.
:modifies:  regs._store
:effects:   applies instructions to shallow copy.
'''
def sim_instructions(regs, instructions):
    last_snd = 0
    store = regs._store

    i = 0
    while 0 <= i < len( instructions ):
        instr = instructions[i]

        if ( instr[0] == "snd" ):   last_snd = store[ instr[1] ]
        elif ( instr[0] == "set" ): store[ instr[1] ] = regs.get( instr[2] )
        elif ( instr[0] == "add" ): store[ instr[1] ] += regs.get( instr[2] )
        elif ( instr[0] == "mul" ): store[ instr[1] ] *= regs.get( instr[2] )
        elif ( instr[0] == "mod" ): store[ instr[1] ] %= regs.get( instr[2] )

        elif ( instr[0] == "rcv" ):
            if ( regs.get( instr[1] ) != 0 ):
                return last_snd

        elif ( instr[0] == "jgz" ):
            if ( regs.get( instr[1] ) > 0 ):
                i += regs.get( instr[2] )
                continue

        else:   raise RuntimeError( "Illegal instruction found." )
        i += 1

    return 0


'''
:param:     regs, list with Registers.
            instructions, list of lists with instructions in input file.
:return:    number of values sent by program 1.
:modifies:  regs0._store, regs1._store
:effects:   applies concurrent instructions to all shallow copies.
'''
def sim_dual(regs, instructions):
    sent, prog = 0, 0
    stores = { 0: regs[0]._store, 1: regs[1]._store }
    ind, state, queue = { 0: 0, 1: 0 }, { 0: 'g', 1: 'g' }, { 0: deque(), 1: deque() }
    reg, i = stores[ prog ], ind[0]

    while True:
        instr = instructions[i]
        if ( instr[0] == "snd" ):
            if ( prog == 1 ): sent += 1
            queue[prog].append( regs[prog].get(instr[1]) )

        elif ( instr[0] == "set" ): reg[ instr[1] ] = regs[prog].get( instr[2] )
        elif ( instr[0] == "add" ): reg[ instr[1] ] += regs[prog].get( instr[2] )
        elif ( instr[0] == "mul" ): reg[ instr[1] ] *= regs[prog].get( instr[2] )
        elif ( instr[0] == "mod" ): reg[ instr[1] ] %= regs[prog].get( instr[2] )

        elif ( instr[0] == "rcv" ):
            if ( queue[(1 - prog)] ):
                state[prog] = 'g'
                reg[ instr[1] ] = queue[(1 - prog)].popleft()
            else:
                if ( state[(1 - prog)] == 'd' ):
                    break
                if ( (len(queue[prog]) == 0) and (state[(1 - prog)] == 'r') ):
                    break
                
                ind[ prog ], state[ prog ] = i, 'r'
                prog = (1 - prog)
                reg, i = stores[ prog ], ind[ prog ]
                continue

        elif ( instr[0] == "jgz" ):
            if ( regs[prog].get(instr[1]) > 0 ):
                i += regs[prog].get( instr[2] )
                continue

        i += 1
        if ( not 0 <= i < len(instructions) ):
            if state[(1 - prog)] == 'd':
                break

            ind[ prog ], state[ prog ] = i, 'd'
            prog = (1 - prog)
            reg, i = regs[ prog ], ind[ prog ]

    return sent


'''
Run methods associated with part 'a'.
'''
def part_a():
    instructions = read_instructions()
    regs = Registers()
    for instr in instructions:
        if ( instr[1].isalpha() ):  regs.add( instr[1] )

    last_snd = sim_instructions(regs, instructions)
    print( "The last played frequency is {0}.".format(last_snd) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    instructions = read_instructions()
    regs0, regs1 = Registers(), Registers()
    for instr in instructions:
        if ( instr[1].isalpha() ):
            regs0.add( instr[1] )
            regs1.add( instr[1] )
    regs1.set('p', 1)
    regs = { 0: regs0, 1: regs1 }

    sent = sim_dual(regs, instructions)
    print( "Program 1 sends {0} values.".format( sent ) )
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
