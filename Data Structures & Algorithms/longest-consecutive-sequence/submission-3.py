class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        for num in num_set:
        # 1. Is this the beginning of a sequence?
            if num-1 not in num_set:
                current = num
                current_length = 1

                while current + 1 in num_set:
                    current += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest