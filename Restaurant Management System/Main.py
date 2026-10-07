from Food_item import FoodItem
from menu import Menu 
from Users import Customer, Employee, Admin
from orders import Order
from restaurant import Restaurant

mamar_restaurant = Restaurant("Mamar Restaurant")

def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your E-mail: ")
    phone = input("Enter Your Phone Number: ")
    address = input("Enter Your Address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)


    while True:
        print(f"WelCome {customer.name}!!")
        print("1. View Menu")
        print("2. Add Item To Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")


        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        
        elif choice == 3:
            customer.view_cart()
        
        elif choice == 4:
            customer.pay_bill()
        
        elif choice == 5:
            break
        
        else:
            print("Invalid Input")



def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your E-mail: ")
    phone = input("Enter Your Phone Number: ")
    address = input("Enter Your Address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)


    while True:
        print(f"WelCome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")


        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurant, item)
        
        elif choice == 2:
            name = input("Enter employee name: ")
            phone = input("Enter employee phone: ")
            email = input("Enter employee e-mail: ")
            designation = input("Enter employee designation: ")
            age = input("Enter employee age: ")
            salary = input("Enter employee salary: ")
            address = input("Enter employee address: ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(mamar_restaurant, employee)
            
        
        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_restaurant, item_name)

        elif choice == 6:
            break
        
        else:
            print("Invalid Input")


while True:
    print("Welcome !!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")