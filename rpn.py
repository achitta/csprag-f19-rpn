#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		if token == '+':
			num1 = stack.pop()
			num2 = stack.pop()
			result = num1+num2
			stack.append(result)
		elif token == '-':
			num1 = stack.pop()
			num2 = stack.pop()
			result = num2 - num1
			stack.append(result)
		else:
			stack.append(int(token))
		print(stack)
	if len(stack) != 1:
		raise TypeError("Bad Input")
	return stack.pop()
def main():
	while True:
		calculate(input('rpn calc> '))

if __name__ == '__main__':
	main()
