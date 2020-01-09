# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    #first check if base case has been reached
    if len(sequence)==1:
        #if so return a list containing the character
        return([sequence])
    else:
        #create the list we will return
        end_list=[]
        #need to enumerate sequence so we can identify the index for identical characters
        enum_seq=list(enumerate(sequence))
        
        #create a dictionary so we can check if itterative process has occured for an identical character
        repeated_characters={}
        
        for i in enum_seq:
            #check if character has already been used if not then perform recursive process
            if repeated_characters.get(i[1],None)==None:
                
                #create a list of all characters that don't have the same index as the character we're considering
                recurs_input=[k for j,k in enum_seq if j!=i[0]]
                
                #join list so that input will be a string
                recurs_input=''.join(recurs_input)
                recurs_list=get_permutations(recurs_input)
                
                #check list returned isn't empty and if not then add
                if len(recurs_list)!=0:
                    end_list+=[i[1]+k for k in recurs_list]
                repeated_characters[i[1]]=1
            
        return(end_list)
            

    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations('mate'))

