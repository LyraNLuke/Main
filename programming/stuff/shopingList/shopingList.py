import tkinter as tk

##main code

#list of items
    #item informations
        #type, price, amount, overall price
cart = [
    {"item": "kokonut", "amount": 5, "price": 2},
    {"item": "bannana", "amount": 503, "price": 3}
]
    #add / remove / update item functions
def showFrame(name):
    frames[name].tkraise()
    
    
def displayItems():
    i=2
    for item in cart:
        tk.Label(
            list,
            text=item["item"], font=FONT_NORMAL,
            bg=COLOR_LIST, fg=COLOR_TEXT
        ).grid(row=i, column=0, sticky="ew", padx=10)
        tk.Label(
            list,
            text=item["amount"], font=FONT_NORMAL,
            bg=COLOR_LIST, fg=COLOR_TEXT
        ).grid(row=i, column=2, sticky="ew", padx=10)
        tk.Label(
            list,
            text=item["price"],font=FONT_NORMAL,
            bg=COLOR_LIST, fg=COLOR_TEXT
        ).grid(row=i, column=4, sticky="ew",padx=10)
        tk.Label(
            list,
            text=(item["amount"]*item["price"]), font=FONT_NORMAL,
            bg=COLOR_LIST, fg=COLOR_TEXT
        ).grid(row=i, column=6, sticky="ew",padx=10)
        i+=1
        

def make_placeholder(entry, placeholder):
    entry.delete(0,tk.END)
    root.focus()
    entry.insert(0, placeholder)
    entry.config(bg=COLOR_ENTRYFIELD_ERR, fg=COLOR_ENTRYTXT_ERR)

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(bg=COLOR_ENTRIES, fg=COLOR_TEXT)

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(bg=COLOR_ENTRYFIELD_ERR, fg=COLOR_ENTRYTXT_ERR)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    
    
def addItem(event=None):
    global cart
    item=itemInput.get().strip()
    amount=amountInput.get().strip()
    price=priceInput.get().strip()
    
    error=False
    if item == "":
        make_placeholder(itemInput, "cant be empty")
        error=True
    try: 
        if amount != "": amount = int(amount)
    except: 
        make_placeholder(amountInput, "must be intager")
        error=True
    try: 
        if price != "": price = int(price)
    except: 
        make_placeholder(priceInput, "must be integer")  
        error=True    
    if error: return
    
    cart.append({"item":item, "amount":amount, "price":price})
    itemInput.delete(0, tk.END)
    amountInput.delete(0,tk.END)
    priceInput.delete(0, tk.END)
    root.focus()
    displayItems()
    mainInterface.tkraise()
    

def editItem(item):
    pass
        


##user inteface
#base design values
FONT_TITLE  = ("Arial", 20, "bold")
FONT_NORMAL = ("Arial", 12)
FONT_BOLD   = ("Arial", 12, "bold")
FONT_SMALL  = ("Arial", 9)
FONT_BUTTON = ("Arial", 11, "bold")

COLOR_DEFAULT       = "#050516"
COLOR_BUTTON_HOVER  = "#eeb1b5"
COLOR_BUTTON        = "#425554"
COLOR_BUTTON_TEXT   = "#110202"
COLOR_TEXT          = "#ECDCDC"
COLOR_LIST          = "#0F2A35"
COLOR_EDIT_INTEFACE = "#202233"
COLOR_ENTRIES       = "#2c4b44"
COLOR_ENTRYTXT_ERR  = "#3d0000"
COLOR_ENTRYFIELD_ERR= "#f31b1b"


#main interface
root = tk.Tk()
root.title("SchopingCart")
root.geometry("360x468")
root.resizable(True,True)
root.configure(bg=COLOR_DEFAULT)

root.columnconfigure(0, weight=1)

title = tk.Label(
    root,
    text="Schoping Cart",
    font=FONT_TITLE,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT,
)
title.grid(row=0, column=0, pady=(10,20), sticky="ew")

#buttons for adding new items / removing items
    #isput displays for adding item details
