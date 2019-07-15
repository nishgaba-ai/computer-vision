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
        Checks if input string or corresponding string from input is a palindrome
    '''
    
    try:
        # Convert input type to string
        data = str(data)
        return True if data==data[::-1] else False

    except:
        print("Error while processing, please check the input is correct")


def isPrime(n):
    '''
        Checks if a given number is prime or not

        Source: GeeksforGeeks
    '''
    try:
        n = int(n)
        return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n>1
    except:
        print("Error Occured While Checking for prime, please check the input is correct")
        return False



