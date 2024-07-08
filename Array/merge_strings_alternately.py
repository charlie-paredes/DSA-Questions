class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = []

        merged = []
        i = j = 0

        #loop through both words if theres space in each of them
        while i<len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1 
            j += 1

        #loop through the rest of word1. Only executes if word1 is longer than word2
        while i<len(word1):
            merged.append(word1[i])
            i += 1

        #loop through the rest of word2. Only executes if word2 is longer than word1
        while j<len(word2):
            merged.append(word2[j])
            j += 1
        
        #return the merged string
        return ''.join(merged)
        
