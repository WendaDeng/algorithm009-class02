class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if len(bills) == 0 or bills[0] > 5:
            return False
        change = {5:0, 10:0, 20:0}
        for bill in bills:
            change[bill] += 1
            if bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                else:
                    return False
            if bill == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True
