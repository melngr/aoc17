'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day21.py
Purpose:    Advent of Code 2017, day 21
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from collections import defaultdict
import numpy as np
import os
import sys

orig_pattern = ".#./..#/###"

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
Input parsing helper function.
:param:     string, string representation of grid.
:return:    numpy array representation of grid.
'''
def make_np(square):
    return np.array( [ [pxl == '#' for pxl in line] for line in square.split('/') ] )


'''
File reader method.
:requires:  file 'day21.txt' to exist in 'inputs' subdirectory.
:return:    defaultdict with Particles from input.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_data():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day21.txt"
    path = os.path.join( pwd, input_file )

    try:    f = open( path, 'r' )
    except: raise RuntimeError( "Input file 'day21.txt' could not be opened." )

    maps = defaultdict( np.array )
    for line in f.readlines():
        k, v = map( make_np, line.strip().split(" => ") )
        for arr in ( k, np.fliplr(k) ):
            for rot in range(4):
                maps[np.rot90(arr, rot).tobytes()] = v

    f.close()
    return maps


'''
Grid enhancing method as described in problem.
:param:     grid, numpy array of pixels.
:return:    grid after ehancement.
'''
def enhance(grid, maps):
    size = len(grid)
    div = 2 if ( size % 2 == 0 ) else 3
    assert ( div != None )

    resize = lambda x: x * (div+1) // div
    new_size = resize(size)
    sol = np.empty( (new_size, new_size), dtype = bool )
    squares = range( 0, size, div )
    new_squares = range( 0, new_size, (div+1) )

    for i, ni in zip(squares, new_squares):
        for j, nj in zip(squares, new_squares):
            square = grid[ i:(i+div), j:(j+div) ]
            enhanced = maps[square.tobytes()]
            sol[ni:(ni+div+1), nj:(nj+div+1)] = enhanced

    return sol


'''
Called solving method.
:param:     part, 'a' or 'b' to determine how many iterations to perform.
:return:    pixels in grid.
'''
def solve(part):
    maps = read_data()
    iters = 5 if ( part == 'a' ) else 18
    assert ( iters != None )

    grid = make_np( orig_pattern )
    for _ in range(iters):
        grid = enhance( grid, maps )
    return int( grid.sum() )


'''
Run methods associated with part 'a'.
'''
def part_a():
    pixels = solve('a')
    print( "There are {0} pixels after 5 iterations.".format(pixels) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    pixels = solve('b')
    print( "There are {0} pixels after 18 iterations.".format(pixels) )
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
