# welcome to the calculator v1

what = input('What are we doing? ...')

a = float(input('First number:'))
b = float(input('Second number: '))

if what == "+":
	c = a + b
	print('Result: ' + str(c))
elif what == "-":
	c = a - b
	print('Result: ' + str(c))
elif what == "*":
	c = a * b
	print('Result: ' + str(c))
else:
	print('Error! Try again with "+", "-"" or "*"')