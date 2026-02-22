#printing same num normally and with underscores
var1=25000000
var2=25_00_00_00
var3=25_000_000
print(var1,var2,var3,sep="\n")

#print output 175000.0 using e notation
num=1.75e5
print(num)

print(format(3**.125,".3f"))
print(f"{3**.125:.3f}")

#print 150000 as currency in dollars
print(format(150000,",.2f"))
#with dollar added
print(f"${150000:,.2f}")

#print percentage
print(f"{2/10:.0%}")

#calculate the exponent

# num1=float(input("Enter base:"))
# num2=int(input("Enter exponent:"))
# expo=pow(num1,num2)
# print(f"{num1} to the power of {num2} is {expo:.2f}")

#Round Numbers
# number=float(input("enter a number to be rounded:"))
# places=2
# print(f"{number} rounded to {places} decimal places is {number:.2f}")

#condition based result

num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
result=(num1-num2).is_integer()
print(f"The difference between {num1} and {num2} is an integer? {result}")
