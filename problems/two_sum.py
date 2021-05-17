from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if (i + j == target and index_i != index_j):
                    return [index_i, index_j]