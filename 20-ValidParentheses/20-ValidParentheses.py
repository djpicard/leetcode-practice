class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i is "(" or i is "{" or i is "[":
                st.append(i)
                continue
            if i is ")":
                if st and st[-1] == "(":
                    st.pop()
                    continue
            if i is "}": 
                if st and st[-1] == "{":
                    st.pop()
                    continue
            if i is "]":
                if st and st[-1] == "[":
                    st.pop()
                    continue
            return False
        if len(st) > 0: 
            return False
        return True
            