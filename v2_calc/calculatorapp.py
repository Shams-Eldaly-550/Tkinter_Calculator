import tkinter as tk 
from tkinter import messagebox

#   النافذه الرئيسيه
window = tk.Tk()
window.title("CALCULATOR")
window.geometry("350x510")
window.configure(bg="#6D7D85")
window.resizable(False,False)
def on_closing ():
    window.destroy()
window.protocol("WM_DELETE_WINDOW" , on_closing)

#   entry شاشه ال
entry_var = tk.StringVar() 
entry = tk.Entry(
    window,
    textvariable = entry_var,
    font=("Consolas",20 ,"bold"),
    bg="#FFFFFF",
    fg="#222222",
    bd=10,
    justify="right",
    state="readonly"
)
entry.grid(row=0 ,column=0 ,columnspan=4 ,padx=10 ,pady=5 ,ipadx=4 ,ipady=8)

#   منطق التعامل مع الازرار والعمليات الحسابيه 
def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set('')

def backspace():
    entry_var.set(entry_var.get()[:-1])

def calculate():
    try:
        expressoin = entry_var.get().replace('x','*').replace('÷','/')
        result = eval(expressoin) # متنسيش تقفلي الكتابه من الكيبورد
        entry_var.set(result)
    except Exception:
        messagebox.showerror("Error", "Invalid operation")

#   Separation of Data and Logic
#     Data:
buttons= [
    ("C",1 ,0 ,clear,"#D7D6F3",1),("⌫",1 ,1 ,backspace,"#D7D6F3",1),("(",1 ,2 ,lambda:press("("),"#F4F5F7",1),(")",1 ,3 ,lambda:press(")"),"#F4F5F7",1),
    ("7",2 ,0 ,lambda:press("7"),"#F4F5F7",1),("8",2 ,1 ,lambda:press("8"),"#F4F5F7",1),("9",2 ,2 ,lambda:press("9"),"#F4F5F7",1),("÷",2 ,3 ,lambda:press("÷"),"#D0E8E4",1),
    ("4",3 ,0 ,lambda:press("4"),"#F4F5F7",1),("5",3 ,1 ,lambda:press("5"),"#F4F5F7",1),("6",3 ,2 ,lambda:press("6"),"#F4F5F7",1),("x",3 ,3 ,lambda:press("x"),"#D0E8E4",1),
    ("1",4 ,0 ,lambda:press("1"),"#F4F5F7",1),("2",4 ,1 ,lambda:press("2"),"#F4F5F7",1),("3",4, 2 ,lambda:press("3"),"#F4F5F7",1),("-",4 ,3 ,lambda:press("-"),"#D0E8E4",1),
    ("0",5 ,0 ,lambda:press("0"),"#F4F5F7",1),(".",5 ,1 ,lambda:press("."),"#F4F5F7",1),("%",5 ,2 ,lambda:press("%"),"#F4F5F7",1),("+",5 ,3 ,lambda:press("+"),"#D0E8E4",1),
    ("=",6 ,0 ,calculate,"#F3C5A8",4)
]

#     Logic:
for Text, rw, clmn, comnd, color, clmns in buttons:
    button= tk.Button(
        window,
        text=Text,
        font=("Consolas", 14, "bold"),
        command=comnd,
        bg=color,
        fg="#2B2D42",
        activebackground="#EEEEEE",
        height=2,
        width=2
    )
    button.grid(row=rw, column=clmn, columnspan=clmns, padx=5, pady=5, sticky="nsew")

window.mainloop()