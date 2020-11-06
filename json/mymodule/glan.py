global p 
p = 3.14
def vol(r,h):
	
	v = p * (r**2) * h
	return v
def area(r,h):
	a=2 * p * r * h + 2* p * (r**2)
	return a