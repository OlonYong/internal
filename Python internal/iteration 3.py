#Import Modules
from tkinter import *
from tkinter import ttk
window = Tk()

#Define the menu with the item, price, and description.
menu = {
    "Hot Noodles" : [3.80, "Instant noodles in a cup (chicken beef, or spicy)"], 
    "Spaghetti Bun" : [1.50, "Spaghetti tossed in a flavorful sauce and served between soft buns"], 
    "Garlic Bread" : [2.00, "Freshly baked bread infused with aromatic garlic and butter, toasted to perfection"], 
    "Hot Dogs" : [4.00, "Juicy sausages served in a soft bun"], 
    "Steam Buns" : [3.70, "Soft and fluffy steamed buns filled with various savory fillings"], 
    "Peters Pie" : [4.80, "Savory pies with a flaky crust and a meat filling"],
    "Salads" : [7.50, "Fresh and crisp salad greens topped with a variety of vegetables, proteins, and dressings"], 
    "Sandwiches" : [4.80, "Made with fresh bread and filled with a selection of meats, cheeses, and vegetables"], 
    "Sandwiches (Gluten Free)" : [5.80, "Gluten-free bread filled with a selection of meats, cheeses, and vegetables"], 
    "Chicken Sub" : [4.80, "A hearty sandwich filled with tender grilled chicken and fresh vegetables"], 
    "Pizza Bread" : [3.80, "Bread topped with cheese, tomato sauce, and various toppings for a pizza-like flavor"], 
    "Wraps" : [5.50, "Soft tortilla wraps filled with a variety of ingredients"],
    "Potato chips" : [2.50, " Crispy and flavorful potato chips"], 
    "Mrs Higgins Cookies" : [3.80, "Delicious chocolate chip cookies"], 
    "Juicies" : [1.00,"Refreshing fruit juice frozen into a convenient and delicious ice block, available in various flavors"], 
    "Coconut Juicies" : [2.50, "Refreshing coconut-flavored ice blocks"], 
    "Moosies" : [2.00, "Creamy and indulgent ice cream bars"],
    "Slushies" : [2.50, "Icy and refreshing drinks available in a range of fruity flavors"],
    "Water" : [2.50, "Pure NZ Spring Water 600ml"], 
    "Lipton Ice Tea" : [4.50, "Chilled and refreshing iced tea"], 
    "Aloe Ice Tea" : [4.50, "A unique blend of iced tea infused with the soothing and refreshing taste of aloe vera"],
    "Barista Bros Chocolate" : [4.50, "Rich and creamy chocolate milk made with the finest ingredients, providing a decadent and satisfying drink"], 
    "Hot Chocolate" : [2.50, "A comforting and velvety smooth beverage made with warm milk and premium cocoa powder"], 
    "Powerade" : [4.50, "A refreshing sports drink designed to replenish electrolytes and provide hydration during physical activities"]}

#First frame is used for login/register account. 
def frames1():
    global frame1
    frame1 = Frame(window)
    frame1.pack()
    window.title("Login")
    window.geometry("530x400")

#Define useful veriables for later use
    global order
    global total
    order = [] 
    total = 0

    title = Label(frame1, text="BDSC Cafe click and collect",font=("Comic Sans MS Bold", 20), pady=10)
    title.pack()

    username = Label(frame1, text="Username", pady=10)
    username.pack()

    username_entry = Entry(frame1)
    username_entry.pack()

    password = Label(frame1, text="Password", pady=10)
    password.pack()

    password_entry = Entry(frame1)
    password_entry.pack()

    logins = Button(frame1, text="Login", command=lambda: login(username_entry, password_entry, message))
    logins.pack(pady=10, padx=10)

    register = Button(frame1, text="Register account", command=lambda: registers(username_entry, password_entry, logins, register, message))
    register.pack(pady=10, padx=10)

    message = Label(frame1, text="")
    message.pack()

#Second frame is used for the menu where the user can either order, view their order, or checkout
def frames2():
    global frame2
    frame2 = Frame(window)
    frame2.pack()
    window.title("menu")
    window.geometry("530x400")
    frame1.pack_forget()

    title = Label(frame2, text="BDSC Cafe click and collect",font=("Comic Sans MS Bold", 20), pady=10)
    title.pack()

    logins = Button(frame2, text="Order", command=frames3)
    logins.pack(pady=10)

    view_orders = Button(frame2, text="View Order", command=view_order)
    view_orders.pack(pady=10)

    checkout = Button(frame2, text="Checkout", command=checkouts)
    checkout.pack(pady=10)

#Third frame is used for ordering food.
def frames3():
    global frame3
    global combo
    global number
    frame3 = Frame(window)
    frame3.pack()
    window.title("order food")
    window.geometry("530x400")
    frame2.pack_forget()

    title = Label(frame3, text="BDSC Cafe click and collect",font=("Comic Sans MS Bold", 20), pady=10)
    title.pack()

    title2 = Label(frame3, text="Order food", font=("Comic Sans MS", 15))
    title2.pack(padx=10, pady=10)   

