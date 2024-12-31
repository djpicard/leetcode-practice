class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def calc(indx):
            if indx == 0: return [1]
        
            prev = calc(indx - 1)
            out = [1]
            for i in range(len(prev) - 1):
                out.append(prev[i] + prev[i+1])
            out.append(1)
            return out
        return calc(rowIndex)