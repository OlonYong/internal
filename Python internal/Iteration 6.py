#Import relevant modules
from tkinter import Tk, Label, Frame, messagebox, Button, Canvas, Scrollbar, Entry, Spinbox, VERTICAL, BOTH
from PIL import ImageTk, Image, ImageFilter, ImageEnhance

#Define important variables used throughout the program
window = Tk()
window.config(bg = "white")
user = ""   #Users login credentials
password = ""   
order = []  #Tracks the user's order
total = 0   #Tracks the total cost of the user's order
cafemenu = {#Contains all the information about the items in the menu
    0 : ["Hot Noodles", 3.80, "Instant noodles in a cup (chicken beef, or spicy)", "noodles.png"], 
    1 : ["Spaghetti Bun", 1.50, "Spaghetti tossed in a flavorful sauce and served between soft buns", "spaghetti.png"], 
    2 : ["Garlic Bread", 2.00, "Freshly baked bread infused with aromatic garlic and butter, toasted to perfection", "garlicbread.png"], 
    3 : ["Hot Dogs", 4.00, "Juicy sausages served in a soft bun", "hotdog.png"], 
    4 : ["Steam Buns", 3.70, "Soft and fluffy steamed buns filled with various savory fillings", "steambuns.png"], 
    5 : ["Peters Pie", 4.80, "Savory pies with a flaky crust and a meat filling", "pie.png"],
    6 : ["Salads", 7.50, "Fresh and crisp salad greens topped with a variety of vegetables, proteins, and dressings", "salad.png"],
    7 : ["Sandwiches", 4.80, "Made with fresh bread and filled with a selection of meats, cheeses, and vegetables", "sandwiches.png"], 
    8 : ["Gluten Free Sandwiches", 5.80, "Gluten-free bread filled with a selection of meats, cheeses, and vegetables", "gluten.png"], 
    9 : ["Chicken Sub", 4.80, "A hearty sandwich filled with tender grilled chicken and fresh vegetables", "chickensub.png"], 
    10 : ["Pizza Bread", 3.80, "Bread topped with cheese, tomato sauce, and various toppings for a pizza-like flavor", "pizzabread.png"], 
    11 : ["Wraps", 5.50, "Soft tortilla wraps filled with a variety of ingredients", "wrap.png"],
    12 : ["Potato chips", 2.50, " Crispy and flavorful potato chips", "chips.png"],
    13 : ["Mrs Higgins Cookies", 3.80, "Delicious chocolate chip cookies", "cookies.png"], 
    14 : ["Juicies", 1.00,"Refreshing fruit juice frozen into a convenient and delicious ice block, available in various flavors", "juicies.png"], 
    15 : ["Coconut Juicies", 2.50, "Refreshing coconut-flavored ice blocks", "coconut.png"], 
    16 : ["Moosies", 2.00, "Creamy and indulgent ice cream bars", "moosies.png"],
    17 : ["Slushies", 2.50, "Icy and refreshing drinks available in a range of fruity flavors", "slushy.png"],
    18 : ["Water", 2.50, "Pure NZ Spring Water 600ml", "water.png"],    
    19 : ["Lipton Ice Tea", 4.50, "Chilled and refreshing iced tea", "lipton.png"], 
    20 : ["Aloe Ice Tea", 4.50, "A unique blend of iced tea infused with the soothing and refreshing taste of aloe vera", "aloe.png"],
    21 : ["Barista Bros Chocolate", 4.50, "Rich and creamy chocolate milk made with the finest ingredients, providing a decadent and satisfying drink", "barista.png"], 
    22 : ["Hot Chocolate", 2.50, "A comforting and velvety smooth beverage made with warm milk and premium cocoa powder", "chocolate.png"], 
    23 : ["Powerade", 4.50, "A refreshing sports drink designed to replenish electrolytes and provide hydration during physical activities", "powerade.png"]}
window.resizable(False, False)

