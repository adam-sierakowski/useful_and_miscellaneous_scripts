# check if a number is a palindrome without converting it to string
# a mental exercise and a coding task in a recruitment process

def count_digits(input_number):
	digit_count = None
	i = 0
	while True:
		if input_number < 10**i:
			digit_count = i
			break
		i += 1
	if input_number == 0:
		digit_count = 1
	return(digit_count)

def break_into_digits(input_number):
	digit_count = count_digits(input_number)
	digits = []
	i = 0
	for i in range(1, digit_count+1):
		digit = (input_number % 10**i - sum(digits))
		digits.append(digit)
	for i in range(0, len(digits)):
		digits[i] = int(digits[i] / 10**i)
	digits.reverse()
	return(digits)

def check_if_palindrome(input_number):
	digit_count = count_digits(input_number)
	if digit_count == 1:
		return True
	else:
		digits = break_into_digits(input_number)
		for i in range(0, int(len(digits)/2)):
			if digits[i] != digits[-i-1]:
				return False
			else:
				is_palindrome_up_to_this_point = True
	if is_palindrome_up_to_this_point == True:
		return True

def main():

	print(check_if_palindrome(921222353222129))

if __name__ == "__main__":
	main()

