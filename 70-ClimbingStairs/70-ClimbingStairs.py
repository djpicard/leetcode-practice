class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {
            1: 1,
            2: 2 
        }

        def climb(n):
            if n in mem: return mem[n]
            mem[n] = climb(n - 1) + climb(n - 2)
            return mem[n]
        
        return climb(n)