#Another frame is used to position the spin box and combo box
    inner_frame = Frame(frame3)
    inner_frame.pack()

#Users can choose their desired item and quantity using a combo box and spin box
    combo = ttk.Combobox(inner_frame, values=[f"{item} - ${price:.2f}" for item, [price, _] in menu.items()], width=30)
    combo.pack(side=LEFT)
    combo.bind("<<ComboboxSelected>>", lambda event: description(combo, info))
    combo.insert(0, "Select an item")
    number = Spinbox(inner_frame, from_=1, to=999, width=3)
    number.pack(side=LEFT, padx=10)

    info = Label(frame3, text="")
    info.pack()

    add = Button(frame3, text="Add to order", command=lambda: add_item(message))
    add.pack(pady=10)
#Return to the second frame
    back = Button(frame3, text="Back", command=lambda: [frame3.pack_forget(), frames2()])
    back.pack()
#Give the user a description of the item they have selected
    message = Label(frame3, text="")
    message.pack()

#Function used to check whether the user credentials are valid
def login(username_entry, password_entry, message):
    with open("saved.txt", "r") as file:
        for line in file:
            if username_entry.get() == line.split(" : ")[0] and password_entry.get() == line.split(" : ")[1]:
                frames2()
                break
            else:         
                message.config(text="Incorrect username or password")

#Function used to register a new account
def registers(username_entry, password_entry, logins, register, message):  
    logins.pack_forget()
    register.pack_forget()
    message.pack_forget()

    age = Label(frame1, text="Age")
    age.pack(pady=10)
    age_entry = Spinbox(frame1, from_=1, to=999, width=5)
    age_entry.pack(padx=10)

    register = Button(frame1, text="Create account", command=lambda: create_account(username_entry, password_entry, age_entry, message))
    register.pack(pady=20, padx=10)

    message = Label(frame1, text="")
    message.pack()

#Function used to create a new account and save into a text file
def create_account(username_entry, password_entry, age_entry, message):
    user = username_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    if user == "" or password == "" or age == "":
        message.config(text="Please fill in all fields")
    else:
        if int(age) < 13 or int(age) > 18:
            message.config(text="You must be 13 to 18 to create an account")
        else:
            with open("saved.txt", "a") as f:
                f.write(f"{user} : {password} : {age}\n")                
                frames2()

#Function used to show the description of the item the user has selected
def description(combo,info):
    item = combo.get()
    item = item.split(" - ")[0]
    if item !="":
        info.config(text=menu[item][1])

#Function used to add an item to the user's order
def add_item(message):
    global order
    global total
    item = combo.get()
    count = number.get()
    if item != "Select an item":
        item, price = item.split(" - ")
        order.append(f"{count}x {item}")
        total += float(price.strip("$"))
        message.configure(text=f"{count}x {item} added to order")
    else:
        message.configure(text="Please select an item")

#Function used to view the user's order
def view_order():
    global frame4
    frame4 = Frame(window)
    frame4.pack()
    window.title("View order")
    window.geometry("530x400")
    frame2.pack_forget()

    view = Label(frame4, text="View Order", font=("Comic Sans MS", 15))
    view.pack(padx=10, pady=10)   
    for item in order:
        Label(frame4, text=item).pack()

    Label(frame4, text=f"Total: ${total:.2f}").pack()

    back = Button(frame4, text="Back", command=lambda: [frame4.pack_forget(), frames2()])
    back.pack()

#Function used to finish the user's order
def checkouts():
    global frame5
    frame5 = Frame(window)
    frame5.pack()
    window.title("Checkout")
    window.geometry("530x400")
    frame2.pack_forget()

    titles = Label(frame5, text="Checkout", font=("Comic Sans MS", 15))
    titles.pack(padx=10, pady=10)   

    title = Label(frame5, text="Your order is:",font=("Comic Sans MS", 10), pady=10)
    title.pack()

    for item in order:
        Label(frame5, text=item).pack()

    Label(frame5, text=f"Total: ${total:.2f}").pack()

    if order != []:
        confirm = Button(frame5, text="Confirm order", command=lambda: [frame5.pack_forget(), finish()])
        confirm.pack(pady=10)

    back = Button(frame5, text="Back", command=lambda: [frame5.pack_forget(), frames2()])
    back.pack()

#This screen is shown when the user completes their order.
def finish():
    global frame6
    frame6 = Frame(window)
    frame6.pack()
    window.title("Finish")

    titles = Label(frame6, text="Order confirmed", font=("Comic Sans MS", 15))
    titles.pack(padx=10, pady=10)   

    Label(frame6, text="Your order has been confirmed and will be ready for pickup").pack()

#Brings the user to the first frame so they can order again if they wish
    home = Button(frame6, text="Home", command=lambda: [frame6.pack_forget(), frames1()])
    home.pack(pady=10)

frames1()
window.mainloop()