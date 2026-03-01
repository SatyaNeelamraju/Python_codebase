######################################## identifying the scope of each variable LEGB #################################
#Local, Enclosing, Global, built-in

def explore_basement():
    def explore_cabinet():
        cabinet_items = ["keys", "sunglasses"]
        print(f"Local:{cabinet_items}")
    
    basement_items = ["bed" , "cabinet"]
    explore_cabinet()
    print(f"Enclosing: {basement_items}")

address = "Python Palace"
explore_basement()
print(f"Global:{address}") #print is the built in function 

############################################## find out expected output ##############################################################
print("-------------------------------------------------------")

def explore_basement():
    def explore_cabinet():
        address="Cookie Cabinet"
        print(address)
    
    address="Mouse House"
    explore_cabinet()
    print(address)

address = "Python Palace"
explore_basement()
print(address)

#Cookie Cabinet, Mouse House, Python Palace
print("-----------------------------------------------------")

def explore_basement():
    def explore_cabinet():
        global address
        address="Cookie Cabinet"
        print(address)
    
    address="Mouse House"
    explore_cabinet()
    print(address)

address = "Python Palace"
explore_basement()
print(address)

# The address variable with Python Palace value is a global scope variable. whenever the program encounters global key word for address variable
# the previous global variable value is also updated to the latest no change to other variables which are not in global scope

print(locals())
print(globals())

def explore_basement():
    def explore_cabinet():
        global address
        address="Cookie Cabinet"
        print(address)
    
    address="Mouse House"
    explore_cabinet()
    print(address)

def visit_woods():
    my_invitation="Welcome to the party"
    if "my_invitation" in locals():
        print(my_invitation)


address = "Python Palace"
explore_basement()
print(address)
visit_woods()

