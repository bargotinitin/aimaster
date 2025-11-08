def func1():
 print("howdy")

func1()


def func2(str1):
	print(str1)

func2("Hello world")


def func3(*args):
 print(args)
 print(args[1])


func3("hero", "Spiderman", "Ironman")

def func4(*args):
 print(args)
 print(args[1])

 def innerfunc3(args):
  print(args[0])

 innerfunc3(args)

func4("hero", "Spiderman", "Ironman")