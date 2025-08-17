menu = {
    'pizza':40,
    'passta':30,
    'bargar':50,
    'coffe':20
}



print("welcome to python restaurent")

print("pizza:Rs40 \n passta:30 \n bargar:50 \n coffe:20" )


order_total = 0



item1 = input("enter your order = ")

if item1 in menu:
    order_total += menu[item1]
    print(f"your item {item1} hass be added")
else:
    print(f"order item {item1} not available")



anther_order = input("you want to add anther item (Y/N)")

if anther_order == "y":
    item2 = input("enter item to add")
    if item2 in menu:
        order_total += menu[item2]
        print(f"item {item2} is added")
    else:
        print(f"item is not{item2} avaialable")



print(f"total amount to pay{order_total}")


