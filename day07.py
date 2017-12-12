'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day07.py
Purpose:    Advent of Code 2017, day 7
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

import collections
import networkx as nx
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day07.txt' to exist in 'inputs' subdirectory.
:return:    list of strings with bank information.
:throws:    RuntimeError, if file cannot be opened.
'''
def read_info():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day07.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day07.txt' could not be opened." )

    info = []
    for line in f:
        info.append( line.strip() )

    f.close()
    return info


'''
Graph building method.
:param:     info, list of strings with program information.
:requires:  info != None
:return:    dictionary with dicitonaries and nodes.
:throws:    RuntimeError, if info is empty.
            RuntimeError, if node(s) / edge(s) cannot be added to graph.
'''
def build_graph(info):
    if ( len(info) < 1 ):
        raise RuntimeError( "Program information does not exist." )

    graph = nx.DiGraph()
    for line in info:
        data = line.strip().split()
        try:
            graph.add_node( data[0], weight = int(data[1].strip("()")) )
        except:
            raise RuntimeError( "Could not create node." )

        if ( len(data) > 2 ):
            for child in data[3 : ]:
                try:
                    graph.add_edge( data[0], child.strip(',') )
                except:
                    raise RuntimeError(
                        "Could not create edge between parent and child." )

    return graph


'''
Method to find node that unbalances the graph.
:param:     graph, NetworkX DiGraph built using input file.
:requires:  graph != None
:return:    necessary weight of node to rebalance graph.
'''
def find_unbalance(graph):
    node_weights = {}
    for node in reversed( list(nx.topological_sort(graph)) ):
        total = graph.nodes()[node]["weight"]
        counts = collections.Counter( node_weights[child] for child in graph[node] )
        unbalanced = None

        for child in graph[node]:
            if ( len(counts) > 1 and counts[node_weights[child]] == 1 ):
                unbalanced = child
                break

            weight = node_weights[child]
            total += weight

        if unbalanced:
            diff = node_weights[unbalanced] - weight
            return ( graph.nodes()[unbalanced]["weight"] - diff )

        node_weights[node] = total


'''
Run methods associated with part 'a'.
'''
def part_a():
    info = read_info()
    graph = build_graph(info)
    print( "The root node is {0}.".format( list(nx.topological_sort(graph))[0] ) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    info = read_info()
    graph = build_graph(info)
    weight = find_unbalance(nx.freeze(graph))
    print( "The weight needed to rebalance the graph is {0}.".format(weight) )


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
