#!/usr/bin/python
# Filename: stringtools.py
import string

def split_embiggen_sort(sentence):
    '''
    takes a string and removes punctuation 
    splits it into a list of individual words, 
    converts them to uppercase and 
    sorts them in descending order
    '''
    all_converted = embiggen(sentence)
    all_converted = stripper3(all_converted)
    all_converted = divide_at_spaces(all_converted)
    all_converted = big_to_little(all_converted)
    
    return all_converted

def stripper3(sentence):
    '''
    takes a string as input and removes punctuation using list comprehension
    returns a string 
    '''
    res = "".join([x for x in sentence if x not in string.punctuation])
    return res

def embiggen(sentence):
    '''
    convert a string to uppercase and 
    returns a string
    '''
    assert(type(sentence) is str)
    converted = sentence.upper()
    return converted

def divide_at_spaces(sentence):
    '''
    takes a string as input
    splits the string at space characters and 
    returns a list of strings
    '''
    assert(type(sentence) is str)
    chopped = sentence.split()
    return chopped

def big_to_little(bits):
    '''
    sorts a list of words from longest to shortest and return a list
    '''
    assert(type(bits) is list)
    bits.sort(key=len)
    return bits