'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day04.py
Purpose:    Advent of Code 2017, day 4
            Pulls in command line input of 'a' or 'b' to represent which set of
            functions to call based on part.
'''

from collections import Counter
import itertools
import os
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day04.txt' to be in directory.
:return:    list of list with all lines from source.
:throws:    IOError, if file cannot be opened.
'''
def read_file():
    pwd, input_file = os.path.dirname( __file__ ), "inputs/day04.txt"
    path = os.path.join( pwd, input_file )

    try:
        f = open( path, 'r' )
    except:
        raise RuntimeError( "Input file 'day04.txt' could not be opened." )

    phrases = []
    for line in f:
        words = line.strip().split(' ')
        phrases.append( words )

    f.close()
    return phrases


'''
Counts number of phrases with no duplicates.
:param:     phrases, list of lists to be analyzed.
:requires:  phrases != None
:return:    counted number of phrases with unique words.
:throws:    IndexError, if phrases cannot be parsed.
'''
def count_no_dups(phrases):
    valid = 0
    try:
        for phrase in phrases:
            if ( len(phrase) == len(set(phrase)) ):
                valid += 1

    except IndexError:
        raise IndexError( "List 'phrases' cannot be parsed." )

    return valid


'''
Counts number of phrases with no anagram duplicates.
:param:     phrases, list of lists to be analyzed.
:requires:  phrases != None
:return:    counted number of phrases with unique words.
:throws:    IndexError, if phrases cannot be parsed.
'''
def count_no_anagrams(phrases):
    valid = 0
    try:
        for phrase in phrases:
            anagram = False
            for w1, w2 in itertools.combinations( phrase, 2 ):
                anagram = ( Counter(w1) == Counter(w2) )
                if ( anagram ):
                    break
            if ( not(anagram) ):
                valid += 1

    except IndexError:
        raise IndexError( "List 'phrases' cannot be parsed." )

    return valid


'''
Run methods associated with part 'a'.
'''
def part_a():
    phrases = read_file()
    valid = count_no_dups( phrases )
    print( "There are {0} valid passphrases.".format( valid ) )


'''
Run methods associated with part 'b'.
'''
def part_b():
    phrases = read_file()
    valid = count_no_anagrams( phrases )
    print( "There are {0} valid passphrases.".format( valid ) )


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
