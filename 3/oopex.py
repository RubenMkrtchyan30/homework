# 6. List sort
# Create a class: Some people are standing in a row in a park. There are trees
# between them which cannot be moved. Your task is to rearrange the people by
# their heights in a non-descending order without moving the trees. People can be
# very tall!
# Example
#  For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
#  sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# class Park:
# 	def __init__(self,a):
# 		self.a = a

# 	def sortPark(self):
# 		c = []
# 		n = 0
# 		for i in self.a:
# 			if i < 0:
# 				c.append(i)

# 			else:
# 				c.append(b[n])
# 				n += 1

				

# 		print(c)

# b = []
# a = [-1,140,-1,-1,150,160]
# for i in a:
# 	if i > 0:
# 		b.append(i)
# 		b.sort()

# res = Park(a)
# res.sortPark()

# 7. Weight
# Several people are standing in a row and need to be divided into two teams. The
# first person goes into team 1, the second goes into team 2, the third goes into
# team 1 again, the fourth into team 2, and so on.You are given an array of positive
# integers - the weights of the people. Return an array of two integers, where the
# first element is the total weight of team 1, and the second element is the total
# weight of team 2 after the division is complete.
# Example For a = [50, 60, 60, 45, 70], the output should be
# alternating Sums(a) = [180, 105]

class People:
	def __init__(self,people):
		self.people = people

	def teams(self):
		team1 = []
		team2 = []
		for i in range(len(self.people)):
			if i % 2 == 0:
				team1.append(people[i])
			else:
				team2.append(people[i])
			x = sum(team1)
			y = sum(team2)

		return x,y
people = [50,60,10,100,20,70]
res = People(people)
print(res.teams())


