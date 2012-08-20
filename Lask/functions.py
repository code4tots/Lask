'''
Created on Aug 19, 2012

@author: math4tots
'''
from executor import ex, Context

def WrappedFunction(f):
    def r(context,*args): return f(*[ex(context,arg) for arg in args])
    return r

def PrintFunction(arg):
    print(arg)
    return arg

def LambdaFunction(context,argNames,expr):
    def user_defined_function(*args):
        tmp_context = Context(context)
        
        argIterator = args.__iter__()
        for name in argNames:
            tmp_context[name] = argIterator.next()
            
        return ex(tmp_context,expr)
    
    return WrappedFunction(user_defined_function)

def IfFunction(context,condition,branch1,branch2):
    if ex(context,condition): return ex(context,branch1)
    else: return ex(context,branch2)
    
def ForFunction(context,iter_var,in_keyword,collection,expr):
    assert in_keyword == 'in', 'expected "in" keyword'
    return [ ex(context.quickAssign(iter_var,x),expr) for x in ex(context,collection) ]
            
def WhileFunction(context,condition,expr):
    ret = None
    while ex(context,condition): ret = ex(context,expr)
    return ret

def DoFunction(*args):
    return args[-1]

def LetFunction(context,var_name, be_keyword, value):
    assert be_keyword == 'be', 'expected "be" keyword'
    context[var_name] = ex(context,value)
    return context[var_name]



from operator import add, sub, mul, div, eq, ne, ge, gt, le, lt


baseDict = {
    # Functions inherited from Python.
    '+': WrappedFunction(add),
    '-': WrappedFunction(sub),
    '*': WrappedFunction(mul),
    '/': WrappedFunction(div),
    '==': WrappedFunction(eq),
    '!=': WrappedFunction(ne),
    '>=': WrappedFunction(ge),
    '>': WrappedFunction(gt),
    '<=': WrappedFunction(le),
    '<': WrappedFunction(lt),
    'print': WrappedFunction(PrintFunction),
    'input': WrappedFunction(raw_input),
    'range': WrappedFunction(range),
    
    # Wrapped Functions tailored for our programming language.
    'do': WrappedFunction(DoFunction),
    
    # Other Functions tailored for our programming language.
    'lambda': LambdaFunction,
    'if': IfFunction,
    'for': ForFunction,
    'while': WhileFunction,
    'let': LetFunction,
}

