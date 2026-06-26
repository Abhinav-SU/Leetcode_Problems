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
                    