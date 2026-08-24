class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            numStr = ""
            while s[i] != "#":
                numStr += s[i]
                i += 1
            i += 1
            num = int(numStr)

            res.append(s[i: i + num])
            i += num
        
        return res
        




        
    











    """
    OPTIMAL SOLUTION (O(n) time and O(1) space):
    
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list, i = [], 0

        while i < len(s): 
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            decoded_list.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        return decoded_list
    """
