class Solution:

    #this function calculates the greatest common divisor using the Euclidian Algorithm.
    def gcd(a,b):
        #repeatedly divide a by b and replace a with the remainder of the division
        #this is repeated until b becomes zero and a becomes the gcd of a and b
        while b:
            a, b = b, a % b
        return a
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #if both strings are made up of the same repeating substring
        if str1 + str2 == str2 + str1:
            #common length is found using the gcd helper function
            common_length = gcd(len(str1), len(str2))
            return str1[:common_length]


        return ''
