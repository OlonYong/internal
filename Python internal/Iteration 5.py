from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
window = Tk()
window.config(bg="white")
user = ""
password = ""
order= []
total = 0
menu = {
    "Hot Noodles" : [3.80, "Instant noodles in a cup (chicken beef, or spicy)", "noodles.png"], 
    "Spaghetti Bun" : [1.50, "Spaghetti tossed in a flavorful sauce and served between soft buns", "spaghetti.png"], 
    "Garlic Bread" : [2.00, "Freshly baked bread infused with aromatic garlic and butter, toasted to perfection", "garlicbread.png"], 
    "Hot Dogs" : [4.00, "Juicy sausages served in a soft bun", "hotdog.png"], 
    "Steam Buns" : [3.70, "Soft and fluffy steamed buns filled with various savory fillings", "steambuns.png"], 
    "Peters Pie" : [4.80, "Savory pies with a flaky crust and a meat filling", "pie.png"],
    "Salads" : [7.50, "Fresh and crisp salad greens topped with a variety of vegetables, proteins, and dressings", "salad.png"],
    "Sandwiches" : [4.80, "Made with fresh bread and filled with a selection of meats, cheeses, and vegetables", "sandwiches.png"], 
    "Sandwiches (Gluten Free)" : [5.80, "Gluten-free bread filled with a selection of meats, cheeses, and vegetables", "gluten.png"], 
    "Chicken Sub" : [4.80, "A hearty sandwich filled with tender grilled chicken and fresh vegetables", "chickensub.png"], 
    "Pizza Bread" : [3.80, "Bread topped with cheese, tomato sauce, and various toppings for a pizza-like flavor", "pizzabread.png"], 
    "Wraps" : [5.50, "Soft tortilla wraps filled with a variety of ingredients", "wrap.png"],
    "Potato chips" : [2.50, " Crispy and flavorful potato chips", "chips.png"], 
    "Mrs Higgins Cookies" : [3.80, "Delicious chocolate chip cookies", "cookies.png"], 
    "Juicies" : [1.00,"Refreshing fruit juice frozen into a convenient and delicious ice block, available in various flavors", "juicies.png"], 
    "Coconut Juicies" : [2.50, "Refreshing coconut-flavored ice blocks", "coconut.png"], 
    "Moosies" : [2.00, "Creamy and indulgent ice cream bars", "moosies.png"],
    "Slushies" : [2.50, "Icy and refreshing drinks available in a range of fruity flavors", "slushy.png"],
    "Water" : [2.50, "Pure NZ Spring Water 600ml", "water.png"], 
    "Lipton Ice Tea" : [4.50, "Chilled and refreshing iced tea", "lipton.png"], 
    "Aloe Ice Tea" : [4.50, "A unique blend of iced tea infused with the soothing and refreshing taste of aloe vera", "aloe.png"],
    "Barista Bros Chocolate" : [4.50, "Rich and creamy chocolate milk made with the finest ingredients, providing a decadent and satisfying drink", "barista.png"], 
    "Hot Chocolate" : [2.50, "A comforting and velvety smooth beverage made with warm milk and premium cocoa powder", "chocolate.png"], 
    "Powerade" : [4.50, "A refreshing sports drink designed to replenish electrolytes and provide hydration during physical activities", "powerade.png"]}

def first_menu():
    global initial, login_img, order_img, checkout_img, logo_img, view_img
    initial = Frame(window, bg="white")
    initial.grid(sticky="nsew")
    window.title("BDSC Cafe click and collect")
    window.geometry("500x350")

    title = Label(initial, text="BDSC Cafe Online Order", bg="white", font=("Arial Bold", 20), fg="#781d4b")
    title.grid(row=0, column=1, columnspan=4, padx=25, pady=10, sticky="nsew")

    title2 = Label(initial, text="Main Menu", bg="white", font=("Roboto", 20), fg="#781d4b")
    title2.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(initial, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10)

    order_img = ImageTk.PhotoImage(Image.open("images/order.png").resize((40, 25)))
    order_btn = Button(initial, text="Order food", image=order_img, compound="left", bg="#781d4b", fg="white", width=250, font=("Calibri Bold", 15), command=lambda:[order_screen(), initial.grid_forget()])
    order_btn.grid(row=2, column=1, columnspan=3, pady=10)
    
    checkout_img = ImageTk.PhotoImage(Image.open("images/checkout.png").resize((40, 25)))
    checkout_btn = Button(initial, text="Checkout order", image=checkout_img, compound="left", bg="#781d4b", fg="white", width=250, font=("Calibri Bold", 15), command=lambda: [initial.grid_forget(), checkout()])
    checkout_btn.grid(row=3, column=1, columnspan=3, pady=10)

    login_img = ImageTk.PhotoImage(Image.open("images/login.png").resize((40, 25)))
    login_btn = Button(initial, text="User Login", image=login_img, compound="left", bg="#781d4b", fg="white", width=250, font=("Calibri Bold", 15), command=lambda: [initial.grid_forget(), login()])
    login_btn.grid(row=5, column=1, padx=10, pady=10, columnspan=3)

