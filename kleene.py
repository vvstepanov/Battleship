##################################################################
#
# Kleene logic class library
#
##################################################################

# https://en.wikipedia.org/wiki/Three-valued_logic#Kleene_and_Priest_logics

import numpy as np
from enum import IntEnum, unique

@unique
class kleene(IntEnum) :

    
    # 
    false = 0
    true  = 1
    dunno = 2

    def __str__(self) :
        if self==kleene.false : return 'false'
        if self==kleene.true : return 'true'
        return 'dunno'

    def __repr__(self):
        return f'kleene.{str(self)}'

    def __invert__(self) : # not
        if self==kleene.false : return kleene.true
        if self==kleene.true : return kleene.false
        return kleene.dunno

    def __and__(self,other) :
        if (self==kleene.false) or (other==kleene.false) : return kleene.false
        if (self==kleene.true) and (other==kleene.true) : return kleene.true
        return kleene.dunno

    def __or__(self,other) :
        if self==kleene.true  or other==kleene.true : return kleene.true
        if self==kleene.false and other==kleene.false : return kleene.false
        return kleene.dunno

    def __xor__(self,other) : # is this correct?
        if self==kleene.dunno or other==kleene.dunno : return kleene.dunno
        if self==other : return kleene.false
        return kleene.true

    def negate(self) : # as a method
        if self==kleene.false : return kleene.true
        if self==kleene.true : return kleene.false
        return kleene.dunno

    def c(self) : # colored string
        kolor = ['\x1b[33m\x1b[1m', '\x1b[32m\x1b[1m', '\x1b[37m\x1b[1m', '\x1b[0m']
        return kolor[int(self)] + str(self) + kolor[-1]

    # &=	__IAND__(SELF, OTHER)
    # |=	__IOR__(SELF, OTHER)
    # ^=	__IXOR__(SELF, OTHER)

    # def __bool__(self) :
    #     #return bool(self.value)
    #     if self==kleene.false : return False
    #     if self==kleene.true : return True
    #     return np.nan
    
###################################################################
# testing for the Kleene logic code

'''
a = kleene(0)
a = kleene(False)

b = kleene(1)
b = kleene(True)

c = kleene(2)
c = kleene(kleene.dunno)
#c = kleene()
#c = kleene((0,1))

bool(kleene(0))  # False
bool(kleene(1))  # True
bool(kleene(2))  # True

print(repr(a))
print(repr(b))
print(repr(c))

print(a.c())
print(b.c())
print(c.c())

print(kleene.c(a))
print(kleene.c(b))
print(kleene.c(c))

k = [a,c,b]
print('\nConjunction')
print('\t\t', False, '\t', 'Dunno', '\t', True,sep='')
i = k[0]; print(i, '\t',(i & k[0]).c(), '\t',(i & k[1]).c(), '\t',(i & k[2]).c(), sep='')
i = k[1]; print(i, '\t',(i & k[0]).c(), '\t',(i & k[1]).c(), '\t',(i & k[2]).c(), sep='')
i = k[2]; print(i, '\t',(i & k[0]).c(), '\t',(i & k[1]).c(), '\t',(i & k[2]).c(), sep='')

print('\nDisjunction')
print('\t\t', False, '\t', 'Dunno', '\t', True,sep='')
i = k[0]; print(i, '\t', (i | k[0]).c(), '\t', (i | k[1]).c(), '\t', (i | k[2]).c(), sep='')
i = k[1]; print(i, '\t', (i | k[0]).c(), '\t', (i | k[1]).c(), '\t', (i | k[2]).c(), sep='')
i = k[2]; print(i, '\t', (i | k[0]).c(), '\t', (i | k[1]).c(), '\t', (i | k[2]).c(), sep='')
'''

