class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet =set(words)
        memo ={}

        def canReach(word):
            if word in memo:
                return memo[word]

            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordSet:
                    if suffix in wordSet or canReach(suffix):
                        memo[word]= True
                        return True
            memo[word] = False
            return False
        result = []
        for word in words:
            if canReach(word):
                result.append(word)
        return result
        