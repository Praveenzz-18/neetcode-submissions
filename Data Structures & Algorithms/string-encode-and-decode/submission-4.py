class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(len(s))+ "#" +s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            # length = int( s[i:j] ) converting string to int here 
            length = int(s[i:j])
            i=j+1    # updating the i and j pointers   firstly moving j and 
                                    #then moving i to j and SLICING THE STRING HERE """ 
            j=i+length                
            res.append(s[i:j])
            i=j
        return res