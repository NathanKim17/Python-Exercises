def my_decorator(func) :
	def wrapper():
		print("Something is happening before the function is called")
		func()
		print("Something is happening after the function is called")
	return wrapper

def say_whee():
		print("wheeee")

def add_100(func):
	def wrapper():
		return func() + 100
	return wrapper

say_whee = my_decorator(say_whee);

def foofoo():
	return 5

foofoo = add_100(foofoo)
print(foofoo())
