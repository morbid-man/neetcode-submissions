class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        head = 0
        tail = n - 1
        while head < tail:

            while not s[head].isalnum() and head < tail:
                head += 1
            while not s[tail].isalnum() and head < tail:
                tail -= 1
            
            if head >= tail:
                return True
            
            if s[head].lower() != s[tail].lower():
                print(f"{s[head]}:{s[tail]}")
                return False
            
            head += 1
            tail -= 1

        return True
            

