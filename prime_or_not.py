#prime number or not
class prime():
	def test(int):
		my_bool = True
		for i in range(1, int):
			if(int%i == 0) and i!=1 and i!=int:
				my_bool = False
		return my_bool

print("The number passed in is a prime number:")
print(prime.test(11))