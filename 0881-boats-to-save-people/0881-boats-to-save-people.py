
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        low,high =0,len(people)-1
        minBoat=0
        while low <= high:
            currLimit = limit
            boatCap = 2
            if currLimit >= people[low]  and boatCap > 0:
                currLimit -= people[low]
                boatCap -= 1
                low+=1
            if currLimit >= people[high]  and boatCap > 0:
                currLimit -= people[high]
                boatCap -=1
                high-=1
            minBoat+=1
        return minBoat