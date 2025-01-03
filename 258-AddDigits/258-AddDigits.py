class Solution:
    def addDigits(self, num: int) -> int: 
        # for a 1 liner "return num %9 or 9"
        def convert(num):
            if num < 10:
                return num

            tmp = 0
            n = list(map(int, list(str(num))))
            
            for i in n:
                tmp += i

            if tmp > 9:
                return convert(tmp)
            return tmp

        return convert(num)