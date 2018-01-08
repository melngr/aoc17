'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day22.py
Purpose:    Advent of Code 2017, day 22
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from collections import defaultdict
import os
import sys

statuses = { 0: 'c', 1: 'w', 2: 'i', 3: 'f' }
to_left = { (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1) }
to_right = { val: key for key, val in to_left.items() }

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day22.txt' to exist in 'inputs' subdirectory.
:return:    list of lists with grid definitions from input.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_data():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day22.txt"
    path = os.path.join( pwd, input_file )

    try:    f = open( path, 'r' )
    except: raise RuntimeError( "Input file 'day22.txt' could not be opened." )

    data = [ list( line.strip() ) for line in f ]

    f.close()
    return data


'''
Grid initialization.
:param:     data, list of lists with grid definitions from input.
:return:    deaultdict with grid definitions.
'''
def init_grid(data):
    grid = defaultdict( int )
    rows, cols = len( data ), len( data[0] )
    for row in range( rows ):
        for col in range( cols ):
            grid[ ( (row - rows // 2), (col - cols // 2) ) ] = \
                ( int(data[row][col] == '#') * 2 )

    return grid


'''
Infection simulating method with clean and infected.
:param:     grid, deaultdict with grid definitions.
:return:    count of bursts resulting in infected nodes.
:throws:    RuntimeError, if illegal cell status found in grid.
'''
def simple_infection(grid):
    count = 0
    curr_pos, curr_dir = (0, 0), (-1, 0)
    for _ in range(10000):
        if ( statuses[ grid[curr_pos] ] == 'c' ):
            curr_dir = to_left[ curr_dir ]
            count += 1
        elif ( statuses[ grid[curr_pos] == 'i'] ):
            curr_dir = to_right[ curr_dir ]
        else:
            raise RuntimeError( "Illegal status found for node." )

        grid[curr_pos] = ( grid[curr_pos] + 2 ) % 4
        curr_pos = ( curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1] )

    return count


'''
Infection simulating method with clean, weakened, infected, and flagged.
:param:     grid, deaultdict with grid definitions.
:return:    count of bursts resulting in infected nodes.
:throws:    RuntimeError, if illegal cell status found in grid.
'''
def complex_infection(grid):
    count = 0
    curr_pos, curr_dir = (0, 0), (-1, 0)
    for _ in range(10000000):
        if ( statuses[ grid[curr_pos] ] == 'c' ):
            curr_dir = to_left[ curr_dir ]
        elif ( statuses[ grid[curr_pos] ] == 'w' ):
            count += 1
        elif ( statuses[ grid[curr_pos] ] == 'i' ):
            curr_dir = to_right[ curr_dir ]
        elif ( statuses[ grid[curr_pos] ] == 'f' ):
            curr_dir = to_right[to_right[ curr_dir ]]
        else:
            raise RuntimeError( "Illegal status found for node." )

        grid[curr_pos] = ( grid[curr_pos] + 1 ) % 4
        curr_pos = ( curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1] )

    return count


'''
Run methods associated with part 'a'.
'''
def part_a():
    data = read_data()
    grid = init_grid(data)
    bursts = simple_infection(grid)
    print( "{0} bursts result in an infected node.".format(bursts) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    data = read_data()
    grid = init_grid(data)
    bursts = complex_infection(grid)
    print( "{0} bursts result in an infected node.".format(bursts) )
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
