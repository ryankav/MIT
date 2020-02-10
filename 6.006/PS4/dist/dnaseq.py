#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        
        self.dict = {}
        
        for k_v in pairs:
            self.put(k_v[0],k_v[1])
    # Associates the value v with the key k.
    def put(self, k, v):
        
        value=self.dict.get(k,None)
        if not value:
            self.dict[k]=[v]
        else:
            value.append(v)
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        
        value = self.dict.get(k,[])
        
        return value

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    try:
        subseq = ''
        pos=0
        for i in range(k):
            subseq+=next(seq)
        rol_hash=RollingHash(subseq)
        
        while True:
            yield rol_hash.current_hash(),(subseq,pos)
            
            prev_char=subseq[0]
            subseq=subseq[1:]+next(seq)
            rol_hash.slide(prev_char,subseq[-1])
            
            pos+=1
            
    except StopIteration:
        return
        
# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    try:
        subseq = ''
        pos=0
        for i in range(k):
            subseq+=next(seq)
        rol_hash=RollingHash(subseq)
        
        while True:
            yield rol_hash.current_hash(),(subseq,pos)
            
            #this may not be the fastest approach but is deffinetely the easiest
            #to implement.
            for i in range(m):
                prev_char=subseq[0]
                subseq=subseq[1:]+next(seq)
                rol_hash.slide(prev_char,subseq[-1])
                
                pos+=1
    except StopIteration:
        return
# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).

def getExactSubmatches(a, b, k, m):
    
    dictionary = Multidict(intervalSubsequenceHashes(a,k,m))
        
    for key,(b_seq,b_pos) in subsequenceHashes(b,k):
        seq_and_pos = dictionary.get(key)
        if not seq_and_pos:
            continue
        matching_pos=[a_pos for a_seq,a_pos in seq_and_pos if a_seq==b_seq]
        
        if not matching_pos:
            continue
        
        for a_pos in matching_pos:
            yield a_pos, b_pos
        
        
        
if __name__=='__main__':    

        
    if len(sys.argv) != 4:
        print('Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0]))
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
