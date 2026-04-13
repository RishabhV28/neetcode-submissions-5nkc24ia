class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i,num in enumerate(nums):
            A.append([num,i])
        A.sort()
        start=0
        end=len(nums)-1
        while start<end:
            total=A[start][0]+A[end][0]
            if total==target:
                return [min(A[start][1],A[end][1]),max(A[start][1],A[end][1])]
            elif total<target:
                start+=1
            else:
                end-=1

        return []
        