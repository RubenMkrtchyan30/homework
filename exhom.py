#You have word.txt file and in them you have
# one story.
# Write a Python function that accepts this
# story and calculate the number of uppercase
# letters and lowercase letters.

# word = 'word.txt'
# x ='asdasdDAD'
# upper = 0
# lower = 0

# for i in x:
# 	if i.isupper():
# 		upper += 1
# 	if i.islower():
# 		lower += 1

# a = print('upper = ',upper)
# l = print('lower = ',lower)



# import json 

# with open(word,'w') as f:
# 	json.dump(x,f)

# with open(word) as f:
# 	print(json.load(f))

# 2Write a python function which get a new list
# from a given list, consisting of the first
# repeating elements.
# my_list = [“a”,”b”,”a”,”c”,”b”]
# output “a”,”b”,”c”


def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "b"])


list1 = 'mylist.txt'  
import json

with open(list1,'w') as f:
	json.dump(mylist,f)

with open(list1) as f:
	print(json.load(f))