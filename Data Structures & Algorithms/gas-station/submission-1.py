class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalgas=totalcost=tank=start=0
        for i in range(len(gas)):
            totalgas+=gas[i]
            totalcost+=cost[i]

            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        if totalgas<totalcost:
            return -1
        return start