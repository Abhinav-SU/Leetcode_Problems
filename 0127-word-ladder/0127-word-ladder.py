ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        beginSet = {beginWord}
        endSet = {endWord}
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        count =1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet,endSet = endSet,beginSet
            newSet = set()
            for word in beginSet:
                wordArr = list(word)
                for i in range(len(wordArr)):
                    orgChar = wordArr[i]
                    for char in ALPHABETS:
                        wordArr[i] = char
                        newWord = "".join(wordArr)
                        if newWord == word:
                            continue
                        if newWord in endSet:
                            return count+1
                        if newWord in wordSet:
                            newSet.add(newWord)
                            wordSet.remove(newWord)
                        wordArr[i] = orgChar
            beginSet = newSet
            count +=1
        return 0