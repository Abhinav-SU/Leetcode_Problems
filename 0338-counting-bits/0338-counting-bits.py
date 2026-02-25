class Solution:
    def countBits(self, n):
        count = [0]* (n+1)

        for i in range(0, n + 1):
            count[i] = bin(i).count("1")

        return count
