class Solution:
    def tribonacci(self, n):

        t = [0] * (n + 3)
        t[0], t[1], t[2] = 0, 1, 1

        if n < 2:
            return t[n]

        for i in range(3, n + 1):
            t[i] = t[i - 1] + t[i - 2] + t[i - 3]

        return t[n]
