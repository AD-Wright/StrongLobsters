## Author: https://stackexchange.com/users/13482588/ironeagle
## The strong lobster numbers are a set where the prime factors of a number
## are all contained within the number, but also at least as many times in the number
## as in the list of primes.

import itertools
from functools import reduce

def isStrongLobster(n):
    # expand the number into subsequences through a binary mask
    r=[]
    N=str(n)
    l=len(N)
    s='0' + repr(l) + 'b'
    for i in range(2**l): # iterate through all possible binary masks
        m=format(i,s)
        t=''
        for j in range(l): # iterate through each character
            if m[j]=='1':
                t+=N[j] # append the corresponding character of n if mask is 1
        r+=[[m,t]] # store the mask used and the resulting subsequence
    # find the prime factors
    A=[]
    for i in range(2,n-1):
        while n%i<1:A+=[str(i)];n//=i

    # OVERRIDE FOR TESTING (manually set prime factors to test the following logic)
##    print(A)
##    A=['5','137','5']
##    print(A)
    # match each prime factor to r, store match locations
    R=[]
    k=0
    for f in A:
        k+=1
        for g in r:
            if f==g[1]:
                R+=[[k,g]] # holds prime factor matched (factor#), mask, subsequence

    # do the check for a normal Lobster Number (has all factors as substrings)
    a=len(A)
    if set() == set(range(1,a+1)) - set([x[0] for x in R]) and a>0:
        # check all combinations of valid solutions for all the factors
        #  create all combinations of the correct length (choosing from the available factor match list)
        for p in itertools.combinations(R,a):
            # check if it is valid (does it contain all the factors?)
            if set() == set(range(1,a+1)) - set([y[0] for y in p]):
                # and the binary mask values for each solution set, is it == 0?
                q=[z[1][0] for z in p] # get all elements in one array
                u=['0']*len(q[0])
                for i in range(len(q[0])): # sort the array by ith bit (all first bits together, etc.)
                    u[i]=[str(v[i]) for v in q]
                for U in u: # for each group of bits
                    V=0
                    for i in range(a): # add them all up
                        V+=int(U[i])
                        if V>1: # if a bit is used more than once in any group
                            return False
                # else (if all bits are used at most once) 
                return True # Hey!  It's a strong Lobster!
    # else not even a normal lobster number
    return False

# Iterate through all possible numbers, print tick mark to show progress
for i in range(2,2147483647):
    if isStrongLobster(i):
        print(i)
    if i%10000==0:
        print(i/10000)

# Python 3 (or at least how I write it) is really not the tool to do this.  It is reasonably fast though.

