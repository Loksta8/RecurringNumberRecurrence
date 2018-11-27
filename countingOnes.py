def numberOfOnes(n):
	count = 0
	count = str(n).count("1")
	return count

def countOnes(n):
	count = 0
	for i in range(1,n+1):
		count = count + numberOfOnes(i)
	return count

print(countOnes(199980))
