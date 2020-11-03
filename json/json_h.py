import json

name = 'json_h.txt'
about_you = input('enter info about you')

with open(name,'w') as about:
	json.dump(about_you,about)

f = open('json_h','r')
r = json.loads(f.read())

#3

file_name = 'json_h.txt'
try:
	with open(name) as file1:
	user = json.load(file1)
	print('Hello',user)

except:
	username = input('what is your name? ')
	with open(file_name, 'w') as file:
	user = json.dump(username, file)
	print('Hello',user)