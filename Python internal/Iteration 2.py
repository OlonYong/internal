#Define Values
order = []
total = 0
loggedin = True
menu = {
    1 : ["HOT LUNCHES", [
        ["Hot Noodles", 3.80], 
        ["Spaghetti Bun", 1.50], 
        ["Garlic Bread" , 2.00], 
        ["Hot Dogs", 4.00], 
        ["Steam Buns", 3.70], 
        ["Peters Pie", 4.80]
    ]],
    2 : ["HEALTHY CHOICES", [
        ["Salads", 7.50], 
        ["Sandwiches", 4.80], 
        ["Sandwiches (Gluten Free)", 5.80], 
        ["Chicken Sub", 4.80], 
        ["Pizza Bread", 3.80], 
        ["Wraps", 5.50]
    ]],
    3 : ["SNACKS AND FROZEN", [
        ["Potato chips", 2.50], 
        ["Mrs Higgins Cookies", 3.80], 
        ["Juicies", 1.00], 
        ["Coconut Juicies", 2.50], 
        ["Moosies", 2.00], 
        ["Slushies", 2.50]
    ]],
    4: ["DRINKS", [
        ["Water", 2.50], 
        ["Lipton Ice Tea", 4.50], 
        ["Aloe Ice Tea", 4.50], 
        ["Barista Bros Chocolate", 4.50], 
        ["Hot Chocolate", 2.50], 
        ["Powerade", 4.50]
    ]]
}

#User Login
while loggedin:
    try:
        choice = int(input("Would you like to\n1. Login\n2. Register account\nYour Entry: "))
        if choice == 1:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            with open("Internal assessment/Iteration 2/saved.txt", "r") as file:
                for line in file:
                    if name == line.split(" : ")[0] and password == line.split(" : ")[1]:
                        loggedin = False
                        break
                else:
                    input("Incorrect username or password\n")
        elif choice == 2:
            name = input("Enter a username: ")
            password = input("Enter a password: ")
            age = int(input("Enter your age: "))
            if not (13 <= age <= 18):
                print("You must be between 13 and 18 years old")
                quit()
            else:
                with open("Internal assessment/Iteration 2/saved.txt", "a") as f:
                    f.write(f"{name} : {password} : {age}\n")                
                input("Account Created!\n")
                break
    except ValueError:
        print("Please enter an integer")

#Main program
while True:
    try:
        choice = int(input("\nBDSC Cafe click and collect\n1. Hot food\n2. Cold food\n3. Snacks\n4. Drinks\n5. Finish order\n6. Discard order\nYour Entry: "))
        if 1 <= choice <= 4:
            title = f"~~~~~~~~~~~~~~~\n{menu[choice][0]}\n~~~~~~~~~~~~~~~\n"
            for i in range(6):
                title += f"{i+1}. {menu[choice][1][i][0]} - ${menu[choice][1][i][1]:.2f}\n"
            title += "7. Exit"
            choice2 = int(input(f"{title}\nYour Entry: "))
            count = int(input("How many: "))
            order.append(f"{menu[choice][1][choice2-1][0]} x{count}")
            total += menu[choice][1][choice2-1][1] * count
        elif choice == 5:
            break
        elif choice == 6:
            quit()
        else:
            input("INVALID")
    except ValueError:
        input("INVALID INTEGER (enter to continue) ")
print(f"Your order is {', '.join(order)} to a total of ${total:.2f}")