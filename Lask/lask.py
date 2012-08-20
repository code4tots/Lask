'''
Created on Aug 19, 2012

@author: math4tots
'''
from functions import baseDict
from executor import Context, ex
from lexer import lex
from parser import parse


def lask(s): return ex(Context(None,baseDict),parse(lex(s)))

def lask_with_exit_code(s):
    ret = lask(s)
    try: return int(ret)
    except: return -1

def main():
    from sys import argv, exit, stdin
    
    if len(argv) == 1:
        exit(lask_with_exit_code(stdin.read()))
    else:
        exit(lask_with_exit_code(open(argv[1],'r')))
        
if __name__ == '__main__': main()