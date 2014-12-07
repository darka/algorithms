class Solution:
    def findPeakElement(self, num):
        a = 0
        b = len(num)
        while True:
            middle = (a + b) / 2
            if middle == 0 and len(num) == 1:
                return middle
            if middle == 0 and num[middle] > num[middle+1]:
                return middle
            if middle == len(num) - 1 and num[middle-1] < num[middle]:
                return middle
            if num[middle-1] < num[middle] > num[middle+1]:
                return middle
            elif num[middle-1] > num[middle]:
                b = middle
            else:
                a = middle
