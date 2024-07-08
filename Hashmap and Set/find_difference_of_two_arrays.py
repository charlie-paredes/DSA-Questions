class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        #create sets to store unique integers in the lists
        set_nums1= set(nums1)
        set_nums2= set(nums2)

        #initialize answer list
        answer=[]

        #find distinct integers in each set that are not in the other
        distinct_nums_in_nums1 = set_nums1 - set_nums2
        distinct_nums_in_nums2 = set_nums2 - set_nums1

        #append the unique integers to the answer list as lists
        answer.append(list(distinct_nums_in_nums1))
        answer.append(list(distinct_nums_in_nums1))

        return answer