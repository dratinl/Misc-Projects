import random
import requests
import itertools


with open('inputsample.txt', 'w') as f:

	test_size = random.randrange(600)
	f.write(str(test_size) + '\r\n')
	for x in range(test_size):
		n = random.randrange(200)
		f.write(str(n) + '\r\n')
		numbers = ''
		for y in range(n-1):
			numbers += str(random.randrange(100)) + ' '
		numbers += str(random.randrange(100))
		f.write(str(numbers) + '\r\n')
		f.write(str(random.randrange(100)) + '\r\n')
	f.close()