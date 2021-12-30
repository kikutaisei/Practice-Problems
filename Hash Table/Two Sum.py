class Solution:
    def twoSum(self, nums, target):
        dict = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in dict:
                return [dict[diff], i]
            else:
                dict[nums[i]] = i
                
        return None

testCase1 = Solution()
print(testCase1.twoSum([2, 7, 11, 15], 9)) # Prints "[0, 1]"

testCase2 = Solution()
print(testCase2.twoSum([3, 2, 4], 6)) # Prints "[1, 2]"
