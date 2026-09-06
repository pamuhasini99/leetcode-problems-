class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mpp={}
        for i in nums:
            mpp[i]=mpp.get(i,0)+1
        max_frequency = max(mpp.values())
        ans=0
        for i in mpp:
            if mpp[i]==max_frequency:
                ans+=mpp[i]
        return ans
        