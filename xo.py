  
all_steps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random as r

def tablo():
	print('')
	print('')	
	print('			',all_steps[0],'|', all_steps[1],'|', all_steps[2],'	')
	print('			-----------',	 )
	print('			',all_steps[3],'|', all_steps[4],'|', all_steps[5],'	')
	print('			-----------',	 )
	print('			',all_steps[6],'|', all_steps[7],'|', all_steps[8])
	print('')
	print('')


minus = []

def pc():
	while True:
		comp = r.randint(1,9)
		if comp not in minus:
			all_steps[comp-1] = 'O'
			print(comp)
			minus.append(comp)
			break

def user():
	while True:
		user = int(input('enter your number'))
		all_steps[user-1] = 'X'
		minus.append(user)
		break

while True:
	tablo()
	user()
	tablo()
	pc()