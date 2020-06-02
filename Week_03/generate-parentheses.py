class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.addParenthesis(n, n, '')
        return self.res

    def addParenthesis(self, left, right, s):
        if left == 0 and right == 0:
            self.res.append(s)

        if left > 0:    self.addParenthesis(left - 1, right, s + '(')
        if right > left:    self.addParenthesis(left, right - 1, s + ')')
