#Dictionary
menu={"Spaggeti":"10$","Kebab":"15$","steak":"25$","biryani":"12$","sushi":"17$","kfc":"14$"}

def print_menu():
    print("spaggeti")
    print("kebab")
    print("steak")
    print("briyani")
    print("sushi")
    print("kfc")
    
def search_menu(food):
    if(food in menu):
        print(f"You Selected '{food}' and it's price is: '{menu[food]}', Your order has been submitted.")
    else:
        print("we don't have this food")    
