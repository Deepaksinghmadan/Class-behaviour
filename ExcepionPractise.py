class MobileNumberError(Excepion):pass
class MobileNuberNot Valid(Exception):pass
try:
	number = int(input("?"))
	if len(str(number))!=10:
		raise MobileNumberError
	if int(str(number)[0])<6:
		raise MobileNuberNot Valid
except valueerror:
	print(" error")
except MobileNumberError:
	print("not a ten digit")
except MobileNumberNotValid:
	print("Mobilenot valid")
except:
	print("defauls")
else:
	while len(str(number)) !=1:
		sum = 0
		for i in str(number):
			sum +=int(i)
			number = str(sum)
			



