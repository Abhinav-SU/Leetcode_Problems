class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases where the valid substring starts from index 0
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the index of the last unmatched '('
                if not stack:
                    stack.append(i)  # If stack is empty, push current index as the new potential start for a valid substring
                else:
                    # The length of the current valid substring is the difference between the current index and the index of the last unmatched '('
                    max_length = max(max_length, i - stack[-1])
        
        return max_length