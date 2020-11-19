# class Myclass:
# 	def __init__(self,name,surname):
# 		self.name = name
# 		self.surname = surname

# class he(Myclass):
# 	def __init__(self,name,surname,age):
# 		self.name = name
# 		self.age=age

# 	def myfunc(self):
# 		print('my name is  ' + self.name)


# p1 = he('Ruben','Mkrtchyan','20')
# p1.myfunc()

class rectangle:
	def __init__(self,width,length):
		self.width = width
		self.length = length

	def arearec(self):
		return self.length * self.width

res = rectangle(4,3)
print(res.arearec())