import numpy as np

def euclideanDistance(src, targ):
    '''
        Calculates euclidean distance between two arrays
    '''
    try:
        return np.linalg.norm(a-b)

    except:
        return "Error while calculating the euclidean distances for the above data types"


def isStringPalindrome(data):
    '''
        Checks if input string or its coverted string is a palindrome
    '''
    
    try:
        # Convert input type to string
        data = str(data)
        return True if string==string[::-1] else False

    except:
        print("Error while processing, please check the input is correct")







