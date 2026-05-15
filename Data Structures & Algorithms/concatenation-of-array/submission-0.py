class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newnums=[]
        for j in nums:
            newnums.append(j)
        for i in nums:
            newnums.append(i)

        return newnums