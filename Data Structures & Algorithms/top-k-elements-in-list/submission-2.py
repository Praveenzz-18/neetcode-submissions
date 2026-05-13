class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]  # building an freq map in len(nums)
        for num in nums:
            count[num]= 1 +count.get(num,0) #count of freq hash map

        for num,cnt in count.items():   #bucket sort
            freq[cnt].append(num)            #appending the cnt and nums to freq map means bucket sort

        res=[]
        for i in range(len(freq)-1,0,-1):   #travsering through bucket sort in backward to find the top k most 
                                                #repteing element
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res