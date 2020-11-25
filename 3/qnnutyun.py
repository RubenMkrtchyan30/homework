class Coronavirus:
	def __init__(self,celsius):
		self.celsius = celsius

	def temperature(self):
		import math as m
		farenheit = (self.celsius * m.pi) 
		farenheit = m.ceil(farenheit)
		if farenheit >  119 and farenheit < 128:
			return 'You Have coronavirus', self.celsius
		else:
			return 'Everithyng is ok', self.celsius


cel = float(input('enter your temperature '))
res = Coronavirus(cel)
print(res.temperature())

class Name:
	def __init__(self,your_name):
		self.your_name = your_name

	def res(self):
		import math as m
		self.your_name = self.your_name.lower()
		result = 0
		dict1 = {1 : ('a',' j', 's'),  2 : ('b', 'k', 't'),  3 : (' c', 'l', 'u'),  4 : ('d', 'm', 'v'),   5 : ('e', 'n', 'w'),   6 : ('f', 'o', 'x'), 
7 : ('g', 'p', 'y'),   8 : ('h', 'q', 'z'),   9 : ('i','r')}
		for i in self.your_name:

			# for j in range(len(dict1)):
			# 	if i in dict1.get(j):
			# 		result += j
			if i in dict1.get(1):
				result += 1
			elif i in dict1.get(2):
				result += 2
			elif i in dict1.get(3):
				result += 3
			elif i in dict1.get(4):
				result += 4
			elif i in dict1.get(5):
				result += 5
			elif i in dict1.get(6):
				result += 6
			elif i in dict1.get(7):
				result += 7
			elif i in dict1.get(8):
				result += 8
			elif i in dict1.get(9):
				result += 9
			else:
				return('Error - enter name ')

		if m.sqrt(result) < 5:
			return result,'Yes'
		else:
			return result,'No'
your_name = input('enter your name ')
result = Name(your_name)
print(result.res())

# 3.

class Game:
	def __init__(self,player_word,player_word2,player_word3):
		self.player_word = player_word
		self.player_word2 = player_word2
		self.player_word3 = player_word3

	def Harry(self):
		import random as r
		point = 0
		magic_word = ('Avada Kedavra',  'Crucio', 'Imperio')
		voldemort = r.choice(magic_word)
		print('1st magic word voldemort is',voldemort)
		if self.player_word == voldemort:
			point += 1
		else:
			point -= 1
		
		voldemort2 = r.choice(magic_word)
		print('2rd magic word voldemort is',voldemort2)
		if self.player_word2 == voldemort2:
			point += 1
		else:
			point -= 1

		voldemort3 = r.choice(magic_word)
		print('3rd magic word voldemort is',voldemort3)
		if self.player_word3 == voldemort3:
			point += 1
		else:
			point -= 1

		if point > 0:
			print('you win, your points is',point)
		else:
			print('you lose, your points is',point) 


player_word = input('your 1st word (Avada Kedavra/Crucio/Imperio) ')
player_word2 = input('your 2rd word (Avada Kedavra/Crucio/Imperio) ')
player_word3 = input('your 3rd word (Avada Kedavra/Crucio/Imperio) ')
result = Game(player_word,player_word2,player_word3)
result.Harry()
