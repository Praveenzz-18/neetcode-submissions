class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Hashset={}
        n=len(numbers)
        for i in range(n):
            for j in range(n):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]