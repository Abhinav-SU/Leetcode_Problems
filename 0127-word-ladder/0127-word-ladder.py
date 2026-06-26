class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet = {beginWord}
        endSet = {endWord}
        count = 1

        while beginSet and endSet:
            if len(endSet) > len(beginSet):
                beginSet, endSet = endSet, beginSet
            newSet = set()
            for curr_word in beginSet:
                wordChar = list(curr_word)
                for i in range(len(wordChar)):
                    orgChar = wordChar[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        wordChar[i] = c
                        new_word = "".join(wordChar)

                        if new_word in endSet:
                            return count + 1

                        if new_word in wordSet:
                            newSet.add(new_word)
                            wordSet.remove(new_word)

                    wordChar[i] = orgChar

            beginSet = newSet
            count += 1
        return 0
