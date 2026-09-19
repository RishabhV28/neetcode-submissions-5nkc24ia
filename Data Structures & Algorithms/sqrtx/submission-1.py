class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0

        if x==1:
            return 1
        
        res=1
        for i in range(x):
            if i*i>x:
                res=i-1
                return res
            res=i

        return res
        