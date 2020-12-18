'''
Extremely simple calculator using tkinter
Only accepts two numbers and the numerical operation
'''

from tkinter import *
from tkinter import messagebox

class Inputs(Frame):
    def __init__(self, parent):
        '''
        Creates a frame with entrys
        '''
        super().__init__(parent)
        self.pack()

        self.num1 = Entry(self)
        self.num2 = Entry(self)

        Label(self, text="First number").pack()
        self.num1.pack()
        Label(self, text="Second number").pack()
        self.num2.pack()

class Operation(Button):
    def __init__(self, parent, inputs, column, text, operation):
        '''
        Creates a button with the correct text that displays the calculation result
        '''
        self.inputs = inputs
        self.operation = operation

        super().__init__(parent, text=text, command=self.display_result)
        self.grid(row=0, column=column)

    def display_result(self):
        '''
        Method that displays result of calculation accepting operation function as argument
        '''
        try:
            messagebox.showinfo("Result", "{0:g}".format(self.operation(
                float(self.inputs.num1.get()), 
                float(self.inputs.num2.get())
            )))
        except:
            messagebox.showerror("Error", "You didn't enter a number")

class Calculator(Tk):
    def __init__(self):
        '''
        Creates root with inputs and operations
        '''
        super().__init__()
        self.title("Calculator")
        self.geometry("250x120")

        inputs = Inputs(self)
        
        opframe = Frame(self)
        Operation(opframe, inputs, 1, "+", lambda x, y: x + y)
        Operation(opframe, inputs, 2, "-", lambda x, y: x - y)
        Operation(opframe, inputs, 3, "*", lambda x, y: x * y)
        Operation(opframe, inputs, 4, "/", lambda x, y: x / y)
        Operation(opframe, inputs, 5, "%", lambda x, y: x % y)
        Operation(opframe, inputs, 6, "^", lambda x, y: x ** y)
        opframe.pack(pady=5)

if __name__ == "__main__":
    Calculator().mainloop()