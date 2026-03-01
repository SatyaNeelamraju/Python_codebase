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

# Updating the Cookie Cabinet in last line to return Mouse House

print("new_output:")

def explore_basement():
    def explore_cabinet():
        address="Cookie Cabinet"
        print(address)
    
    address="Mouse House"
    explore_cabinet()
    print(address)
    return address

address = "Python Palace"
print(explore_basement())


