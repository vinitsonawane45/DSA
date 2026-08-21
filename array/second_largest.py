class Solution():
    def secondlargest(self,nums):
        largest = nums[0]
        second_largest = float('-inf')

        for i in nums:
            if i > largest:
                largest = i
        for i in nums:
            if i != largest and i > second_largest:
                second_largest = i
        return second_largest
sol = Solution()
print(sol.secondlargest([3, 5, 2, 8, 1]))