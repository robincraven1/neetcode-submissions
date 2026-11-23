class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        index = 0
        while index < len(nums):
            n = 1
            while index + n < len(nums):
                if nums[index] + nums[index + n] == target:
                    return [index, index+n]
                n += 1
            index += 1

        """

        hashmap = {} #dict format, key:value, number:index

        for index, number in enumerate(nums):
            hashmap[number] = index #updates a key:value into hashmap

        for index, number in enumerate(nums):
            complement = target - number
            if complement in hashmap and hashmap[complement] != index:
                return [index, hashmap[complement]]
        return []




            