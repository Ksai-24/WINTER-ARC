class solution:
    def containduplicates(self,nums):
        nums=[1,2,3,3,4,5,6,7,7]
        """
        if len(nums)==len(str(nums)):
            return False
        else:
            return True
        """
        return len(nums)==len(str(nums))