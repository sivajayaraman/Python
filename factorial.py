number=input("Enter the number....")
fact=1
for i in  range(1,number+1) :
	fact=fact*i
print("{0}!={1}".format(number,fact))