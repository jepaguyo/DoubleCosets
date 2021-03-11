# Double Cosets CLT

from __future__ import division

import random
import itertools
import collections
import numpy as np

from itertools import permutations 

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

def descentnum(pi):
    count = 0
    for i in range(0,n-2):
        if pi[i] > pi[i+1]:
            count += 1
    return(count)

def expectedvalue(lst):
    n = len(lst)
    prb = 1/n
    sum = 0
    for i in range(n):
        sum += (lst[i] * prb)
    return(sum)

def secondmoment(lst):
    n = len(lst)
    prb = 1/n
    sum = 0
    for i in range(n):
        sum += ((lst[i]**2) * prb)
    return(sum)

def variance(x, y):
    var = x - (y**2)
    return(var)


k = 4
n = 8
b1 = list(range(1,k+1))
b2 = list(range(k+1,n))
Sn = sorted(list(permutations(range(1,n))))

doublecosets = {}

for sigma in Sn:
    kblock = []
    nkblock = []
    for i in range(0,k):
        kblock.append(sigma[i])
    for i in range(k,n-1):
        nkblock.append(sigma[i])
    T11block = intersection(kblock, b1)
    T12block = intersection(kblock, b2)
    T21block = intersection(nkblock, b1)
    T22block = intersection(nkblock, b2)
    T11 = len(T11block)
    T12 = len(T12block)
    T21 = len(T21block)
    T22 = len(T22block)

    T = ((T11, T12), (T21, T22))

    # sets up dictionary
    if T in doublecosets:
        doublecosets[T].append(descentnum(sigma))
    else:
        doublecosets[T] = [descentnum(sigma)]

#Print out statistics stuff
for T in doublecosets:
    print(T, len(doublecosets[T])) 
    print(expectedvalue(doublecosets[T]), secondmoment(doublecosets[T]), variance(secondmoment(doublecosets[T]), expectedvalue(doublecosets[T])))

print(len(doublecosets))


#place cosets in "bins"
#place descents in respective cosets
#size of coset
#probability mass function 





    


