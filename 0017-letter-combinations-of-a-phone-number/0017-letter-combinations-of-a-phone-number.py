class Solution:
	def letterCombinations(self,digits):
		
		if not digits:
			return []
		phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
					
		result = []
		
		
		def backtrack(index,path):
			
			if len(digits) == len(path):
				result.append("".join(path))
				return
				
			currentDigit = digits[index]
			letters = phone_map[currentDigit]
			
			for letter in letters:
				path.append(letter)
				backtrack(index+1,path)
				path.pop()
				
		backtrack(0,[])
		return result