#The navigation bar used to move thorughout the program
def navigation(frame):
    global navbar, logo_img
    navbar = Frame(frame, bg="#5f0137")
    navbar.grid(row=0, column=0, sticky="ew", columnspan=2)

    #Edit the navigation bar to match whether the user is logged in or not
    if user != "":
        label = "Logout"
        command = reset
    else:
        label = "Login"
        command = login

    #The buttons inside the navigation bar    
    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((57,40)))
    logo_lbl = Label(navbar, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    Button(navbar, text="Home", font=("Roboto", 12), bg="#5f0137", fg= "white", command= lambda: [frame.grid_forget(), navbar.grid_forget(), home_page()]).grid(row=0, column=1, pady=10, padx=(25, 65), sticky="ew")
    Button(navbar, text="Hot Food", font=("Roboto", 12), bg="#5f0137", fg= "white", command=lambda: (menu(), frame.grid_forget(), window.after(50, lambda: shortcuts("hot")))).grid(row=0, column=2, pady=10, padx=10, sticky="ew")
    Button(navbar, text="Healthy", font=("Roboto", 12), bg="#5f0137", fg= "white", command=lambda: (menu(), frame.grid_forget(), window.after(50, lambda: shortcuts("healthy")))).grid(row=0, column=3, padx=10, sticky="ew")
    Button(navbar, text="Snacks", font=("Roboto", 12), bg="#5f0137", fg= "white", command=lambda: (menu(), frame.grid_forget(), window.after(50, lambda: shortcuts("snacks")))).grid(row=0, column=4, padx=10, sticky="ew")
    Button(navbar, text="Drinks", font=("Roboto", 12), bg="#5f0137", fg= "white", command=lambda: (menu(), frame.grid_forget(), window.after(50, lambda:  shortcuts("drinks")))).grid(row=0, column=5, padx=10, sticky="ew")
    Button(navbar, text=label, font=("Roboto", 12), bg="#5f0137", fg= "white", command=lambda: (frame.grid_forget(), command())).grid(row=0, column=6, padx=(70, 10), sticky="e")
    Button(navbar, text="Cart", font=("Roboto", 12), bg="#5f0137", fg= "white", command=lambda: [frame.grid_forget(), checkout()]).grid(row=0, column=7, padx=15, sticky="e")

#Function used to scroll to the correct category when the user clicks on the navigation bar
def shortcuts(category):
    placements = {"hot" :0, "healthy" : 0.25, "snacks" : 0.5, "drinks" : 0.75}
    menu_page.yview_moveto(placements[category])
    menu_page.update()

#The main menu page
def home_page():
    #Page setup for home page
    global home, login_img, order_img, logo_img, background
    home = Frame(window, bg="white")
    home.grid(sticky="nsew")
    window.title("BDSC Cafe online order")
    window.geometry("780x400")
    navigation(home)
    background = ImageTk.PhotoImage(Image.open("images/bdsc.jpg").resize((780,400)))
    Label(home, image=background).grid(rowspan=5, columnspan=5, sticky="nsew")
    
    #Change the home page to match whether the user is logged in or not
    if user != "":
        label = "Logout"
        command = reset
    else:
        label = "Login/Register"
        command = login

    #Home screen buttons
    Label(home, text="BDSC Cafe Online Order", bg="White", font=("Arial Bold", 35), fg="#5f0137").grid(row=1, column=0, columnspan=4, padx=25, pady=10, sticky="nsew")
    order_img = ImageTk.PhotoImage(Image.open("images/order.png").resize((40, 25)))
    Button(home, text="Order food", image=order_img, compound="left", bg="#5f0137", fg="white", width=250, font=("Calibri Bold", 25), command=lambda:[home.grid_forget(), menu()]).grid(row=2, column=0, columnspan=4)

    login_img = ImageTk.PhotoImage(Image.open("images/login.png").resize((40, 25)))
    Button(home, text=label, image=login_img, compound="left", bg="#5f0137", fg="white", width=250, font=("Calibri Bold", 25), command=lambda: [home.grid_forget(), command()]).grid(row=3, column=0, pady=10, columnspan=4)

#Brings up the login page
def login():
    #Creates the frame and sets the title for login page
    global loginwindow, logo_img
    loginwindow = Frame(window, bg="white")
    loginwindow.grid(sticky="nsew")
    window.title("Login")
    window.geometry("780x400")
    navigation(loginwindow)

    #Login page widgets
    Label(loginwindow, text="BDSC Cafe Online Order", fg="#5f0137", bg="white", font=("Calibri Bold", 30)).grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)
    Label(loginwindow, text="Login", bg="white", fg="#5f0137", font=("Comic Sans MS", 25)).grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    Label(loginwindow, text="Username", fg="#5f0137", bg="white", font=("Calibri Bold", 15)).grid(row=3, column=0, pady=10, sticky="e")
    username_entry = Entry(loginwindow,font=("Calibri", 12), highlightthickness=2, highlightbackground="#5f0137")
    username_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    Label(loginwindow, text="Password", fg="#5f0137", bg="white", font=("Calibri Bold", 15)).grid(row=4, column=0, sticky="e")
    password_entry = Entry(loginwindow, show="•", font=("Calibri", 12), highlightthickness=2, highlightbackground="#5f0137")
    password_entry.grid(row=4, column=1, padx=10, sticky="w")

    messages = Label(loginwindow, fg="#5f0137", bg="white", font=("Calibri", 15))
    messages.grid(row=5, columnspan=3, pady=10)

    Button(loginwindow, text="Login", bg="#5f0137", fg="white", font=("Calibri", 15), command=lambda: check_login(loginwindow)).grid(row=6, column=0, columnspan=2)
    Button(loginwindow, text="Register", bg="#5f0137", fg="white", font=("Calibri", 15), command=lambda: [loginwindow.grid_forget(), register()]).grid(row=6, column=1, padx=(100,0), sticky="w")
    Button(loginwindow, text="Back", bg="#5f0137", fg="white", font=("Calibri", 15), command=lambda: [loginwindow.grid_forget(), home_page()]).grid(row=6, column=0, sticky="e")  

    #Checks if the user has entered the correct credentials
    def check_login(loginwindow):
        global user, password
        username = username_entry.get()
        passwords = password_entry.get()
        try:
            with open("saved_accounts.txt", 'r') as file:
                if len(file.read()) == 0:
                    messages.config(text="No accounts saved. Please register an account")
            with open("saved_accounts.txt", 'r') as file:
                for line in file:
                    if username in line:
                        if username == line.split(" : ")[0] and passwords == line.split(" : ")[1].strip():
                            loginwindow.grid_forget()
                            user = username
                            password = passwords
                            home_page()
                            break
                        else:
                            messages.config(text="Invalid Credentials.")
                    else:
                        messages.config(text="Incorrect credentials. Please try again")
        except IOError:
            messages.config(text="No accounts saved. Please register an account")
            with open("saved_accounts.txt", 'w') as file:
                file.close()
                
