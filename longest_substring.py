#string is passed in, return the length of the longest substring
def length_of_longest_substring(s: str) -> int:
	#we have a python dictionary, and we initialize the ints max_len and start to 0
    seen = {}
    max_len = 0
    start = 0

    #loop through the length of the string
    for i in range(len(s)):
    	#if current element is in seen and if its greater than start
        if s[i] in seen and seen[s[i]] >= start:
            # Update the start index to skip the previously seen character
            #start holds 1 plus the index of the current element
            start = seen[s[i]] + 1

        #seen holds the index of the current element
        seen[s[i]] = i
        #max_len calculates the max between the current max,
        #and the difference between the current index and start
        max_len = max(max_len, i - start + 1)
    return max_len