def main_menu():
    global main, logout_img, order_img, checkout_img, logo_img, view_img
    main = Frame(window, bg="white")
    main.grid(sticky="nsew")
    window.title("BDSC Cafe click and collect")
    window.geometry("500x400")

    title = Label(main, text="BDSC Cafe Online Order", bg="white", font=("Arial Bold", 20), fg="#781d4b")
    title.grid(row=0, column=1, columnspan=4, padx=25, pady=10, sticky="nsew")

    title2 = Label(main, text="Main Menu", bg="white", font=("Roboto", 20), fg="#781d4b")
    title2.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(main, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10)

    order_img = ImageTk.PhotoImage(Image.open("images/order.png").resize((40, 25)))
    order_btn = Button(main, text="Order food", image=order_img, compound="left", bg="#781d4b", fg="white", width=250, font=("Calibri Bold", 15), command=lambda:[order_screen(), main.grid_forget()])
    order_btn.grid(row=2, column=1, columnspan=3, pady=10)

    checkout_img = ImageTk.PhotoImage(Image.open("images/checkout.png").resize((40, 25)))
    checkout_btn = Button(main, text="Checkout order", image=checkout_img, compound="left", bg="#781d4b", fg="white", width=250, font=("Calibri Bold", 15), command=lambda: [main.grid_forget(), checkout()])
    checkout_btn.grid(row=3, column=1, columnspan=3, pady=10)

    logout_img = ImageTk.PhotoImage(Image.open("images/logout.png").resize((40, 25)))
    logout_btn = Button(main, text="Log out", image=logout_img, compound="left", bg="#781d4b", fg="white", width=250, font=("Calibri Bold", 15), command=lambda: [messagebox.showinfo("Logged out!", "Logged out successfully!"), reset(), main.grid_forget(), first_menu()])
    logout_btn.grid(row=5, column=1, padx=10, pady=10, columnspan=3)

