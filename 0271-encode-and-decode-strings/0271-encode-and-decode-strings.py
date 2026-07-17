class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res +=chr(257)+s

        return res


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s=="":
            return []
        res =[]
        resStr =""
        for char in s:
            if char ==chr(257):
                res.append(resStr)
                resStr =""
            else:
                resStr += char
        res.append(resStr)
        return res[1:]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))