ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # FIX 1: Convert list to set properly
        wordSet = set(wordList)
        
        # Check early to save time
        if endWord not in wordSet:
            return 0
            
        endSet = {endWord}
        beginSet = {beginWord}
        count = 1
        
        while endSet and beginSet:
            # Swap to always expand the smaller set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            # FIX 2: newSet and the loops must be OUTSIDE the swap 'if' block
            newSet = set()
            
            for word in beginSet:
                wordArr = list(word)
                for i in range(len(wordArr)):
                    orgChar = wordArr[i]
                    
                    for c in ALPHABETS:
                        wordArr[i] = c
                        # FIX 3: Remove quotes around wordArr
                        newWord = "".join(wordArr)
                        
                        if newWord == word:
                            continue
                        
                        # Did the ripples touch?
                        if newWord in endSet:
                            return count + 1
                            
                        # Is it a valid stepping stone?
                        if newWord in wordSet:
                            newSet.add(newWord)
                            wordSet.remove(newWord)
                            
                    # Backtrack to the original character for the next iteration
                    wordArr[i] = orgChar
            
            # Move to the next level
            beginSet = newSet
            count += 1
            
        return 0