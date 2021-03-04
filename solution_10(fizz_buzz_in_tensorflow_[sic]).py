def binary_digits(n: int, num_digits: int = 10) -> toren.tensor:
	digits=[]
	for n in range(num_digits):
		digits.append(float(n%2))
		n=n//2
	return torch.tensor(digits)
	

training_data= [Instance.create(n, binary_digits) for n in range (1,1023)]
test_data = [Instance.creat(n, binary_digits) for n in range (1,101)]
input_dim = len(training-data[0].features)
