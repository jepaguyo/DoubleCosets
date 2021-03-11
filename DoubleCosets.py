# Double Cosets CLT

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

k = 3
n = 6
b1 = list(range(1,k+1))
b2 = list(range(k+1,n))
Sn = sorted(list(permutations(range(1,n))))
#size = len(Sn)
#print(size)

descentlist = []
matrixlist = []


for sigma in Sn:
    print(sigma)
    #descentlist.append(descentnum(sigma))
    #print(descentnum(sigma))
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
    #print(kblock)
    #print(nkblock)
    T11 = len(T11block)
    T12 = len(T12block)
    T21 = len(T21block)
    T22 = len(T22block)
    T = [[T11, T12], [T21, T22]]
    if T not in matrixlist:
        matrixlist.append(T)
    print(np.matrix(T))
    print(descentnum(sigma))

for A in matrixlist:
   print(np.matrix(A))





    


