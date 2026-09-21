class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        if x < 0:
            return False

        temp = x
        reversed_num = 0

        while temp != 0:
            ld = temp % 10
            temp //= 10
            reversed_num = reversed_num * 10 + ld

        return reversed_num == x
