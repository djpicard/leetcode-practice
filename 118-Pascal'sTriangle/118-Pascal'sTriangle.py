class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(0, numRows - 1):
            tmp = [1]
            prev = res[i]
            if len(prev) > 1:
                for i in range(len(prev) -1):
                    tmp.append(prev[i] + prev[i + 1])
            tmp.append(1)
            res.append(tmp)
        return res

