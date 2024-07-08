class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #loop through nums
        #set value at current intex to difference
        #see if value at next index plus difference equals target

        # Initialize an empty dictionary to store elements and their indices
        my_map = {}

        # Loop through the list of numbers along with their indices
        for i, n in enumerate(nums):
            # Calculate the value that, when added to the current number, will give the target
            complement = target - nums[i]

             # Check if the complement exists in the dictionary (previously seen numbers)
            if complement in my_map:
                # If yes, return the indices of the current number and its complement
                return [my_map[complement], i]
            else:
                # If not, add the current number to the dictionary with its index
                my_map[nums[i]] = i
         # If no solution is found, return an empty list
        return []
    