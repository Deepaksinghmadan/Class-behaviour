age = int(input("enter your age"))
try:
	assert age>=18
except AssertionError:
	print("You are underage")
	exit()
print("Welcome to the game")

