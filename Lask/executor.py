'''
Created on Aug 19, 2012

@author: math4tots
'''
from lexer import Token

def ex(context,s):
    if isinstance(s,Token): return context[s]
    elif isinstance(s,str): return s
    elif isinstance(s,list): return ex(context,s[0])(context,*s[1:])
    
class Context(object):
    def __init__(self,parent=None,d={}):
        self.parent = parent
        self.d = d
        
    def __getitem__(self,key):
        try: return int(key)
        except:
            try: return float(key)
            except: pass
        if key in self.d: return self.d[key]
        elif self.parent != None: return self.parent[key]
        
    def __setitem__(self,key,value): self.d[key] = value
        
    def recursive_set_item(self,key,value):
        if key in self.d: self.d[key] = value
        elif self.parent != None and key in self.parent: self.parent[key] = value
        else: self.d[key] = value
        
    def __contains__(self,key):
        return key in self.d or (self.parent != None and key in self.parent)
    
    # Just so my ForFunction implementation can look nice.
    def quickAssign(self,key,value):
        self[key] = value
        return self
