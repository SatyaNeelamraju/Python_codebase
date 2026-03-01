#maing using of locals

# def visit_woods(my_invitation):
#     if "my_invitation" in locals():
#         print(my_invitation)

# invitation="Welcome to the party"
# visit_woods(invitation)

#collect all cookies 

def on_the_shelf():
    shelf_cookies=["Peanut","Choclate"]
    return shelf_cookies

def under_the_sofa():
    sofa_cookies =["Oat","Salted Caramel"]
    return sofa_cookies

cookies=on_the_shelf()+under_the_sofa()
print(cookies)