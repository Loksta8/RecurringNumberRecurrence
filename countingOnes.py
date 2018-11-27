'''
Author: Logan Herrera
Date: 11/26/2018
This program was created to count the number of recurring ones.
'''
#This function keeps track of the recurrences
def numberOfOnes(n):
	count = 0
	count = str(n).count("1")
	return count

#This function loops from 1 to a value given to it and uses
#The "numberOfOnes" function for the entire range of numbers
#This is a Nested function
def countOnes(n):
	count = 0
	for i in range(1,n+1):
		count = count + numberOfOnes(i)
	return count
#Finally print the results by using the function
print(countOnes(199980))
