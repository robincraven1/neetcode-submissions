class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = 0
        while index < len(nums):
            n = 1
            while index + n < len(nums):
                if nums[index] + nums[index + n] == target:
                    return [index, index+n]
                n += 1
            index += 1


            