from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float("-inf")
        min1 = min2 = float("inf")
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        # print(max1, max2, max3, min1, min2)
        return max(max1 * max2 * max3, max1 * min1 * min2)


def test():
    s = Solution()
    assert s.maximumProduct([1, 2, 3]) == 6
    assert s.maximumProduct([1, 2, 3, 4]) == 24
