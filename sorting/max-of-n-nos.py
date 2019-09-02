## Basic Implementation of finding the maximum of n (independent parameter) integers.
## Author: AJ

class arr_max:
    def __init__(self):
        self.arr = [] # Create an empty array

    def get_data(self):
        self.arr = list(map(int, input().split()))
        return self.arr

    def max_finder(self):
        if len(self.arr) == 0:
            print('Array is empty')
            return None

        currMax = self.arr[0]
        for indx in range(len(self.arr)):
            if self.arr[indx] > currMax:
                currMax = self.arr[indx]

        return currMax

arrClass = arr_max()
arrClass.get_data()
print(arrClass.max_finder())

