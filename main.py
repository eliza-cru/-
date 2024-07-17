# from tkinter import *

# clicks = 0


# def finish():
#    root.destroy()
#    print("App is close!")

# def click_button():
#    global clicks
#    clicks += 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#    btn3["text"] = f"Clicks {clicks}"



# root = Tk()
# root.title("My first app")
# root.geometry("400x300")
# root.minsize(200, 200)
# root.maxsize(600, 350)
# root.atributes("-fullscreen", True)
# root.atributes("-alpha", 5.0)
# root.protocol("WM_DELETE_WINDOW", finish)



# icon = PhotoImage(file="free-sticker-tiger-4193303.png")
# root.iconphoto(True, icon)

# label = Label(text="Hello my friends")
# label.pack()

# label2 = Label(text="welcome to my app")
# label2.pack()

# btn1 = Button(text="Click")
# btn1.pack()

# btn2 = Button()
# btn2.pack()
# btn2["text"] = "No Click"

# btn3 = Button(text="Click me", command=click_button)
# btn3.pack()


# root.mainloop()


# from tkinter import *

# def calk():
#     val1 = entry1.get()
#     val2 = entry2.get()
#     val3 = entry3.get()

#     if val1 == '' or val2 == '' or val3 == '':
#         txt["text"] = 'заполните поля'
#         txt["bg"] = '#5c3b46'
#         return
#     else:
#         if val2 != '+' and val2 == '' and val2 != '/' and val2 != "*":
#             txt["text"] = "неверная операция" 
#             txt["bg"] = "#9c405e"
#         elif val2 == '-':
#             if val2 == "-":
#                 txt["text"] = float(val1) - float(val3)
#                 txt["bg"] = '#85ed8d'
#         elif val2 == '+':
#             if val2 == "+":
#                 txt["text"] = float(val1) + float(val3)
#                 txt["bg"] = '#85ed8d'
#         elif val2 == '*':
#             if val2 == "*":
#                 txt["text"] = float(val1) * float(val3)
#                 txt["bg"] = '#85ed8d'                
#         elif val2 == '/':
#             if val2 == "/":
#                 txt["text"] = float(val1) / float(val3)
#                 txt["bg"] = '#85ed8d'        

     


# root = Tk()
# root.title("My first app")
# root.geometry("450x300")
# root.configure(bg="#f095b4")

# frame = Frame(root)
# frame.pack(anchor="center")

# lad1 = Label(text='число', font=("Comis Sans MS", 12))
# lad2 = Label(text='операция', font=("Comis Sans MS", 12))
# lad3 = Label(text='число', font=("Comis Sans MS", 12))
# entry1 = Entry(font=("Comis Sans MS", 12), width=14)
# entry2= Entry(font=("Comis Sans MS", 12), width=14)
# entry3 = Entry(font=("Comis Sans MS", 12), width=14)
# btn = Button(text="вычислить", font=("Comis Sans MS", 14),bg="#faa7c4", fg="#d12460", command=calk)
# txt = Label(text="")

# lad1.grid(row=0, column=0, padx=10, pady=10)
# lad2.grid(row=0, column=1, padx=10, pady=10)
# lad3.grid(row=0, column=2, padx=10, pady=10)
# entry1.grid(row=1, column=0, padx=10, pady=10)
# entry2.grid(row=1, column=1, padx=10, pady=10)
# entry3.grid(row=1, column=2, padx=10, pady=10)
# btn.grid(row=2, column=0, columnspan=3, sticky='we', padx=10, pady=10)
# txt.grid(row=3, column=0, columnspan=3, sticky='we', padx=10, pady=10)

# root.mainloop()