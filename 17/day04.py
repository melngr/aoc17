'''
Author:     Griffin Melnick, melnick.griffin@gmail.com
File:       day04.py
Purpose:    Advent of Code, day 4
'''

from collections import Counter
import itertools
import sys

# --------------------------------------------------------------
# --------------------------------------------------------------

'''
File reader method.
:requires:  file 'day04-input.txt' to be in directory.
:return:    list of list with all lines from source.
:throws:    IOError, if file cannot be opened.
'''
def read_file():
    try:
        f = open( "day04-input.txt", 'r' )
        phrases = []
        for line in f:
            words = line.strip().split(' ')
            phrases.append( words )

    except IOError as err:
        raise IOError( err )

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
            raise IndexError( "USAGE => too few args" )
        else:
            raise IndexError( "USAGE => too many args" )

    else:
        part = sys.argv[1]
        if ( part.strip() == 'a' ):
            part_a()
        elif ( part.strip() == 'b' ):
            part_b()
        else:
            raise RuntimeError( "USAGE => invalid argument" )
