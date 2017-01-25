#!/usr/bin/python

#########################################
## CS 3430: S2017: HW01: Euclid Numbers
## Your Name
## Your A-Number
#########################################

import math


def is_prime(n):
    '''is_prime(n) ---> True if n is prime; False otherwise.'''
    # your code here
    if n < 2:
        return False
    if n == 2:
        return True
    for d in xrange(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True
    pass


def next_prime_after(p):
    flag = False
    x = p
    '''computes next prime after prime p; if p is not prime, returns None.'''
    if not is_prime(p): return None
    if is_prime(p):
        for i in xrange(x+1, 2*x):
            if is_prime(i):
                print i
                break
    ## your code here
    pass


def euclid_number(i):
    '''euclid_number(i) --> i-th Euclid number.'''
    if i < 0: return None
    ## your code here
    pass

#
# def compute_first_n_eucs(n):
#     '''returns a list of the first n euclid numbers.'''
#     eucs = []
#     ## your code here
#     return eucs
#
#
# def prime_factors_of(n):
#     '''returns a list of prime factors of n if n > 1 and [] otherwise.'''
#     if n < 2: return []
#     factors = []
#     ## your code here
#     return factors
#
#
# def tabulate_euc_factors(n):
#     '''returns a list of 3-tuples (i, euc, factors).'''
#     euc_factors = []
#     ## your code here
#     return euc_factors
