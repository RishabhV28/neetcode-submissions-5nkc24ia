class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=''
        for i in  strs :
            str1+= str(len(i)) + "#"+ i
            
        return str1

    def decode(self, s: str) -> List[str]:
        list1=[]
        
        ind=0
        i=0
        while i<len(s):
            str2=''
            while s[i]!='#':
                str2+=s[i]
                i+=1
            num=int(str2)
            i+=1

    
            list1.append(s[i:i+num])
            i+=num
        return list1
        

            
