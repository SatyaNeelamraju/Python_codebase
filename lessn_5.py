def greet(name):
    return(f'"Hello, {name}!"')

value=greet("Anagha")
print(value)
######################################################################

def cube(num):
    result=pow(5,3)
    print(f"The value of {num} raised to power of 3 is {result} " )

cube(5)
cube(4)
cube(3)
######################################################################
def convert_cel_to_far():
    C=float(input("Enter Celsius Temparature:"))
    F=(C * 9/5) +32
    print(f"Temperature Converted to Farenheit is {F:.2f}")

def convert_far_to_cel():
    F=float(input("Enter Farenheit temperature:"))
    C=(F-32) * 5/9
    print(f"Temperature Converted to Celsius is {C:.2f}")

# convert_cel_to_far()
# convert_far_to_cel()
######################################################################
for a in range(2,10):
    print(a,sep="\n")
####################################program to double the number for 3 iterations################################

def double(i):
    n=0
    while (n<3):
        i=i+i
        print(i,sep="\n")
        n=n+1

# j=int((input("enter a num:")))
# double(j)

def invest (p,i,t):
    for j in range(1,t+1):
        p=p+(p*i)
        print(f"year {j}: ${p:.2f} ")

p=int(input("enter principal:"))
i=float(input("enter intrest:"))
t=int(input("enter tenure:"))
invest(p,i,t)