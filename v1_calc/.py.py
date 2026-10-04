import tkinter as tk

window = tk.Tk()
window.title("calculator")
window.geometry("300x400")
nums = [7,8,9,4,5,6,1,2,3]

def show_num(num):
    entry.insert(tk.END,str(num))
for i in range (0,9):
    tk.Button(window,text=nums[i],command=lambda x=nums[i]:show_num(x),width=5,height=2,font=("Arial",8)).grid(row=(i//3)+1,column=i%3)
entry = tk.Entry(window,width=20,font=("Arial",16))
entry.grid(row = 0, column = 0, columnspan = 4)

def clear():
    entry.delete(0, tk.END)
c = tk.Button(window, text ="c", command=clear, width=5,height=2,font=("Arial",8) )
c.grid(row = 1, column = 4)

first_num = 0
second_num = 0
operation =""
answer = 0

def add():
    global first_num
    global operation
    first_num = int(entry.get())
    operation = "+"
    clear()
plus = tk.Button(window, text ="+", command=add, width=5,height=2 ,font=("Arial",8))
plus.grid(row = 2, column = 4)

def sub():
    global first_num
    global operation
    first_num = int(entry.get())
    operation = "-"
    clear()
subtraction = tk.Button(window, text ="-", command=sub, width=5,height=2,font=("Arial",8) )
subtraction.grid(row = 3, column = 4)

def mul():
    global first_num
    global operation
    first_num = int(entry.get())
    operation = "*"
    clear()
multiplication = tk.Button(window, text ="X", command=mul, width=5,height=2 ,font=("Arial",8))
multiplication.grid(row = 4, column = 4)

def div():
    global first_num
    global operation
    first_num = int(entry.get())
    operation = "/"
    clear()
division = tk.Button(window, text ="/", command=div, width=5,height=2 ,font=("Arial",8))
division.grid(row = 5, column = 4)

def equal():
    global second_num
    global operation
    global answer
    second_num = int(entry.get())
    clear()
    if operation == "+":
        answer = first_num + second_num
    elif operation == "-":
        answer = first_num - second_num
    elif operation == "*":
        answer = first_num * second_num
    elif operation == "/" and second_num != 0:
        answer = first_num / second_num
    else:
        answer = "Error"
    entry.insert(tk.END, answer)
equall = tk.Button(window, text ="=", command=equal, width=5,height=2,font=("Arial",8) )
equall.grid(row = 4, column = 2)




window.mainloop()
