def Kanye() :
	print("I'll let you finish, but Beyonce has one of the best videos of all time!")

def Taylor(func) :
	def wrapper() :
		print("Thank you so much! I.. [Shocked]")
		func()
		print("Thank you so much! I.. [Shocked]")
	return wrapper

Kanye()
Kanye = Taylor(Kanye)
Kanye()
