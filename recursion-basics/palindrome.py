class palindrome:
    def __init__(self):
        self.string = ""
        self.is_palindrome = False

    def get_data(self):
        self.string = input()

    def find_palindrome(self, curr):
        if len(curr) < 1:
            self.is_palindrome = True
            return True
        if curr[0] != curr[len(curr)-1]:
            self.is_palindrome = False
            return False
        self.find_palindrome(curr[1:len(curr)-1])

pal = palindrome()
pal.get_data()
pal.find_palindrome(pal.string)
print(pal.is_palindrome)