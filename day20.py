'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day20.py
Purpose:    Advent of Code 2017, day 20
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from collections import defaultdict
import math
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

class Particle:
    '''
    Default constructor.
    :modifies:  self._p, self._v, self._a, self._dist
    :effects:   initializes all values.
    '''
    def __init__(self, pos=[0, 0, 0], vel=[0, 0, 0], acc=[0, 0, 0]):
        self._p = pos
        self._v = vel
        self._a = acc
        self._dist = sum( abs(x) for x in self._p )


    # ----------------------------------------------------------
    # Modifiers

    '''
    Step method.
    :modifies:  self._v, self._p, self._dist
    :effects:   applies position and velocity changes.
    '''
    def step(self):
        for i in range(3):
            self._v[i] += self._a[i]
            self._p[i] += self._v[i]
        self._dist = sum( abs(x) for x in self._p )
        # self._dist = math.sqrt( sum( x**2 for x in self._p ) )


    # ----------------------------------------------------------
    # Overridden methods

    '''
    Repr representation.
    :return:    raw string of object.
    '''
    def __repr__(self):
        return ( "self._p = [{0}, {1}, {2}], self._v = [{3}, {4}, {5}], \
            self._a = [{6}, {7}, {8}], self._dist = {9}".format(self._p[0], \
            self._p[1], self._p[2], self._v[0], self._v[1], self._v[2], \
            self._a[0], self._a[1], self._a[2], self._dist) )


# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:part:      determines whether or not the string should be split.
:requires:  file 'day20.txt' to exist in 'inputs' subdirectory.
:return:    defaultdict with Particles from input.
:throws:    RuntimeError, if file cannot be opened.
            ValueError, if illegal letter is found in input.
'''
def read_particles():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day20.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day20.txt' could not be opened." )

    particles = defaultdict()
    for i, line in enumerate(f):
        line = line.strip().split(", ")
        try:
            p = [ int(x) for x in line[0].split('=')[1][1 : -1].split(',') ]
            v = [ int(x) for x in line[1].split('=')[1][1 : -1].split(',') ]
            a = [ int(x) for x in line[2].split('=')[1][1 : -1].split(',') ]
        except ValueError:
            raise ValueError( "Illegal value found for position, velocity, or \
                acceleration." )

        particles[i] = Particle(p, v, a)

    f.close()
    return particles


'''
Simulation.
:param:     particles, defaultdict with Particles from input.
:return:    key of Particle with distance closest to zero.
:modifies:  particles
:effects:   applies step() function to each particle.
'''
def find_closest(particles):
    for val in range(10000):
        min_part, min_dist = None, None
        for i, part in particles.items():
            part.step()
            if ( (min_dist == None) or (part._dist < min_dist) ):
                min_part = i
                min_dist = part._dist

    return min_part


'''
Simulation for collisions.
:param:     particles, defaultdict with Particles from input.
:return:    count number of particles not removed.
:modifies:  particles
:effects:   applies step() function to each particle.
'''
def count_remaining(particles):
    for val in range(10000):
        min_part, min_dist = None, None
        for i, part in particles.items():
            part.step()
            if ( (min_dist == None) or (part._dist < min_dist) ):
                min_part = i
                min_dist = part._dist

        positions = defaultdict( list )
        for i, part in particles.items():
            tup = tuple( part._p )
            positions[tup].append( i )

        for key, val in positions.items():
            if ( len(val) > 1 ):
                for i in val:    del particles[i]

    return len(particles)


'''
Run methods associated with part 'a'.
'''
def part_a():
    particles = read_particles()
    closest = find_closest(particles)
    print( "The particle closest to zero is number {0}.".format(closest) )
    return 0


'''
Run methods associated with part 'b'.
'''
def part_b():
    particles = read_particles()
    remaining = count_remaining(particles)
    print( "There are {0} remaining particles.".format(remaining) )
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
