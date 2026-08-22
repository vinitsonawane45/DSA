class Solution():
    def leftrotate(self,nums):
        first = nums[0]

        for i in range(len(nums)-1):
            nums[i] = nums[i+1]

        nums[-1] = first
        return first
sol = Solution()
nums = [1, 2, 3, 4, 5]
a=sol.leftrotate(nums)
print(nums)
