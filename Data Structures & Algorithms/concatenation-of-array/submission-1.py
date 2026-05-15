class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        newnums=[0]*(2*n)
        for i,j in enumerate(nums):
            newnums[i]=newnums[n+i]=j

        return newnums