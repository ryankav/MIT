# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations
import random

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict_map={}
# =============================================================================
# As code doen't change consonants don't need them in the dicitonary
# =============================================================================
# #         for i in CONSONANTS_LOWER:
# #             dict_map[i]=i
# #             dict_map[i.upper()]=i.upper()    
# #     
# =============================================================================
# =============================================================================
        for i in range(5):
            dict_map[VOWELS_LOWER[i]]=vowels_permutation[i]
            dict_map[VOWELS_LOWER[i].upper()]=vowels_permutation[i].upper()
            
        return dict_map
            
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        new_text=[]
        for i in self.message_text:
            try:
                new_text.append(transpose_dict[i])
            except KeyError:
                new_text.append(i)
        cipher=''.join(new_text)
        return cipher
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        
        values={}
        perm = get_permutations(VOWELS_LOWER) 
        
        for order in perm:
            letter_map={}
            for letter in range(len(VOWELS_LOWER)):
                letter_map[VOWELS_LOWER[letter]]=order[letter]
                letter_map[VOWELS_UPPER[letter]]=order[letter].upper()
                
            values[order]={'count':0, 'text':None} 
            #now decrypt text
            values[order]['text']=self.apply_transpose(letter_map)
            
            #now count the number of words that are valid
            for word in values[order]['text'].split():
                if is_word(self.valid_words,word):
                    values[order]['count']+=1
            
        #now find maximum word count
        max_value=max([x[1]['count'] for x in values.items()])
        max_orders=[k for k,v in values.items() if v['count']==max_value]
        
        if len(max_orders)==1:
            return (max_orders[0],values[max_orders[0]]['text'])
        else:
            print('There is more than one permutation which produces the maximum number of words')
            answer = input('if you would like to select the permutation then enter "y" otherwise a permutation shall be randomly selected for you: ')
        
        if answer.lower()!='y':
            choice=random.choice(max_orders)
            return values[choice]['text']
        #now show them the options
        for order in max_orders:
            print('Here is the decrypted text given by the permutation {}: '.format(order) + values[order]['text'])
            answer=input('If you have read the decrypted text enter anything to continue or enter "q" to quit?: ')
            if answer.lower()=='q':
                print('You have quit this function. The cypher remains unsolved')
                return
        
        for order in max_orders:
            print(order, end=' ')
        
        answer=input('Which of the above permutations was most likely to be correct?: ')
            
        while not answer in max_orders:
            answer=input('Which of the above permutations was most likely to be correct? If you are not sure enter nothing and one of these permutations will randomly be chosen or enter "q" to quit: ')
            if answer=='':
                chosen_key=random.choice(max_orders)
                return (chosen_key, values[chosen_key]['text'])
            elif answer=='q':
                print('You have quit this function. The cypher remains unsolved')
                return
        
        return (values[answer]['text'])
        

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
