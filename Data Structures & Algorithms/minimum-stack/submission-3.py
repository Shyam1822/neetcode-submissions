class MinStack:
    #2/6/26

    def __init__(self):
        self.st = []
        self.min_st = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if (self.min_st and self.min_st[-1]<val):
            self.min_st.append(self.min_st[-1])
        else:
            self.min_st.append(val)
            

    def pop(self) -> None:
        self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
