'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day10.py
Purpose:    Advent of Code 2017, day 10
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:part:      determines whether or not the string should be split.
:requires:  file 'day10.txt' to exist in 'inputs' subdirectory.
:return:    string of groups.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if illegal letter is found in input.
'''
def read_lengths(part):
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day10.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day10.txt' could not be opened." )

    if ( part == 'a' ):
        try:
            lengths = [ int( x ) for x in f.readline().strip().split(',') ]
        except ValueError:
            raise ValueError( "Illegal letter found in input file." )
    else:
        lengths = f.readline().strip()

    f.close()
    return lengths


'''
List generation method.
:return:    list of ints numbered 0 to 255.
'''
def gen_list(n):
    return list( range(n) )


'''
List generation method.
:param:     chars, string from input file.
:return:    list of lengths using ASCII values of input file.
'''
def gen_lengths(chars):
    return ( [ ord(x) for x in chars ] + [17, 31, 73, 47, 23] )


'''
Knot hash function.
:param:     lengths, lengths taken from input file.
            curr, current position in list of numbers.
            skip, skip value.
:return:    modified list of ints.
:modifies:  nums
:effects:   applies cryptographic function to nums using lengths.
'''
def knot_hash(lengths, nums, curr, skip):
    for length in lengths:
        sub = []
        for i in range(length):
            sub.append( nums[ (curr + i) % len(nums) ] )

        sub = sub[ ::-1 ]
        for i in range(length):
            nums[ (curr + i) % len(nums) ] = sub[i]

        curr = (curr + length + skip) % len(nums)
        skip += 1

    return nums, curr, skip


'''
Dense hash method.
:param:     hashed, list of hashed values.
:return:    list with XORed values.
'''
def dense_hash(hashed):
    dense_hash = []
    for i in range(16):
        sub = hashed[ 16*i : 16 * (i+1) ]

        xor = sub[0]
        for j in sub[ 1: ]:
            xor ^= j
        dense_hash.append( xor )
    return dense_hash


'''
Hexadecimal representation of dense hash.
:param:     dense, list of ints after undergoing dense hash.
:return:    concatenated hexadecimal string of ints from dense hash.
'''
def hex_dense(dense):
    return ''.join( [ "{:02x}".format( val ) for val in dense ] )


'''
Run methods associated with part 'a'.
'''
def part_a():
    lengths = read_lengths('a')
    nums = gen_list(256)
    hashed, curr, skip = knot_hash(lengths, nums, 0, 0)
    prod = hashed[0] * hashed[1]
    print( "The product of the first two values of the hash is {0}.".format(prod) )

    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    lengths = gen_lengths( read_lengths('b') )
    nums = gen_list(256)
    curr, skip = 0, 0
    for _ in range(64):
        hashed, curr, skip = knot_hash(lengths, nums, curr, skip)

    dense = dense_hash(hashed)
    hex_rep = hex_dense(dense)
    print( "The hexadecimal string for the knot hash is {0}.".format(hex_rep) )

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
