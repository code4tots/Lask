'''
Created on Aug 19, 2012

@author: math4tots
'''
from lexer import Token

def parse(s):
    stack = [ [] ]
    for c in s:
        if c == '(' and isinstance(c,Token): stack.append([])
        elif c == ')' and isinstance(c,Token): stack[-2].append(stack.pop())
        else: stack[-1].append(c)
    return stack[0]
