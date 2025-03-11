# What does this piece of code do?
# Answer: record after how many times' operation will the two random number in the range 1 to 5 be equal 

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0

#build a loop start with progress = 0
while progress>=0:
	progress+=1

#use randint to generate two random numbers in the range from 1 to 5
	first_n = randint(1,6)
	second_n = randint(1,6)

#stop the loop when two random numbers are equal
	if first_n == second_n:

#print the number of operation 
		print(progress)
		break

