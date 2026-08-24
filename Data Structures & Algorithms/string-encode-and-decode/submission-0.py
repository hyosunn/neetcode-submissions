class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s      
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        while s:
            num = ""
            while s[0] != "#":
                num += s[0]
                s = s[1:]

            length = int(num)
            string = s[1:1 + length]
            s = s[1 + length:]
            decoded.append(string)
        
        return decoded

        

