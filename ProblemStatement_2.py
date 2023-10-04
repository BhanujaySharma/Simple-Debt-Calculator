class Solution:
    def findMaxAverage(self, nums, k):
        epsilon = 1e-5
        left = min(nums)
        right = max(nums)

        def check(average):
            total_sum = 0
            previous_sum = 0
            min_previous_sum = 0

            for i, num in enumerate(nums):
                total_sum += num - average
                if i >= k:
                    previous_sum += nums[i - k] - average
                    min_previous_sum = min(min_previous_sum, previous_sum)
                if i + 1 >= k and total_sum >= min_previous_sum:
                    return True

            return False

        while right - left > epsilon:
            average = (left + right) * 0.5
            if check(average):
                left = average
            else:
                right = average

        return left