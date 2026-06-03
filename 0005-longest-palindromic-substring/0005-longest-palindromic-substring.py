class Solution:
	def longestPalindrome(self,s:str)->str:
		if not s or len(s) < 1:
			return s
		start = 0
		maxLen = 0
		maxStr = ''
		
		def expand(left,right):
			while left >= 0 and right < len(s) and s[left]== s[right]:
				left -= 1
				right += 1
			return right - left - 1
			
		for i in range(len(s)):
			oddLen = expand(i,i)
			evenLen = expand(i,i+1)
			
			currLen = max(oddLen,evenLen)
			
			if maxLen < currLen:
				maxLen = currLen
				start = i - (currLen -1)//2
				
		return s[start : start + maxLen]