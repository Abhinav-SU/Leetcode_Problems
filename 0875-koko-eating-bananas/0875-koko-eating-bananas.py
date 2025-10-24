class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right=0
        for pile in piles:
            right= max(right,pile)

        while left<right:
            mid =left +(right-left)//2
            count=0

            for pile in piles:
                count+=math.ceil(pile / mid)

            if count<=h:
                right =mid
            else:
                left=mid+1

        return right

            