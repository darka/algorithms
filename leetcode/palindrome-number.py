class Solution:
    def reverseNumber(self, x):
        reversed = 0
        while x > 0:
            digit = x % 10
            reversed *= 10
            reversed += digit
            x /= 10
        return reversed
        
    def isPalindrome(self, x):
        return x == self.reverseNumber(x)
