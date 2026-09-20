class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complecent = target - nums[i]
            if complecent in seen:
                return [seen[complecent], i]
            seen[nums[i]] = i