## Implements the creation of power set for a given set using the method described in the Computer Science Distilled book.
## Author: AJ

class power_set:
    def __init__(self):
        self.arr = []
        self.power_set = []

    def get_data(self):
        self.arr = list(map(int, input().split()))

    def print_power_set(self):
        for ele in self.power_set:
            print(ele, end=' ')

    def create_power_sets(self):
        for ele in self.arr:
            if len(self.power_set) == 0:
                self.power_set.append([ele])
                self.power_set.append([])
            else:
                temp_power_set = []
                for ele2 in self.power_set:
                    temp = ele2[:]
                    temp.append(ele)
                    temp_power_set.append(temp)
                for ele2 in temp_power_set:
                    self.power_set.append(ele2)


array = power_set()
array.get_data()
array.create_power_sets()
array.print_power_set()


