import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day15.txt' to exist in 'inputs' subdirectory.
:return:    two values taken as generator values from file.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if illegal letter is found in file.
'''
def read_file():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day15.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day15.txt' could not be opened." )
        return 1
    try:
        a = int(f.readline().strip().split()[4])
        b = int(f.readline().strip().split()[4])
    except ValueError:
        raise ValueError( "Illegal letter found for generator value." )

    return a, b


'''
'a' generator.
:param:     a, starting value for generator.
            part, part of problem to determine if modulo must be taken.
:modifies:  a
:effects:   applies generator transform.
'''
def gen_a(a, part):
    while True:
        a = (a * 16807) % 2147483647
        if ( part == 'b' ):
            if ( a % 4 == 0 ):
                yield a
        else:
            yield a


'''
'b' generator.
:param:     b, starting value for generator.
            part, part of problem to determine if modulo must be taken.
:modifies:  b
:effects:   applies generator transform.
'''
def gen_b(b, part):
    while True:
        b = (b * 48271) % 2147483647
        if ( part == 'b' ):
            if ( b % 8 == 0 ):
                yield b
        else:
            yield b


'''
Match counting method.
:param:     ag, generator built using 'a' value.
            bg, generator built using 'b' value.
            part, part of problem to decide how many iterations needed.
:return:    count of how many matches occur based on last sixteen bits.
:throws:    RuntimeError, if illegal value passed for part.
'''
def count_matches(ag, bg, part):
    count = 0
    if ( part == 'a' ):
        i = 40000000
    elif ( part == 'b' ):
        i = 5000000
    else:
        raise RuntimeError( "Illegal value for part passed." )

    for _ in range(i):
        a = next( ag )
        b = next( bg )

        #if ( "{0:b}".format(a)[-16:] == "{0:b}".format(b)[-16:] ):
        if ( a & 0xFFFF == b & 0xFFFF ):
            count += 1

    return count


'''
Run methods associated with part 'a'.
'''
def part_a():
    a, b = read_file()
    ag = gen_a(a, 'a')
    bg = gen_b(b, 'a')
    count = count_matches(ag, bg, 'a')
    print( "There are {0} pairs with the last sixteen bits matching.".format(count) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    a, b = read_file()
    ag = gen_a(a, 'b')
    bg = gen_b(b, 'b')
    count = count_matches(ag, bg, 'b')
    print( "There are {0} modulated pairs with the last sixteen bits matching.".format(count) )
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
