class Mycar:
	def __init__(self,mark,color):
		self.mark = mark
		self.color = color

	def myfunc(self):
		print('my machine is  ' + self.mark,'and color is ',self.color)

p1 = Mycar('Bmw','White')
p1.myfunc()