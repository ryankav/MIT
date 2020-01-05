# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out = ''
    for i in secret_word:
        if i in letters_guessed:
            out+=i
        else:
            out+='_ '
    
    return(out)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s=string.ascii_lowercase
    pos_let=''
    for i in s:
        if i not in letters_guessed:
            pos_let+=i
            continue
    return(pos_let)
        
def is_vowel(letter):
    
    vowels='aeiou'
    if letter in vowels:
        return True
    else:
        return False

def input_check(guess,guesses,warnings,letters_guessed,secret_word):
    
    invalid=None
    output=None
    if not str.isalpha(guess):
        invalid=True
        output=0
    elif len(guess) != 1:
        invalid=True
        output=0
    elif guess in letters_guessed:
        invalid=True
        
    
    if invalid:
        if output == 0:
            output = 'Oops! That is not a valid letter. '
        else:
            output = 'Oops! You have already guessed that letter. '
            
        if warnings!=0:
            warnings-=1
            output+= ('You have {} warnings left: '.format(warnings) + get_guessed_word(secret_word, letters_guessed))
        elif guesses==1:
            guesses-=1
            output+=('You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
        else:
            guesses-=1
            output+=('You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
        
        return(invalid, guesses, warnings, output)
    
    return((False,))
            
        
        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses=6
    warnings=3
    available_letters=''
    letters_guessed=''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secret_word)))
    print('you have {} warnings left'.format(warnings))
    print('-------------')
    available_letters=get_available_letters(letters_guessed)
    while guesses>0:
        print('You have {} guesses left.'.format(guesses))
        print('Available letters: '+available_letters, end='')
        guess=input('Please guess a letter:')
        guess=str.lower(guess)
        
        check=input_check(guess, guesses, warnings, letters_guessed, secret_word)
        if check[0]:
            guesses=check[1]
            warnings=check[2]
            print(check[3])
            print('-------------')
            if guesses==0:
                print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
            
            continue
                
            
        
# =============================================================================
#         if not str.isalpha(guess):
#             if warnings!=0:
#                 warnings-=1
#                 print('Oops! That is not a valid letter. You have {} warnings left: '.format(warnings) + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 continue
#             elif guesses==1:
#                 guesses-=1
#                 print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
#                 continue
#             else:
#                 guesses-=1
#                 print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 continue
#             
#         if len(guess)!=1:
#             if warnings!=0:
#                 warnings-=1
#                 print('Oops! That is not a valid letter. You have {} warnings left: '.format(warnings) + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 continue
#             elif guesses==1:
#                 guesses-=1
#                 print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
#                 continue
#                 
#             else:
#                 guesses-=1
#                 print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 continue
#             
#         
#         if guess in letters_guessed:
#             if warnings!=0:
#                 warnings-=1
#                 print('Oops! You have already guessed that letter. You have {} warnings left: '.format(warnings) + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 continue
#             elif guesses==1:
#                 guesses-=1
#                 print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
#                 continue
#                 
#             else:
#                 guesses-=1
#                 print('Oops! You have already guessed that letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
#                 print('-------------')
#                 continue
# =============================================================================
        
        letters_guessed+=guess
        if guess in secret_word:
            print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))
            if is_vowel(guess):
                guesses-=2
            else:
                guesses-=1
        
        print('-------------')
        available_letters=available_letters.replace(guess,'')
        
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            unique_letters=set(secret_word)
            score=guesses*len(unique_letters)
            print('Your total score for this game is: {}'.format(score))
            
            break
        
        if guesses<=0:
            print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
            
            



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word, incorrect_letters,correct_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word)!=len(other_word):
        return False

    for k in range(len(my_word)):
        if my_word[k]=='_':
            if other_word[k] in correct_letters:
                return False
            continue
        elif my_word[k]!=other_word[k]:
            return False
    for j in incorrect_letters:
        if j in other_word:
            return False
    
    return True
        



def show_possible_matches(my_word,letters_guessed, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word=my_word.replace(" ","")
    incorrect_letters=set(letters_guessed)
    correct_letters=set(my_word)
    incorrect_letters.difference_update(correct_letters)
    correct_letters.remove('_')
    
    for i in wordlist:
        if match_with_gaps(my_word, i, incorrect_letters,correct_letters):
            print(i, end=' ')
            
                    
def most_likely_letter(my_word,letters_guessed, wordlist, available_letters):
    
    my_word=my_word.replace(" ","")
    incorrect_letters=set(letters_guessed)
    correct_letters=set(my_word)
    incorrect_letters.difference_update(correct_letters)
    count={}
    word_count=0
    
    for i in available_letters:
        count[i]=0
    
    for i in wordlist:
        if match_with_gaps(my_word, i, incorrect_letters,correct_letters):
            word_count+=1
            let=set(i)
            for k in let:
                try:
                    count[k]+=1
                except KeyError:
                    continue
    y = sorted(count.keys(), key = lambda x:count[x], reverse=True)
    
    for n in y:
        print('{0}: {1}%'.format(n,round((count[n]*100/word_count),1)),end=' ')
    
    
    
    
    



def hangman_with_hints(secret_word, wordlist):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses=6
    warnings=3
    available_letters=''
    letters_guessed=''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secret_word)))
    print('you have {} warnings left'.format(warnings))
    print('-------------')
    available_letters=get_available_letters(letters_guessed)
    
    while guesses>0:
        print('You have {} guesses left.'.format(guesses))
        print('Available letters: '+available_letters, end='')
        guess=input('Please guess a letter:')
        
        if guess=='$':
             a=get_guessed_word(secret_word, letters_guessed)
             most_likely_letter(a, letters_guessed, wordlist, available_letters)
             print()
             print('-------------')
             
             continue
            
        if guess=='*':
            a=get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(a,letters_guessed,wordlist)
            print()
            print('-------------')
            
            continue
        guess=str.lower(guess)
        check=input_check(guess, guesses, warnings, letters_guessed, secret_word)
        if check[0]:
            guesses=check[1]
            warnings=check[2]
            print(check[3])
            print('-------------')
            if guesses==0:
                print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
            continue
        
        letters_guessed+=guess
        if guess in secret_word:
            print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))
            if is_vowel(guess):
                guesses-=2
            else:
                guesses-=1
        
        print('-------------')
        
        available_letters=available_letters.replace(guess,'')
        
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            unique_letters=set(secret_word)
            score=guesses*len(unique_letters)
            print('Your total score for this game is: {}'.format(score))
            
            break
        
        if guesses<=0:
            print('Sorry you ran out of guesses. The word was {}'.format(secret_word))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word, wordlist)
