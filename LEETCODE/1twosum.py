class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        BRUTEFORCE APPROCH
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        return None   
        """        

        """
        HASHMAP APPROCH
        """
        hashmap={}
        for i , num in enumerate (nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i
        return None    

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))   # [0,1]
print(sol.twoSum([3,2,4], 6))       # [1,2]
print(sol.twoSum([3,3], 6))         # [0,1]
          