class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = curr = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            ans = max(ans, curr)

        return ans
