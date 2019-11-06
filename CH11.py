# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:27:38 2019

@author: Carlos Villa
"""

#Fibonacci by dictionary. WOW! It it FAST!!
known = {0:1, 1:1}
def fibonacci(n):
    """ Calculates the fibonacci series using a dictionary
        to improve performance. Employs recursion.

        n: int

        returns: int 
    """
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n -2)
    known[n] = res
    
    return res

#histogram
def histogram(s):
    """ Creates a histogram of a string using dictionary
    
        s: string
    
        returns: dictionary
    """
    d = {}
    for c in s:
        while not d.get(c, 0):
            d[c] = 1
        d[c] += 1
    return d

#11-1
def build_dict(fin):
    dict_of_words = {}
    for line in fin:
        word = line.strip()
        dict_of_words[word] = 1
    
    return dict_of_words

fin = open('words.txt')

dictionary = build_dict(fin)

#11-2
def invert_dict(d):
    """ Inverts a dictionary, mapping values to keys in
        a list.

        d: dictionary

        returns: dictionary
    """
    inverse = {}
    for key in d:
        val = d[key]
        #if val is not in inverse, start an empty value list
        #otherwise append the key to value list
        inverse.setdefault(val, []).append(key)
    return inverse

#11-3


hist = histogram('parrot')
invert = invert_dict(hist)

