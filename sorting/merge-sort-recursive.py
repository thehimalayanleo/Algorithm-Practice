## A recursive implementation of merge sort.
## Author: AJ
## test case 1 45 849 904 79 48942 7

class sorting:
    def __init__(self):
        self.arr = []

    def get_data(self):
        self.arr = list(map(int, input().split()))
        return self.arr

    def merge_sort(self, array):
        if len(array) == 1:
            return array
        mid = len(array)//2 # Find the approximate middle point
        # Separate the arrays using the middle point
        left = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])

        left_indx = 0
        right_indx = 0
        complete_arr = []

        # Iteratively combine the two arrays by sorting them appropriately
        for indx in range(len(left) + len(right)):
            if (left_indx < len(left)) and (right_indx < len(right)):
                if (left[left_indx] < right[right_indx]):
                    complete_arr.append(left[left_indx])
                    left_indx+=1
                else:
                    complete_arr.append(right[right_indx])
                    right_indx += 1

            elif left_indx == len(left):
                for indx2 in range(right_indx, len(right)):
                    complete_arr.append(right[indx2])
                right_indx = len(right)
            else:
                for indx2 in range(left_indx, len(left)):
                    complete_arr.append(left[indx2])
                left_indx = len(left)
        #print(len(left)+len(right), len(complete_arr))
        return complete_arr


    def runner(self):
        self.arr = self.merge_sort(self.arr)

    def print_arr(self):
        for ele in self.arr:
            print(str(ele) + ' ', end='')
        print('')

array = sorting()
array.get_data()
array.print_arr()
array.merge_sort(array.arr)
array.runner()
array.print_arr()

