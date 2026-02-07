# OOP implementation for checking if a number is a palindrome without converting it to string.
# Works with different bases, too

class Integer:
    def __init__(self, value: int, base: int=10):
        self.value = value
        self.absolute_value = abs(value)
        self.base = base
        self.digit_count = self.count_digits()
        self.digits = self.get_digits()
        self.is_palindrome = self.check_if_palindrome()

    # PROPERTY-SETTING METHODS
    def count_digits(self) -> list:
        digit_count = 0
        i = 0
        while self.absolute_value >= self.base**i:
            digit_count = i
            i += 1
        digit_count += 1
        return(digit_count)

    # def build_from_digits(self, digits: list):
    #     value = 0
    #     digits.reverse()
    #     for i, digit in enumerate(digits):
    #         value += digit * self.base**i
    #     return(value)
    
    def get_digits(self):
        digits = []
        i = 0
        for i in range(1, self.digit_count+1):
            digit = self.value % self.base**i - sum(digits)
            digits.append(digit)
        for i in range(0, len(digits)):
            digits[i] = int(digits[i] / 10**i)
        digits.reverse()
        return(digits)
    
    def check_if_palindrome(self) -> bool:
        if self.digit_count == 1:
            return True
        for i in range(0, int(len(self.digits)/2)):
            if self.digits[i] != self.digits[-i-1]:
                return False
        return True

    # DISPLAYING METHOD
    def display(self):
        # TODO: Add displaying with the specified base
        print(self.value())

number = Integer(5005, 10)

print(number.__dict__)
