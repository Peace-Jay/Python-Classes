pizza_orders = {
    "order_owners" : ["Basit", "Peace", "Emmanuel"],
    "order_numbers" : ["OR-001", "OR-002", "OR-003"],
    "order_time" : [9, 6, 4]
}

pizza_orders_2 =[
    {
        "order_owner" : "Basit",
        "order_number" : "OR-001",
        "order_time" : 9
    },
    {
        "order_owner" : "Peace",
        "order_number" : "OR-002",
        "order_time" : 6
    },
    {
        "order_owner" : "Emmanuel",
        "order_number" : "OR-003",
        "order_time" : 4
    }
]

user_name = input("Please what is your name: ")

if user_name in pizza_orders["order_owners"]:
    order_index = pizza_orders["order_owners"].index(user_name)
    print(f"Welcome {user_name}, your order number is {pizza_orders['order_numbers'][order_index]} and your order time is {pizza_orders['order_time'][order_index]}")
else:
    print(f"Sorry no order found for {user_name}")

"""
ord_num = 0
for order in pizza_orders_2:
    if order["order_owner"] == user_name:
        ord_num = pizza_orders_2.index(order)
        print(pizza_orders_2[ord_num])
        
        print(f"Welcome {pizza_orders_2[ord_num]['order_owner']} your order number is {pizza_orders_2[ord_num]['order_number']} and your order will be ready in {pizza_orders_2[ord_num]['order_time']} minutes")
        """