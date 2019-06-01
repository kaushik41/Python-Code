import tkinter as tk
mainWindow = tk.Tk()
mainWindow.title("calci")
number_label = tk.Label(mainWindow,text="1st number")
number_label.pack()
name_field = tk.Entry(mainWindow)
name_field.pack()
number_label2 = tk.Label(mainWindow,text="2nd number")
number_label2.pack()



name_field2 = tk.Entry(mainWindow)
name_field2.pack()

operations = tk.Label(mainWindow,text="operation")
operations.pack()

def add():
    first=int(name_field.get())
    second=int(name_field2.get())
    res= first+second

    result_label.config(text=" operation result is: " +  str(res))

def subtract():
    first = int(name_field.get())
    second = int(name_field2.get())
    res = first - second

    result_label.config(text=" operation result is: " + str(res))


def multiply():
   first = int(name_field.get())
   second = int(name_field2.get())
   res=first * second

   result_label.config(text=" operation result is: " + str(res))


def division():
    first = int(name_field.get())
    second = int(name_field2.get())
    res = first / second

    result_label.config(text=" operation result is: " + str(res))


add_button=tk.Button(mainWindow, text=" + ", command=lambda : add())
add_button.pack()
subtract_button=tk.Button(mainWindow , text=" - " ,command=lambda : subtract())
subtract_button.pack()
multiply_button=tk.Button(mainWindow,text="*",command=lambda : multiply())
multiply_button.pack()
division_button=tk.Button(mainWindow,text="/",command=lambda : division())
division_button.pack()
result_label = tk.Label(mainWindow,text="result")
result_label.pack()
mainWindow.mainloop()