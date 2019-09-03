## Implementation of a recursive fibonacci series. Extremely inefficient though.
## Author: AJ

class fibonacci:
    def __init__(self):
        self.number = 0
        self.series = []

    def fib_series(self, num):
        if num <=2:
            if 1 not in self.series:
                self.series.append(1)
            #self.series = list(set(self.series))
            return 1
        next = self.fib_series(num-1) + self.fib_series(num-2)
        if next not in self.series:
            self.series.append(next)
        #self.series = list(set(self.series))
        return next

    def print_fib_series(self):
        for ele in self.series:
            print(ele, end=' ')

fib = fibonacci()
num = int(input())
fib.fib_series(num)
fib.series.insert(0, 0)
fib.series.insert(1, 1)
fib.print_fib_series()

