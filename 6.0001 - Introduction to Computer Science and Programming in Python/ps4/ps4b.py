# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
    
        cipher_dict={}
        for i in range(26):
            cipher_dict[chr(97+i)]=chr(((i+shift)%26)+97)
            cipher_dict[chr(65+i)]=chr(((i+shift)%26)+65)
        
        return cipher_dict

    def apply_shift(self, shift, cipher_dict=None):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        if cipher_dict==None:
            cipher_dict=self.build_shift_dict(shift)
        new_text=[]
        for letter in self.message_text:
            try:
                new_text.append(cipher_dict[letter])
            except KeyError:
                new_text.append(letter)
        cipher=''.join(new_text)
        
        return cipher

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self,text)
        self.shift=shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted=self.apply_shift(shift, cipher_dict=self.encryption_dict)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if type(shift)!=int or 0<=shift<26:
            
            shift=self.get_valid_shift(shift)
        
        if shift!='q':
            self.shift=shift
            self.encryption_dict = self.build_shift_dict(shift)
            self.message_text_encrypted=self.apply_shift(shift, cipher_dict=self.encryption_dict)
        
        else:
            print("No changes were made.")
        
            
            
                
    def get_int_in_range(self,num):
        '''
        Checks that the input is both an integer and in the range 0-25.
        
        
        '''
        try:
            int(num)
        except ValueError:
            return False
        num=int(num)
        return 0<=num<26
            
        
        
    def get_valid_shift(self, shift):
        
        '''
        Check's the shift is in the range 0 <= shift <26 and asks user to input
        new shift value if this isn't the case. 
        
        shift (user input): proposed new shift
        
        returns:
        '''
        while not self.get_int_in_range(shift):
            
            shift=input("If you would like to quit enter 'q' otherwise please input an integer from 0-25. Your previous entry was either not an integer or not in the correct range: ")
            if shift.lower()=='q':
                break
        
        shift=int(shift)
        return shift
                
        #first need to check that shift is an integer to enter while loop
        
        
        
        
        
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
        
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        count_dict={}
        for i in range(26):
            count_dict[i]={'count':0, 'text':None}
            count_dict[i]['text']=self.apply_shift(i)
            for j in count_dict[i]['text'].split():
                if is_word(self.valid_words,j):
                    count_dict[i]['count']+=1
                
        max_value=max([x[1]['count'] for x in count_dict.items()])
        max_keys=[k for k,v in count_dict.items() if v['count']==max_value]
        
        if len(max_keys)==1:
            return (max_keys[0],count_dict[max_keys[0]]['text'])
        else:
            print("Multiple shifts produce the same number of ")
        
        for i in max_keys:
            print('Here is the decrypted text from a shift of {} counts: '.format(i) + count_dict[i]['text'])
            answer=input('If you have read the decrypted text enter anything to continue or enter "q" to quit?: ')
            if answer.lower()=='q':
                print('You have quit this function. The cypher remains unsolved')
                return
        
        for i in max_keys:
            print(i, end=' ')
        
        answer=input('Which of the above keys was most likely to be correct?: ')
        try:
            answer=int(answer)
            
        except ValueError:
                pass
            
        while not answer in max_keys:
            answer=input('Which of the above keys was most likely to be correct? If you are not sure enter nothing and one of these keys will randomly be chosen or enter "q" to quit: ')
            if answer=='':
                chosen_key=random.choice(max_keys)
                return (chosen_key, count_dict[chosen_key]['text'])
            elif answer=='q':
                print('You have quit this function. The cypher remains unsolved')
                return
            try:
                answer=int(answer)
            
            except ValueError:
                continue
            
            
        return (answer, count_dict[answer]['text'])
                
                
        
                
        
        

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

#    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
