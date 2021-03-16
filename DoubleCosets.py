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

def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

# Initialize parameters
n = 9

print 'Statistics for descents in fixed cosets of S_n, where n = ', n-1
print '\n'
for k in range(n):
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

    print 'k = ', k
    print 'Number of double cosets', len(doublecosets)
    print '\n'
    for T in doublecosets:
        print 'Double coset: '
        print np.array(T)
        print 'Size: ', len(doublecosets[T])
        print 'Expected value: ', expectedvalue(doublecosets[T]) 
        print 'Variance: ', variance(secondmoment(doublecosets[T]), expectedvalue(doublecosets[T]))
        print 'Histogram for (number of descents, frequency): '
        for i in range(n-1):
            print(i, countX(doublecosets[T], i))
        print '\n'


# b1 = list(range(1,k+1))
# b2 = list(range(k+1,n))
# Sn = sorted(list(permutations(range(1,n))))

# doublecosets = {}

# for sigma in Sn:
#     kblock = []
#     nkblock = []
#     for i in range(0,k):
#         kblock.append(sigma[i])
#     for i in range(k,n-1):
#         nkblock.append(sigma[i])
#     T11block = intersection(kblock, b1)
#     T12block = intersection(kblock, b2)
#     T21block = intersection(nkblock, b1)
#     T22block = intersection(nkblock, b2)
#     T11 = len(T11block)
#     T12 = len(T12block)
#     T21 = len(T21block)
#     T22 = len(T22block)

#     T = ((T11, T12), (T21, T22))

#     # sets up dictionary
#     if T in doublecosets:
#         doublecosets[T].append(descentnum(sigma))
#     else:
#         doublecosets[T] = [descentnum(sigma)]


# #Print out statistics stuff

# print 'n = ', n-1
# print 'k = ', k
# print 'Number of double cosets', len(doublecosets)
# print '\n'
# for T in doublecosets:
#     print 'Double coset: '
#     print np.array(T)
#     print 'Size: ', len(doublecosets[T])
#     print 'Expected value: ', expectedvalue(doublecosets[T]) 
#     print 'Variance: ', variance(secondmoment(doublecosets[T]), expectedvalue(doublecosets[T]))
#     print 'Histogram for (number of descents, frequency): '
#     for i in range(n-1):
#         print(i, countX(doublecosets[T], i))
#     print '\n'


