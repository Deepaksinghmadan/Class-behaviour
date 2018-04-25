while len(str(number)) !=1:
	sum = 0
	for i in str(number):
		sum+=int(i)
		number = str(sum)
	print(sum)

	