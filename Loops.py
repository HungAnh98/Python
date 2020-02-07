import math
def IsPrime(n):	
	nums = int(math.sqrt(n))
	for i in range(2,nums+1,1):
		if n%i==0:
			return False
	return True


def drawTriangle(n):
	for i in range(1,n+1):
		for x in range(1,i+1):
			print('*',end = '')
		print('\n')



heigh = int(input("Heigh of triangle : "))
result = IsPrime(heigh)
if(result):
	print("triangle's heigh is prime number")
else:
	print("triangle's heigh is not prime number")

drawTriangle(heigh)

			
			

