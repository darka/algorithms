class Solution:
    def plusOne(self, digits):
        done = False
        for i in xrange(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                done = True
                break
        if not done:
            digits.insert(0, 1)
        return digits
            

