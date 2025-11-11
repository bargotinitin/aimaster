import functools

def changecase(func):
	@functools.wraps(func)
	def myinner():
		return func().upper()

	return myinner



@changecase
def myFunction():
	return "hero"

print(myFunction.__name__)
