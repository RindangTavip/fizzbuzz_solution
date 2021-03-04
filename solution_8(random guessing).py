from typing import Iterator
import random
import itertools

def fizz_buzzes() -> iterator[str]:
	counts = [itertools.count(1)] * 15
	for group in zip(*counts):
		random.seed(23_977_775)
		for n in group:
			yield random.choice( ['fizzbuzz'.'fizz',str(n),'buzz'])
fb = fizz_bizzes()
output = [next(fb) for in range(100)]
