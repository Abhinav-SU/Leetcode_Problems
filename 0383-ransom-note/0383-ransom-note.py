from collections import defaultdict
class Solution:
    def canConstruct(self,ransomNote: str, magazine: str) -> bool:
        lenNote = len(ransomNote)
        lenMag = len(magazine)
        if lenMag < lenNote:
            return False
        countMag = defaultdict(int)
        for char in magazine:
            countMag[char] +=1
        for char in ransomNote:
            if countMag[char] == 0:
                return False
            countMag[char] -=1
        return True