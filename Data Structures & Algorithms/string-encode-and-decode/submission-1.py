class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += f'{len(s)}len' + s
        print(encoded_str)
        return encoded_str 

    def decode(self, s: str) -> List[str]:
        i = 0
        results = []
        length_count = True
        string = False
        length = ''
        while i < len(s):
            if s[i:i+3] == "len":
                i = i + 3
                length_count = False
                string = True
            if length_count and not string:
                length += s[i]
                i = i + 1
            if string and not length_count:
                length = int(length)
                results.append(s[i:i + length])
                i = i + length
                length = ''
                length_count = True
                string = False

        return results
            

