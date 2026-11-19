class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = []
        alert = 0
        for num in nums:
            if num in history:
                alert = 1
                history.append(num)
            else:
                history.append(num)
        if alert == 1:
            return True
        else:
            return False