#! /Users/aguda/opt/anaconda3/bin/python3

r = int(input("Please enter a number to list fibanacci Series: "))

def fibanacci(n):
    n1,n2 = 0,1
    count = 0
    if n <= 0:
        print("Please enter number at least 1:")
    elif n == 1:
        return 0
    else:
        while count <= n:
            print(n1)
            n1,n2 = n2, n1+n2
            count += 1

print(fibanacci(r))


'''
# Number of fibonacci number for give value
def fibanacci(n):
	if n<0:
		print("Please enter number at least 1:")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibanacci(n-1)+fibanacci(n-2)
'''