#display for current list
mainInterface = tk.Frame(
    root,
    bg=COLOR_DEFAULT
)
mainInterface.grid(row=1, column=0, pady=(10,5), padx=20, sticky="nsew")
mainInterface.columnconfigure(0, weight=1)


buttons =tk.Frame(  #navButten frame
    mainInterface,
    bg=COLOR_DEFAULT
)
buttons.grid(row=0, column=0, pady=2, sticky="ew")

list = tk.Frame(    #shoping list frame
    mainInterface,
    bg=COLOR_LIST,
    width=300, height=350,
    relief="sunken", bd=2,
)
list.grid(row=1, column=0, pady=(2,7), sticky="nsew")

t=["Item::","","Amount::","","Price::","","Total::"]
for i in range(len(t)): #generating top line of SL display
    tk.Label(
        list,
        text=t[i],
        font=FONT_NORMAL,
        bg=COLOR_LIST, fg=COLOR_TEXT
    ).grid(row=0, column=i, pady=(5,10))


addItemInterface = tk.Frame(
    root,
    bg=COLOR_EDIT_INTEFACE,
    relief="sunken", bd=2
)
addItemInterface.grid(row=1, column=0, pady=(50,5))

t=["Item:","Amount:","Price:"]
for i in range(len(t)):
    tk.Label(
        addItemInterface,
        text=t[i], font=FONT_NORMAL,
        bg=COLOR_EDIT_INTEFACE, fg=COLOR_TEXT
    ).grid(row=i, column=0, sticky="e", pady=2)
    
itemInput = tk.Entry(
    addItemInterface,
    font=FONT_NORMAL,
    bg=COLOR_ENTRIES, fg=COLOR_TEXT
)
itemInput.grid(row=0, column=1, sticky="w")

amountInput = tk.Entry(
    addItemInterface,
    font=FONT_NORMAL,
    bg=COLOR_ENTRIES, fg=COLOR_TEXT
)
amountInput.grid(row=1, column=1, sticky="w")

priceInput = tk.Entry(
    addItemInterface,
    font=FONT_NORMAL,
    bg=COLOR_ENTRIES, fg=COLOR_TEXT
)
priceInput.grid(row=2, column=1, sticky="w")

addItemButton = tk.Button(
    addItemInterface,
    command=addItem,
    text="Add", font=FONT_BUTTON,
    bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT,
    activebackground=COLOR_BUTTON_HOVER
)
addItemButton.grid(row=3, column=0, columnspan=2, pady=(15,5))


itemSelctionInteface = tk.Frame(
    root,
    bg=COLOR_EDIT_INTEFACE,
    relief="sunken", bd=2
)
itemSelctionInteface.grid(row=1, column=0, pady=(50,5), sticky="n")
tk.Label(
    itemSelctionInteface,
    text="Chose the item you want to edit", font=FONT_NORMAL,
    bg=COLOR_EDIT_INTEFACE, fg=COLOR_TEXT
).grid(row=0, column=0, pady=15)

for i in range(len(cart)):
    tk.Button(
        itemSelctionInteface,
        text=cart[i]["item"], font=FONT_NORMAL,
        bg=COLOR_EDIT_INTEFACE, fg=COLOR_TEXT,
        command=lambda n=cart[i]["item"]: editItem(n)
    ).grid(row=i+1, column=0, pady=2)


editItemInteface = tk.Frame(
    root,
    bg=COLOR_EDIT_INTEFACE,
    relief="sunken", bd=2
)
editItemInteface.grid(row=1, column=0, pady=(50,5))


frames = {
    "Home":         mainInterface,
    "Add Item":     addItemInterface,
    "edit Item":    itemSelctionInteface
}

for name, frame in frames.items():
    tk.Button(
        buttons,
        text=name, font=FONT_BUTTON,
        bg=COLOR_BUTTON,
        fg=COLOR_BUTTON_TEXT,
        activebackground=COLOR_BUTTON_HOVER,
        command=lambda n=name: showFrame(n)
    ).pack(side="left", padx=5, expand=True)

displayItems()

mainInterface.tkraise()

root.mainloop()