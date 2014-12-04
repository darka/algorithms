class Solution:
    def generateParenthesisReal(self, current, total, opened, closed):
        ret = []
        if closed == total:
            ret.append(current)
        else:
            if opened < total:
                ret.extend(self.generateParenthesisReal(
                    current + '(', total, opened + 1, closed))
            if closed < opened:
                ret.extend(self.generateParenthesisReal(
                    current + ')', total, opened, closed + 1))
        return ret

    def generateParenthesis(self, n):
        return self.generateParenthesisReal("", n, 0, 0)