#Page for the user to register an account
def register():
    #Page setup for register page
    global registerwindow
    registerwindow = Frame(window, bg="white")
    registerwindow.grid(sticky="nsew")
    window.title("Register")
    window.geometry("780x450")
    navigation(registerwindow)

    #Register page widgets
    Label(registerwindow, text="BDSC Cafe Online Order", bg="white", font=("Calibri Bold", 30), fg="#5f0137").grid(row=1, column=0, columnspan= 2, padx=5, pady=10, sticky="nsew")
    Label(registerwindow, text="Register account", bg="white", fg="#5f0137", font=("Comic Sans MS", 25)).grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    Label(registerwindow, text="Username", bg="white", fg="#5f0137", font=("Calibri Bold", 15)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    username_entry = Entry(registerwindow, bg="white", font=("Calibri", 12), highlightthickness=2, highlightbackground="#5f0137")
    username_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    Label(registerwindow, text="Password", bg="white", fg="#5f0137", font=("Calibri Bold", 15)).grid(row=4, column=0, padx=10, pady=10, sticky="e")
    password_entry = Entry(registerwindow, show="•", bg="white", font=("Calibri", 12), highlightthickness=2, highlightbackground="#5f0137")
    password_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    Label(registerwindow, text="Age", bg="white", fg="#5f0137", font=("Calibri Bold", 15)).grid(row=5, column=0, padx=10, sticky="e")
    age_entry = Spinbox(registerwindow, bg="white",font=("Calibri", 12), from_=1, to=100, highlightthickness=2, highlightbackground="#5f0137")
    age_entry.grid(row=5, column=1, padx=10, sticky="w")

    message = Label(registerwindow, text="", bg="white", fg="#5f0137", font=("Calibri Bold", 15))
    message.grid(row=6, columnspan=3, pady=10)

    Button(registerwindow, text="Register", bg="#5f0137", fg="white", font=("Calibri", 15), command=lambda: register_account()).grid(row=7, column=0, columnspan=2)
    Button(registerwindow, text="Login", bg="#5f0137", fg="white", font=("Calibri", 15), command=lambda: [registerwindow.grid_forget(), login()]).grid(row=7, column=1, padx=(110,0), sticky="w")
    Button(registerwindow, text="Back", bg="#5f0137", fg="white", font=("Calibri", 15), command=lambda: [registerwindow.grid_forget(), home_page()]).grid(row=7, column=0, sticky="e", padx=20)  

    #Function used to save the account into the external text file
    def register_account():
        global user, password
        username = username_entry.get()
        passwords = password_entry.get()
        age = int(age_entry.get())
        if username != "" and passwords != "":
            if 13 <= age <= 18:
                while True:
                    try:
                        with open("saved_accounts.txt", 'a') as file:
                            file.write(f"{username} : {passwords} : {age}\n")
                            file.close()
                            message.config(text="Account created successfully")
                            registerwindow.grid_forget()
                            user = username
                            password = passwords
                            home_page()
                            break
                    except IOError:
                        with open("saved_accounts.txt", 'w') as file:
                            file.close()
            else:
                message.config(text="You are not eligible to register an account")
        else:
            message.config(text="Please fill in all the boxes")

#The order page where the user can make their order
def menu():
    #Page setup for menu page
    global menu_page, images
    window.geometry("960x550")
    menu = Frame(window, bg="#5f0137")
    menu.grid(row=1, column=0, sticky="nsew")
    navigation(menu)

    #Resize the frame to fit the canvas
    window.grid_rowconfigure(1, weight=1) 
    window.grid_columnconfigure(0, weight=1)
    menu.grid_rowconfigure(1, weight=1)  
    menu.grid_columnconfigure(0, weight=1)

    #Create and configure the canvas
    menu_page = Canvas(menu, bg="White")
    menu_page.grid(row=1, column=0, sticky="nsew", padx=(0, 0))
    order_items = Frame(menu_page, bg="White") #Inner frame to hold the menu items
    menu_page.create_window((0,0), window=order_items, anchor="nw")

    #Create and configure rows scrollbar to scroll through the menu
    scroll = Scrollbar(menu, orient=VERTICAL, command=menu_page.yview, bg="White")
    scroll.grid(row=0, rowspan=2, column=1, sticky="ns")
    menu_page.configure(yscrollcommand=scroll.set, highlightbackground="White")

    #Function for scrolling the canvas with the scrollbar
    def scrollbar(event):
        menu_page.configure(scrollregion=menu_page.bbox('all'))
    
    #Function for scrolling the canvas with the mousewheel
    def scrolling(event):
        menu_page.yview_scroll(-int(event.delta/120), "units")

    #Bind scrolling action to the mousewheel and scrollbar
    order_items.bind("<Configure>", scrollbar)
    menu_page.bind_all("<MouseWheel>", scrolling)

    images = {} #Save the images in a dictionary to be used later
    item_position = 0   #Position the item in the correct row
    title_position = 0   #Position the title in the correct row

    #For loop which creates the menu items
    for rows in range(8):
        img = []  #List to save the images in
        for columns in range(3):
            path = f"images/{cafemenu[rows+rows*2+columns][3]}"
            filter_img = Image.open(f"images/{cafemenu[rows+rows*2+columns][3]}").resize((200, 200)).filter(ImageFilter.GaussianBlur(10))
            filter_img = ImageEnhance.Brightness(filter_img).enhance(0.3)
            img.append([ImageTk.PhotoImage(Image.open(path).resize((200, 200))),ImageTk.PhotoImage(filter_img)])
        
        images[rows] = img  #Save the images into a dictionary to prevent them from being garbage collected
        
        #Create the title for each category
        titles = {0 : "Hot Lunches", 2 : "Healthy Choices", 4 : "Snacks and Frozen food", 6 : "Drinks"}
        if rows in titles:
            Label(order_items, text=f"{titles[rows]}", font=("Calibri Bold", 20), bg="#89c9ec", fg="White").grid(row=rows+title_position, columnspan=3, padx=(30, 0), pady=10, sticky="ew")
            item_position += 1
            title_position += 1

        #Create the menu items
        for frames in range(3):
            f = Frame(order_items, bg="White", highlightbackground="light grey", highlightthickness=1)
            f.grid(row=rows+item_position, column=frames, padx=30, pady=30)

            lbl = Label(f, image=images[rows][frames][0])
            lbl.grid(row=0, column=0, columnspan=2)
            lbl.bind("<Enter>", lambda event, arg = cafemenu[rows+rows*2+frames][2], arg2 = images[rows][frames][1]: show_text(event, arg, arg2))
            lbl.bind("<Leave>", lambda event, arg = images[rows][frames][0]: hide_text(event, arg))
            Label(f, text=f"{cafemenu[rows+rows*2+frames][0]} - ${cafemenu[rows+rows*2+frames][1]:.2f}", bg="white", font=("Calibri Bold", 15)).grid(row=1, column=0, columnspan=2)
            amounts = Spinbox(f, from_=1, to=10, width=5, font=("Calibri Bold", 12), state="readonly")
            amounts.grid(row=2, column=1, padx=10, pady=10)
            Button(f, text="Add to Order", font=("Calibri Bold", 12), command=lambda rows=rows, amounts=amounts, frames=frames: add_to_order(cafemenu[rows+rows*2+frames][0], int(amounts.get()), cafemenu[rows+rows*2+frames][1])).grid(row=2, column=0, padx=10, pady=10)

    #Create the total price label and checkout button
    price_lbl = Label(menu, text=f"Total Price - ${total:.2f}", font=("Calibri", 14), bg="#5f0137", fg="White")
    price_lbl.grid(row=2, columnspan=3, padx=(10, 100), pady=10, sticky="e")
    checkout_button = Button(menu, text="Checkout", font=("Calibri", 12), bg="#5f0137", fg="white", command= lambda: [menu.grid_forget(), checkout()])
    checkout_button.grid(row=2, columnspan=3, padx=10, pady=10, sticky="e")

    #Function used to add items to the order
    def add_to_order(item, amount, price):
        global order, total
        if amount == 0:
            messagebox.showerror("Error", "Please enter a valid amount")
            return
        total += price * amount
        order.append(f"{amount}x {item}")
        price_lbl.config(text=f"Total Price - ${total:.2f}")

#The checkout page
def checkout():
    # Setup the page for the checkout page
    global checkoutwindow, logo_img
    checkoutwindow = Frame(window, bg="white")
    checkoutwindow.grid(sticky="nsew")
    window.title("View order")
    window.geometry("780x500")
    navigation(checkoutwindow)

    #Create checkout widgets
    Label(checkoutwindow, text="BDSC Cafe Online Order", font=("Calibri Bold", 30), fg="#5f0137", bg="white").grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
    Label(checkoutwindow, text="Checkout", font=("Comic Sans MS", 25), fg="#5f0137", bg="white").grid(row=2, column=0, columnspan=2, sticky="nsew")
    Label(checkoutwindow, text="Your order is:", font=("Comic Sans MS", 15), bg="white", fg="#5f0137").grid(row=3, column=0, columnspan=2, sticky="nsew", pady=10)
    Button(checkoutwindow, text="Back", bg="#5f0137", fg="white", font=("Calibri", 14),command=lambda: [checkoutwindow.grid_forget(), home_page()]).grid(row=8, columnspan=2, pady=10)
    
    #Create the canvas to hold the menu items
    orders = ""
    if order != []:
        checkout_page = Canvas(checkoutwindow, bg="White", width=200, height=100)
        checkout_page.grid(row=4, column=0, padx=(100, 0))
        order_items = Frame(checkout_page, bg="White")  # Inner frame to hold the menu items
        order_items.pack(fill=BOTH, expand=True)
        checkout_page.create_window((0, 0), window=order_items, anchor="nw")

        # Create and configure vertical scrollbar to scroll through the menu
        scroll = Scrollbar(checkoutwindow, orient=VERTICAL, command=checkout_page.yview, bg="White")
        scroll.grid(row=4, column=1, sticky="ns") 
        checkout_page.configure(yscrollcommand=scroll.set, highlightbackground="White")

        # Function for scrolling the canvas with the scrollbar
        def scrollbar(event):
            checkout_page.configure(scrollregion=checkout_page.bbox('all'))

        # Function for scrolling the canvas with the mousewheel
        def scrolling(event):
            checkout_page.yview_scroll(-int(event.delta / 120), "units")

        # Bind scrolling action to the mousewheel and scrollbar
        order_items.bind("<Configure>", scrollbar)
        checkout_page.bind_all("<MouseWheel>", scrolling)

        #Display each item in the order
        for item in order:
            orders += f"{item}\n"
        Label(order_items, text=orders, font=("Calibri", 12), bg="white", fg="#5f0137").pack(pady=10)
        Label(checkoutwindow, text=f"Total: ${total:.2f}", font=("Calibri Bold", 15), bg="white", fg="#5f0137").grid(row=5, column=0, columnspan=2, sticky="nsew", pady=10)
        Button(checkoutwindow, text="Confirm order", bg="#5f0137", fg="white", font=("Calibri", 14),command=lambda: [checkoutwindow.grid_forget(), finish()]).grid(row=7, columnspan=2)
    else:
        window.geometry("780x400")  
        Label(checkoutwindow, text="Empty", font=("Calibri", 15), bg="white", fg="#5f0137").grid(row=5, column=0, columnspan=2, sticky="nsew", pady=10)

#This screen is shown when the user completes their order.
def finish():
    if user == "" or password == "":
        login()
        messagebox.showerror("Error", "Please login first")
        return()
    global completed, logo_img
    completed = Frame(window, bg="white")
    completed.grid(sticky="nsew")
    window.title("View order")
    window.geometry("660x400")

    logo_img = ImageTk.PhotoImage(Image.open("images/logo.png").resize((100,70)))
    logo_lbl = Label(completed, image=logo_img, bg="white")
    logo_lbl.grid(row=0, column=0, pady=10, sticky="w")

    Label(completed, text="BDSC Cafe Online Order", font=("Arial Bold", 20), fg="#5f0137", bg="white").grid(row=0, column=1, columnspan= 3, padx=5, pady=10, sticky="nsew")   
    Label(completed, text="Checkout", font=("Comic Sans MS", 15), fg="#5f0137", bg="white").grid(row=1, column=1, columnspan=3, sticky="nsew")
    Label(completed, text="Your order has been confirmed and will be ready for pickup", font=("Comic Sans MS", 12), bg="white", fg="#5f0137").grid(row=2, column=1, columnspan=3, sticky="nsew", pady=10)
    
    #Brings the user to the first frame so they can order again if they wish
    Button(completed, text="Home", bg="#5f0137", fg="white", font=("Calibri", 12), command=lambda: [completed.grid_forget(), reset()]).grid(row=3, column=1, columnspan=3, pady=10, sticky="nsew")

#Shows the description when the user hovers over the item
def show_text(event, arg, arg2):
    event.widget.config(text=arg, compound="center", wraplength=185, fg="White", font=("Calibri", 12), width = 198, height=198, image=arg2)

#Hides the description when the user moves their mouse away from the item
def hide_text(event, arg):
    event.widget.config(text="", image=arg, width = 200, height=200)

#Resets the program to its initial state
def reset():
    global order, total, user, password
    order = []
    total = 0
    user = ""
    password = ""
    home_page()

home_page()
window.mainloop()