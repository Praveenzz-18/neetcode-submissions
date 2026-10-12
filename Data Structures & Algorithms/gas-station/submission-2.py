class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        startIndex =0
        totalgas =0

        for i in range(len(gas)):
            totalgas += gas[i] -cost[i]
            if totalgas < 0:
                totalgas = 0
                startIndex = i+1

        return startIndex         





"""
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       
       if sum(gas) < sum(cost):
        return -1

       start = 0
       totalgas = 0

       for i in range(len(gas)):

           if totalgas + gas[i] < cost[i]:
              start = i+1
              totalgas = 0
           else:
              totalgas += gas[i] -cost[i]

       return start       


       


    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        i,j = 0, 0
        currgas = 0

        while j < len(gas):   
            if currgas + gas[j] - cost[j] >= 0:
                currgas += gas[j]- cost[j]
            #    i = j
            else:
                i = j+1
                currgas = 0

            j+= 1  

        return i       








    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        total =0 
        start =0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            if total < 0:
                start =i+1
                total =0

        return start        





 i first find sum of gas and cost      if cost > gas it is not possible to cover all stations
 total at i  += gas[i] - cost[i]
 if at any i total becomes negative , we cannot use any of the i seen until now as start so we set start to i+1 
 and reset total = 0

i = 0
  total at i  += gas[i] - cost[i]
  if total < 0
   start is i+1
   total = 0 

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       if sum(gas) < sum(cost):
        return -1
       start =0
       tank = 0
       for i in range(len(gas)):
        tank  += gas[i] - cost[i]
        if tank < 0:
            start = i+1
            tank = 0


       return start 


"""
