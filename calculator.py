from tkinter import *

print('Started...')

class Calculator:
    def __init__(self, master):
        self.s1 = ''
        self.s2 = ''

        self.e1 = Entry(master, width = 20)
        self.e2 = Entry(master, width = 20)
        
        self.but_mult = Button(master, text = "Преобразовать")
        self.but_plus = Button(master, text = "+")
        self.but_minus = Button(master, text = "-")
        self.but_div = Button(master, text = "/")
        
        self.but_mult.bind('<Button-1>', self.mult)
        self.but_plus.bind('<Button-1>', self.plus)
        self.but_minus.bind('<Button-1>', self.minus)
        self.but_div.bind('<Button-1>', self.div)
        
        self.lbl_res = Label(master, bg = 'black', fg = 'white', width = 20)
        
        self.e1.pack()
        self.e2.pack()
        self.but_plus.pack()
        self.but_minus.pack()
        self.but_mult.pack()
        self.but_div.pack()
        self.lbl_res.pack()
    
    def mult(self, event):
        print('Mult')
        if self.check_enter():
            self.lbl_res['text'] = str(float(self.s1) * float(self.s2))
        else:
            self.lbl_res['text'] = 'Error entered data'

    def plus(self, event):
        print('Plus')
        if self.check_enter():
            self.lbl_res['text'] = str(float(self.s1) + float(self.s2))
        else:
            self.lbl_res['text'] = 'Error entered data'

    def minus(self, event):
        print('Minus')
        if self.check_enter():
            self.lbl_res['text'] = str(float(self.s1) - float(self.s2))
        else:
            self.lbl_res['text'] = 'Error entered data...'

    def div(self, event):
        print('Division')
        if self.check_enter():
            if int(self.s2) != 0:
                self.lbl_res['text'] = str(float(self.s1) / float(self.s2))
            else:
                self.lbl_res['text'] = 'Division by zero'
        else:
            self.lbl_res['text'] = 'Error entered data...'
        

    def is_digit(self, s):
        if s.isdigit():
            return True
        else:
            try:
                float(s)
                int(s)
                return True
            except ValueError:
                return False

    def check_enter(self):
        self.s1 = self.e1.get()
        self.s2 =self.e2.get()

        if self.is_digit(self.s1) and self.is_digit(self.s2):
            return True
        else:
            return False

root = Tk()

calc = Calculator(root)

root.mainloop()