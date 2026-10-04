class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original_x = x
        reversed_x = 0

        while x > 0:
            digit = x % 10
            x = x // 10
            reversed_x = reversed_x*10 + digit

        return original_x == reversed_x
    print(isPalindrome(0, 121))

    