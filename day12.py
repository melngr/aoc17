'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day11.py
Purpose:    Advent of Code 2017, day 11
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import networkx as nx
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:part:      determines whether or not the string should be split.
:requires:  file 'day12.txt' to exist in 'inputs' subdirectory.
:return:    dictionay with nodes mapped to direct connections.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if illegal letter is found in file.
'''
def read_pipes():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day12.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day12.txt' could not be opened." )
        return 1

    pipes = {}
    for line in f:
        line = line.strip().split("<->")
        pipes[ line[0].strip() ] = set( [ x.strip() for x in line[1].split(',') ] )

    f.close()
    return pipes


'''
Graph building method.
:param:     pipes, dictionary with nodes mapped to connections.
:return:    NetworkX DiGraph built using info from the passed dictionary.
'''
def build_graph(pipes):
    graph = nx.DiGraph()
    for key in pipes:
        graph.add_edges_from( [ (key, connect) for connect in pipes[key] ] )
    return graph

'''
Counts number of nodes with connections to '0'.
:param:     graph, NetworkX DiGraph.
:requires:  '0' in graph.nodes()
:return:    number of nodes with connections to '0'.
:throws:    RuntimeError, if '0' node does not exist in graph.
'''
def count_connects(graph):
    if ( '0' in graph.nodes() ):
        return sum([ nx.has_path( graph, node, '0' ) for node in graph.nodes() ])

    else:
        raise RuntimeError( "Necessary source node '0' not found." )
        return 1


'''
Counts number of groups of nodes in graph.
:param:     graph, NetworkX DiGraph.
:return:    number of groups found.
'''
def count_groups(graph):
    return len( list(nx.strongly_connected_component_subgraphs(graph)) )


'''
Run methods associated with part 'a'.
'''
def part_a():
    pipes = read_pipes()
    graph = build_graph(pipes)
    count = count_connects(graph)
    print( "{0} nodes have connections back to node '0'.".format(count) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    pipes = read_pipes()
    graph = build_graph(pipes)
    count = count_groups(graph)
    print( "There are {0} groups of nodes.".format(count) )
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
