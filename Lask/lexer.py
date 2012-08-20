'''
Created on Aug 19, 2012

You might be able to tell from this header that I use Eclipse with PyDev.

I'd appreciate comments, feedback, reasons why my code/explanations sucks, why they're awesome, etc:
 

@author: math4tots
'''

'''
My Token class is practically identical to normal Python strings
except that "isinstance(token,Token)" returns True if token is
a Token instance. I use it to distinguish string literals
from everything else.
'''
class Token(str): pass


def lex(s):
    '''
    findall finds all substrings that match a specific (regex) pattern within a string.
    sub finds and substitutes all substrings that match a specific (regex) with something else.
    '''
    from re import findall, sub
    
    '''
    I decided I wanted to figure out all the regexes I need here.
    Notice that all strings literals matched here are raw --
    it's like prepending a Python string with an r. 
    '''
    string_literal_pattern = r'''\'[^']\'|\"[^"]\"'''
    literal_place_holder = '#'
    special_character_pattern = r'''(\(|\))'''
    
    '''
    I save all the string literals somewhere safe.
    '''
    literals = findall(string_literal_pattern, s)
    
    '''
    Now I replace all the string literals with a place holder. This way
    I can play with the string without messing up the literals.
    '''
    s = sub(string_literal_pattern, ' ' + literal_place_holder + ' ', s)
    
    '''
    Even though in general, I want to delimit tokens using whitespace,
    I want some characters to be tokens by themselves regardless.
    In this case, parentheses.
    If I didn't do this, 'abc(xyz x)' would get lexed as ['abc(xyz','x)'],
    when what we probably wanted was ['abc','(','xyz','x',')'] 
    '''
    s = sub(special_character_pattern, r' \1 ', s)
    
    '''
    Now cut stuff up around whitespace!!
    '''
    s = s.split()
    
    '''
    I also want to mark everything as a Token before I put the string literals back in.
    This way, the token 'var_name' can be distinguished from a string containing 'var_name'
    '''
    s = [ Token(c) for c in s ]
    
    '''
    Now put back the string literals in the order we found them.
    Note that we can't use literal_place_holder within our code because it
    would screw up our lexing mechanism. Hmm.
    '''
    literal_iterator = literals.__iter__()
    s = [literal_iterator.next() if c == literal_place_holder else c for c in s]
    
    return s
