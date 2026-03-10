class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        result = []

        def backtrack(index, current_string):
            # Base case: if the current string length matches digits length
            if index == len(digits):
                result.append(current_string)
                return

            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digits[index]]

            for letter in letters:
                # Recurse to the next digit
                backtrack(index + 1, current_string + letter)

        # Start the recursion
        backtrack(0, "")
        return result