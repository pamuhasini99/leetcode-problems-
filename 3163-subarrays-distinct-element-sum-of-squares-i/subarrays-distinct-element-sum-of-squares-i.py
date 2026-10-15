class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        '''n = len(nums)
        total = 0

        for i in range(n):
            for j in range(i, n):
                subarray = nums[i:j + 1]
                distinct_count = len(set(subarray))
                total += distinct_count * distinct_count

        return total
'''
        n = len(nums)
        total = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                distinct_count = len(seen)
                total += distinct_count * distinct_count

        return total
