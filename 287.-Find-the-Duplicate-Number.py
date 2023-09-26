class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Make a list of fixed size/same size as input list
        #Set all of the values in the list to False; will keep track if that value has been seen before
        assist = [False] * len(nums)

        #Iterate through the list
        for i in nums:
            #if the value of that list position has been seen(==True) then there is a duplicate and the list position should be returned
            if assist[i] == True:
                return i
            #otherwise the position should be marked as seen(=True) as it has already been processed
            else:
                assist[i] = True
        
        #no need to return any default result due to the parameters of the problem(there will always be a duplicate in a given input list)

#Intuitive work around well-known Floyd's Tortoise and Hare Algorithm Problem 
#I am very proud of myself for this one, I worked around the problem even though it seemed like I had to use the algorithm
