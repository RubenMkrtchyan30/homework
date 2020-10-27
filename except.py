harc = input('+, -, /, *, armat, factorial')

if harc == '+':

	def sum():
		print(int(x)+int(y))

	x = input('x =')
	y = input('y =')

	sum()

elif harc == '*':
	def multy():
		print(int(x)*int(y))

	x = input('x =')
	y = input('y =')

	multy()

elif harc == '/':
	def baj():
		print(int(x)/int(y))

	x = input('x =')
	y = input('y =')

	baj()

elif harc == '-':
	def minus():
		print(int(x)-int(y))

	x = input('x =')
	y = input('y =')

	minus()

elif harc == 'armat':
	import math
	def armat():
		print(math.sqrt(int(x)))

	x = input('x =')

	armat()

elif harc == 'factorial':
	import math
	def factorial():
		print(math.factorial(int(x)))
	x = input('x =')


	factorial()


