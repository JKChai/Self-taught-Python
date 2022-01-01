##
## Show another way of rewriting class object using __class__ operator overloading calling the constructor again
## this is a coding mechanics of Python found from property python equivalence code

import os
import sys

## add path
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'src'))

class tryClass:
    def __init__(self, arg1=None, arg2= None):
        self.arg = arg1
        self.arg2 = arg2
    def tryMethod(self, argM):
        prop = type(self)(self.arg, argM)
        return prop

tryInstance = tryClass()

# object stored in different memory, think of class as instances factory
print(tryInstance.tryMethod('Try it'), tryInstance.__class__(arg1=None, arg2='Try it'))

# both should return the same code
print(tryInstance.tryMethod('Try it').arg2, tryInstance.__class__(arg1=None, arg2='Try it').arg2)