class Solution:
    def isPalindrome(self, s: str) -> bool:
        # normal approach
        """
        removedChar = "".join([char for char in s if char.isalnum()]).lower()
        reversedStr=removedChar[::-1]
        if reversedStr==removedChar:
            return True
        else:
            return False
        """
        # two pointer approach
        cleaned = "".join([char for char in s if char.isalnum()]).lower()
        l = 0
        r = len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True