def order_screen():
    global item_img, hotmenu, logo_img, checkout_img
    hotmenu = Frame(window, bg="white")
    hotmenu.grid(sticky="nsew")
    window.title("Order food")
    window.geometry("650x400")

    title = Label(hotmenu, text="BDSC Cafe Online Order", bg="white", font=("Arial Bold", 20), fg="#781d4b")
    title.grid(row=0, column=1, columnspan= 3, pady=10, sticky="w")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(hotmenu, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")
    
    title2 = Label(hotmenu, text="Add to order", bg="white", font=("Roboto", 20), fg="#781d4b")
    title2.grid(row=1, padx=10, pady=10, columnspan=2)

    subgrid = Frame(hotmenu, bg="white")
    subgrid.grid(row=2, columnspan=2, padx=10, pady=10)

    combo = ttk.Combobox(subgrid, values=[f"{item} - ${price:.2f}" for item, [price, _, _] in menu.items()], width=30, font=("Arial", 12))
    combo.grid(row=1, column=0, padx=10, pady=10)
    combo.bind("<<ComboboxSelected>>", lambda event: description(combo, info, item_lbl))
    combo.insert(0, "Select an item")

    number = Spinbox(subgrid, from_=1, to=999, width=3, font=("Arial", 12))
    number.grid(row=1, column = 1, pady=10)

    item_lbl = Label(hotmenu, bg="white")
    item_lbl.grid(row=1, rowspan=3, column=3, pady=10)

    info = Label(hotmenu, text="", bg="white", wraplength=250, fg="#781d4b", font=("Arial", 12))
    info.grid(row=3, rowspan=3, column=2, columnspan=3, padx=10, pady=10)

    add_btn = Button(hotmenu, text="Add to order", command=lambda: add_item(combo, number, message), bg="#781d4b", fg="white", font=("Calibri Bold", 12))
    add_btn.grid(row=3, columnspan=2, pady=10)

    message = Label(hotmenu, text="", bg="white", fg="#781d4b", font=("Arial", 12))
    message.grid(row=4, columnspan=2, pady=10)

    checkout_img = ImageTk.PhotoImage(Image.open("images/checkout.png").resize((40, 25)))
    checkout_btn = Button(hotmenu, text="Checkout", image=checkout_img, compound="left", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: [hotmenu.grid_forget(), checkout()])
    checkout_btn.grid(row=5, columnspan=2, pady=10)

    back_btn = Button(hotmenu, text="Back", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: back_menu(frame=hotmenu))
    back_btn.grid(row=5, column=0, pady=10, sticky="w", padx=30)

def description(combo, info, item_lbl):
    global item_img
    item = (combo.get()).split(" - ")[0]
    if item != "":
        info.config(text=menu[item][1], justify="left")
        item_img = ImageTk.PhotoImage(Image.open(f"images/{menu[item][2]}").resize((250, 150)))
        item_lbl.config(image=item_img, bg="Purple")

def add_item(combo, number, message):
    global order
    global total
    item = (combo.get()).split(" - ")[0]
    count = int(number.get())
    if item != "Select an item":
        order.append(f"{count}x {item}")
        total += menu[item][0] * count
        message.configure(text=f"{count}x {item} added to order")
    else:
        message.configure(text="Please select an item")

def login():
    global loginwindow, logo_img
    loginwindow = Frame(window, bg="white")
    loginwindow.grid(sticky="nsew")
    window.title("Login")
    window.geometry("500x400")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(loginwindow, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")

    title = Label(loginwindow, text="BDSC Cafe Online Order", fg="#781d4b", bg="white", font=("Arial Bold", 20))
    title.grid(row=0, column=1, columnspan=2, sticky="nsew")

    title2 = Label(loginwindow, text="Login", bg="white", fg="#781d4b", font=("Comic Sans MS", 20))
    title2.grid(row=1, column=1, padx=10, columnspan=2)

    username = Label(loginwindow, text="Username", fg="#781d4b", bg="white", font=("Calibri Bold Bold", 15))
    username.grid(row=2, column=1, padx=10, pady=10)
    username_entry = Entry(loginwindow,font=("Calibri Bold", 12), highlightthickness=2, highlightbackground="#781d4b")
    username_entry.grid(row=2, column=2, padx=10, pady=10)

    password = Label(loginwindow, text="Password", fg="#781d4b", bg="white", font=("Calibri Bold Bold", 15))
    password.grid(row=3, column=1, padx=10, pady=10)
    password_entry = Entry(loginwindow, font=("Calibri Bold", 12), highlightthickness=2, highlightbackground="#781d4b")
    password_entry.grid(row=3, column=2, padx=10, pady=10)

    messages = Label(loginwindow, fg="#781d4b", bg="white", font=("Calibri Bold", 15))
    messages.grid(row=4, columnspan=3, pady=10)

    login_btn = Button(loginwindow, text="Login", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: check_login(username_entry, password_entry, messages))
    login_btn.grid(row=5, column=1, columnspan=2, pady=10)

    register_btn = Button(loginwindow, text="Register", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: [loginwindow.grid_forget(), register()])
    register_btn.grid(row=5, column=2, pady=10, padx=20, sticky="e")

    back_btn = Button(loginwindow, text="Back", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: back_menu(frame=loginwindow))
    back_btn.grid(row=6, column=1, columnspan=2, pady=10)  

def check_login(username_entry, password_entry, messages):
    global user, password
    user = username_entry.get()
    password = password_entry.get()
    try:
        with open("saved.txt", 'r') as file:
            if len(file.read()) == 0:
                messages.config(text="No accounts saved. Please register an account")
        with open("saved.txt", 'r') as file:
            for line in file:
                if user in line:
                    if user == line.split(" : ")[0] and password == line.split(" : ")[1].strip():
                        loginwindow.grid_forget()
                        main_menu()
                        break
                    else:
                        messages.config(text="Incorrect credentials. Please try again")
    except IOError:
        messages.config(text="No accounts saved. Please register an account")
        with open("saved.txt", 'w') as file:
            file.close()

def register():
    global registerwindow, logo_img
    registerwindow = Frame(window, bg="white")
    registerwindow.grid(sticky="nsew")
    window.title("Register")
    window.geometry("500x460")
    initial.grid_forget()

    title = Label(registerwindow, text="BDSC Cafe Online Order", bg="white", font=("Arial Bold", 20), fg="#781d4b")
    title.grid(row=0, column=1, columnspan= 3, padx=5, pady=10, sticky="nsew")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(registerwindow, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")

    title2 = Label(registerwindow, text="Register account", bg="white", fg="#781d4b", font=("Comic Sans MS", 20))
    title2.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    username = Label(registerwindow, text="Username", bg="white", fg="#781d4b", font=("Calibri Bold Bold", 15))
    username.grid(row=2, column=1, padx=10, pady=10)
    username_entry = Entry(registerwindow, bg="white", font=("Calibri Bold Bold", 12), highlightthickness=2, highlightbackground="#781d4b")
    username_entry.grid(row=2, column=2, padx=10, pady=10)

    password = Label(registerwindow, text="Password", bg="white", fg="#781d4b", font=("Calibri Bold Bold", 15))
    password.grid(row=3, column=1, padx=10, pady=10)
    password_entry = Entry(registerwindow, bg="white", font=("Calibri Bold", 12), highlightthickness=2, highlightbackground="#781d4b")
    password_entry.grid(row=3, column=2, padx=10, pady=10)

    age = Label(registerwindow, text="Age", bg="white", fg="#781d4b", font=("Calibri Bold Bold", 15))
    age.grid(row=4, column=1, padx=10, pady=10)
    age_entry = Spinbox(registerwindow, bg="white",font=("Calibri Bold", 12), from_=1, to=100, highlightthickness=2, highlightbackground="#781d4b")
    age_entry.grid(row=4, column=2, padx=10, pady=10)

    message = Label(registerwindow, text="", bg="white", fg="#781d4b", font=("Calibri Bold Bold", 15))
    message.grid(row=5, columnspan=3, pady=10)

    register_btn = Button(registerwindow, text="Register", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: register_account(username_entry, password_entry, age_entry, message))
    register_btn.grid(row=6, column=1, columnspan=2, pady=10)

    login_btn = Button(registerwindow, text="Login", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: [registerwindow.grid_forget(), login()])
    login_btn.grid(row=6, column=2, pady=10, padx=20, sticky="e")

    back_btn = Button(registerwindow, text="Back", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: back_menu(frame=registerwindow))
    back_btn.grid(row=7, column=1, columnspan=2, pady=10)  

def register_account(username_entry, password_entry, age_entry, message):
    user = username_entry.get()
    password = password_entry.get()
    age = int(age_entry.get())
    if user != "" and password != "":
        if 13 <= age <= 18:
            while True:
                try:
                    with open("saved.txt", 'a') as file:
                        file.write(f"{user} : {password} : {age}\n")
                        file.close()
                        message.config(text="Account created successfully")
                        registerwindow.grid_forget()
                        main_menu()
                        break
                except IOError:
                    with open("saved.txt", 'w') as file:
                        file.close()
        else:
            message.config(text="You are not eligible to register an account")
    else:
        message.config(text="Please fill in all the boxes")

def back_menu(frame):
    frame.grid_forget()
    accountcheck()
    
def accountcheck():
    if user == "" or password == "":
        first_menu()
    else:
        main_menu()

def view_order():
    global viewwindow, logo_img
    viewwindow = Frame(window, bg="white")
    viewwindow.grid(sticky="nsew")
    window.title("View order")
    window.geometry("530x400")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(viewwindow, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")

    title = Label(viewwindow, text="BDSC Cafe Online Order", font=("Arial Bold", 20), fg="#781d4b", bg="white")
    title.grid(row=0, column=1, columnspan= 3, padx=5, pady=10, sticky="nsew")   

    title2 = Label(viewwindow, text="Your Order is:", font=("Comic Sans MS", 15), fg="#781d4b", bg="white")
    title2.grid(row=1, column=1, columnspan=3, sticky="nsew")
    orders = ""
    for item in order:
        orders += f"{item}\n"
    Label(viewwindow, text=orders.strip(), font=("Comic Sans MS", 10), bg="white", fg="#781d4b").grid(row=2, column=1, columnspan=3, sticky="nsew", pady=10)
    Label(viewwindow, text=f"Total: ${total:.2f}", font=("Comic Sans MS", 10), bg="white", fg="#781d4b").grid(row=3, column=1, columnspan=3, sticky="nsew", pady=10)

    back = Button(viewwindow, text="Back", command=lambda: [viewwindow.pack_forget(), back_menu(frame=viewwindow)], bg="#781d4b", fg="white", font=("Calibri Bold", 12))
    back.grid(row=4, column=1, columnspan=3, pady=10, sticky="nsew")

def checkout():
    if user == "" or password == "":
        login()
        messagebox.showerror("Error", "Please login or register an account first.")
        return()
    global checkoutwindow, logo_img
    checkoutwindow = Frame(window, bg="white")
    checkoutwindow.grid(sticky="nsew")
    window.title("View order")
    window.geometry("530x400")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(checkoutwindow, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")

    title = Label(checkoutwindow, text="BDSC Cafe Online Order", font=("Arial Bold", 20), fg="#781d4b", bg="white")
    title.grid(row=0, column=1, columnspan= 3, padx=5, pady=10, sticky="nsew")   

    title2 = Label(checkoutwindow, text="Checkout", font=("Comic Sans MS", 15), fg="#781d4b", bg="white")
    title2.grid(row=1, column=1, columnspan=3, sticky="nsew")

    subheading = Label(checkoutwindow, text="Your order is:", font=("Comic Sans MS", 10), bg="white", fg="#781d4b")
    subheading.grid(row=2, column=1, columnspan=3, sticky="nsew", pady=10)

    orders = ""
    if order != []:
        for item in order:
            orders += f"{item}\n"
        Label(checkoutwindow, text=orders.strip(), font=("Comic Sans MS", 10), bg="white", fg="#781d4b").grid(row=2, column=1, columnspan=3, sticky="nsew", pady=10)
        Label(checkoutwindow, text=f"Total: ${total:.2f}", font=("Comic Sans MS", 10), bg="white", fg="#781d4b").grid(row=3, column=1, columnspan=3, sticky="nsew", pady=10)
        confirm = Button(checkoutwindow, text="Confirm order", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: [checkoutwindow.grid_forget(), finish()])
        confirm.grid(row=4, column=1, columnspan=3, pady=10, sticky="nsew")
    else:
        Label(checkoutwindow, text="You have not ordered anything", font=("Comic Sans MS", 10), bg="white", fg="#781d4b").grid(row=3, column=1, columnspan=3, sticky="nsew", pady=10)

    back = Button(checkoutwindow, text="Back", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: [checkoutwindow.grid_forget(), back_menu(frame=checkoutwindow)])
    back.grid(row=5, column=1, columnspan=3, pady=10, sticky="nsew")

#This screen is shown when the user completes their order.
def finish():
    global completed, logo_img
    completed = Frame(window, bg="white")
    completed.grid(sticky="nsew")
    window.title("View order")
    window.geometry("550x400")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(completed, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")

    title = Label(completed, text="BDSC Cafe Online Order", font=("Arial Bold", 20), fg="#781d4b", bg="white")
    title.grid(row=0, column=1, columnspan= 3, padx=5, pady=10, sticky="nsew")   

    title2 = Label(completed, text="Checkout", font=("Comic Sans MS", 15), fg="#781d4b", bg="white")
    title2.grid(row=1, column=1, columnspan=3, sticky="nsew")

    Label(completed, text="Your order has been confirmed and will be ready for pickup", font=("Comic Sans MS", 12), bg="white", fg="#781d4b").grid(row=2, column=1, columnspan=3, sticky="nsew", pady=10)
    
#Brings the user to the first frame so they can order again if they wish
    home = Button(completed, text="Home", bg="#781d4b", fg="white", font=("Calibri Bold", 12), command=lambda: [completed.grid_forget(), first_menu()])
    home.grid(row=3, column=1, columnspan=3, pady=10, sticky="nsew")

def reset():
    global order, total, user, password
    order = []
    total = 0
    user = ""
    password = ""

first_menu()
window.mainloop()