method_list = {
    "1": "quantity_available",
    "2": "sell_petrol",
    "3": "refill_petrol",
    "4": "amount_of_sales",
    "5": "exit_station"
}
sales = []


username = "Peace_Jay"
Password = "5555"
class Petrol:
    def __init__(self, petrol_quantity):
        self.quantity = petrol_quantity
        self.sales = []

    def quantity_available(self):
        print(f"The total quantity of petrol avalaible  is {self.quantity}")

    def sell_petrol(self):
        customer_name = input("what is your name?")
        try:
            customer_order = int(input("what is the quantity of petrol you want?"))
            customers = {
                "names": customer_name,
                "orders": customer_order,
                "status": "pending"
            }

            if customer_order <= self.quantity:
                print("sell to customer")
                self.quantity = self.quantity - customer_order
                customers_update = {"status":"successful"}
                customers.update(customers_update)
                print(f"{customer_order} litres of petrol successfully sold to {customer_name}")
            else:
                print("insufficient petrol")
            sales.append(customers)
        except ValueError:
            print("no fuel")


    def refill_petrol(self):
        login_name = input("What is your name?")
        login_password = input("Enter Password")
        if login_name == username:
            print("okay")
            if login_password == Password:
                refill_quantity = int(input("How much do you want to add to the tank?"))
                self.quantity = self.quantity + refill_quantity
                print(f"{refill_quantity} successfully added to the tank")
                print(f"The the quantity of petrol in the tank is {self.quantity}")
        else:
            print("You are not authorized to refill")



    def amount_0f_sales(self):
        print(sales)

    def exit_station(self):
        print("exit")

Total = Petrol(30000)
while True:
    print("************WELCOME*************")
    print("\n Petrol Station Services")
    print("1.quantity_available")
    print("2.sell_petrol")
    print("3.refill_petrol")
    print("4.amount_of_sales")
    print("5. exit_station")


    response = input("which of the services do you want?")
    if response == "5":
        break
    elif response == "1":
        Total.quantity_available()
    elif response == "2":
        Total.sell_petrol()
    elif response == "3":
        Total.refill_petrol()
    elif response == "4":
        Total.amount_0f_sales()
    else:
        print("Invalid input")
