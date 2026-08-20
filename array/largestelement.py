class Solution():
    def largestElement(self,nums):
        largest = nums[0]
        for i in nums:
            if i > largest:
                largest = i
        return largest
sol = Solution()

print(sol.largestElement([3, 5, 2, 8, 1]))