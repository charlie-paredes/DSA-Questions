class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Initialize the first three values of the Tribonacci sequence
        t0, t1, t2 = 0, 1, 1
        
        # Calculate the Tribonacci sequence using iterative approach
        #loop from 3 to n+1, set tn equal to sum of first three
        #t0, t1 and t2 are updated every time 
        for i in range(3, n + 1):
            tn = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tn
            #at the end of this loop t2 has the value of tn
            
        return t2