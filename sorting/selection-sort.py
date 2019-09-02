## Implementation of a selection sort for integers (or any other element, which sorts by using simple greater than or smaller than comparators). By
## adding mutlipele defintions of the comparator, it shoudl be possible to make this program generic.
## Author: AJ

class sorting:
    def __init__(self):
        self.arr = [] # creates a blank array

    def get_data(self):
        self.arr = list(map(int, input().split()))
        return self.arr

    def selection_sort(self):
        larr = len(self.arr)
        for indx in range(larr):
            curr_min = self.arr[indx]
            curr_indx = indx
            for indx2 in range(indx+1, larr):
                if self.arr[indx2] < curr_min:
                    curr_min = self.arr[indx2]
                    curr_indx = indx2
            temp = self.arr[indx]
            self.arr[indx] =  curr_min
            self.arr[curr_indx] = temp

    def print_arr(self):
        for ele in self.arr:
            print(str(ele) + ' ', end='')
        print('')

sorter = sorting()
sorter.get_data()
sorter.print_arr()
sorter.selection_sort()
sorter.print_arr()
