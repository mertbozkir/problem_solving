class Solution:
    def reverse(self, x: int) -> int:
        ex = str(x)
        if ex[0] == "-":
            ex2 = ex[1:]
            print(ex2[::-1])
            if not((-2)**31 < int(ex2[::-1]) < 2**31 - 1):
                return 0
            return ex[0] + str(int(ex2[::-1]))
        else:
            if not((-2)**31 < int(ex[::-1]) < 2**31 - 1):
                return 0
            return int(ex[::-1])
        
        