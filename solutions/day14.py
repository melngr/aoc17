'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day14.py
Purpose:    Advent of Code 2017, day 14
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import day10
import networkx as nx
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day14.txt' to exist in 'inputs' subdirectory.
:return:    string with key from input file.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_key():
    pwd, input_file = os.path.dirname( __file__ ), "../inputs/day14.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day14.txt' could not be opened." )
        return 1

    key = f.readline().strip()

    f.close()
    return key


'''
Hashing method that gives binary representation of hashes.
:param:     key, key string on which to base the knot hash.
:return:    list with 128, 128-bit binary representations of hashes.
'''
def hash(key):
    hashed_grid = []
    for i in range(128):
        hash_key = [ ord(char) for char in "{0}-{1}".format(key, i) ] \
            + [17, 31, 73, 47, 23]
        row = list( range(256) )
        curr, skip = 0, 0
        for _ in range(64):
            row, curr, skip = day10.knot_hash(hash_key, row, curr, skip)

        dense = day10.dense_hash( row )
        hex_rep = day10.hex_dense( dense )
        line = []
        for x in hex_rep:
            line.extend( [ int(x) for x in "{:04b}".format( int(x, 16) ) ] )
        hashed_grid.append( line )

    return hashed_grid


'''
Counts filled squares in knot hashed strings.
:param:     hashed_grid, grid with binary hashes.
:return:    sum count of 1's in hashes.
'''
def count_filled(hashed_grid):
    filled = 0
    for row in hashed_grid:
        filled += row.count(1)

    return filled


'''
Creates NetworkX Graph using hash.
:param:     hashed_grid, grid with binary hashes.
:return:    NetworkX Graph with node and edges based from hash.
'''
def make_graph(hashed_grid):
    graph = nx.Graph()
    for i in range(128):
        for j in range(128):
            if ( hashed_grid[i][j] ):
                graph.add_node( (i, j) )

    for i in range(128):
        for j in range(128):
            if ( i > 0 ):
                if ( hashed_grid[i][j] and hashed_grid[i - 1][j] ):
                    graph.add_edge( (i, j), (i - 1, j) )
            if ( j > 0 ):
                if ( hashed_grid[i][j] and hashed_grid[i][j - 1] ):
                    graph.add_edge( (i, j), (i, j - 1) )

    return graph


'''
Connected component count of graph.
:param:     graph, NetworkX Graph built from hash.
:return:    number of connected components in graph.
'''
def count_groups(graph):
    return nx.number_connected_components(graph)


'''
Run methods associated with part 'a'.
'''
def part_a():
    key = read_key()
    hashed_grid = hash(key)
    filled = count_filled(hashed_grid)
    print( "There are {0} filled squares.".format(filled) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    key = read_key()
    hashed_grid = hash(key)
    graph = make_graph(hashed_grid)
    groups = count_groups(graph)
    print( "There are {0} groups of filled squares.".format(groups) )
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
