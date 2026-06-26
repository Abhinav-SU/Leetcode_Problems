class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        beginSet = {beginWord}
        endSet = {endWord}
        if endWord not in wordSet:
            return 0
        count = 1  
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet,endSet = endSet,beginSet
            newSet = set()
            for word in beginSet:
                wordArr = list(word)
                for i in range(len(wordArr)):
                    orgChar = wordArr[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        wordArr[i] = c
                        new_word = "".join("wordArr")

                        if new_word == word:
                            continue

                        if new_word in endSet:
                            return count + 1

                        if new_word in wordSet:
                            newSet.add(new_word)
                            wordSet.remove(new_word)
                        wordArr[i] = orgChar
            beginSet = newSet
            count +=1           
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        beginSet = {beginWord}
        endSet = {endWord}

        if endWord not in wordSet:
            return 0
        count = 1
        while beginSet and endSet:

            if len(beginSet) > len(endSet):
                beginSet,endSet = endSet,beginSet
            newSet = set()
            for word in beginSet:
                wordArr = list(word)
                for i in range(len(wordArr)):
                    orgChar = wordArr[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        wordArr[i] = c
                        newWord = "".join(wordArr)

                        if newWord == word:
                            continue
                            
                        if newWord in endSet:
                            return count + 1

                        if newWord in wordSet:
                            newSet.add(newWord)
                            wordSet.remove(newWord)
                    wordArr[i] = orgChar
            beginSet = newSet
            count +=1

        return 0
                    