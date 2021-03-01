# def fizz_buzz(n: int) -> str:
# 	if n % 15 == 0:
# 		return "fizzbuzz"
# 	if n % 5 == 0:
# 		return "buzz"
# 	if n % 3 == 0:
# 		return "fizz"
# 	else:
# 		return str(n)

def fizz_buzz(n: int) -> str:
	output = ["fizzbuzz","buzz","fizz",str(n)]
	idx = [n % 15, n % 5, n % 3, 0].index(0)
	return output[idx]
		
for i in range (1,101):
	print(fizz_buzz(i))
