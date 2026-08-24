class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + "#" + s
        return ans
        
    def decode(self, s: str) -> List[str]:
        idx = 0
        ans = []

        while idx != len(s):
            numStr = ""
            while s[idx] != "#":
                numStr += s[idx]
                idx += 1
            num = int(numStr)
            idx += 1

            ans.append(s[idx: idx + num])
            idx += num
        
        return ans





        
    











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
