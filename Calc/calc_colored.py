# welcome to the calculator v1

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.RED)
print(Back.WHITE)

what = input('What are we doing? ...')

print(Back.BLACK)
print(Fore.GREEN)

a = float(input('First number:'))
b = float(input('Second number: '))

print(Back.WHITE)
print(Fore.BLUE)

if what == "+":
	c = a + b
	print('Result:', c)
elif what == "-":
	c = a - b
	print('Result: ' + str(c))
elif what == "*":
	c = a * b
	print('Result: ' + str(c))
else:
	print('Error! Try again with "+", "-"" or "*"')