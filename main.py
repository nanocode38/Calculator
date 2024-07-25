import sys
import os
import tkinter as tk
from tkinter.messagebox import showwarning
from _tkinter import TclError

# Must be False!!
DEBUG = os.path.isfile('DEBUG')


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('319x486')
        self.root.title('Calculator')
        self.root.wm_resizable(DEBUG, DEBUG)
        self.root.wm_iconbitmap('images\\logo.ico')

        self.input_label = tk.Label(self.root, text='', font=('Arial', 23), cursor="hand2", width=16, height=1)
        self.ans_label = tk.Label(self.root, text='', font=('Arial', 23), width=16, height=1)
        self.eq_button = tk.Button(self.root, text='=', command=self.calculate, font=('Arial', 12))
        self.eq_button.config(width=2, height=4)

        self.number_buttons = []

        self.number_buttons.append(tk.Button(self.root, text='0', command=lambda: self.add_num(0), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='1', command=lambda: self.add_num(1), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='2', command=lambda: self.add_num(2), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='3', command=lambda: self.add_num(3), font=('Arial', 12)))
        self.number_buttons.append(
            tk.Button(self.root, text='+', command=lambda: self.add_num('+'), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='4', command=lambda: self.add_num(4), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='5', command=lambda: self.add_num(5), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='6', command=lambda: self.add_num(6), font=('Arial', 12)))
        self.number_buttons.append(
            tk.Button(self.root, text='-', command=lambda: self.add_num('-'), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='7', command=lambda: self.add_num(7), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='8', command=lambda: self.add_num(8), font=('Arial', 12)))
        self.number_buttons.append(tk.Button(self.root, text='9', command=lambda: self.add_num(9), font=('Arial', 12)))
        self.number_buttons.append(
            tk.Button(self.root, text='*', command=lambda: self.add_num('*'), font=('Arial', 12)))
        self.number_buttons.append(
            tk.Button(self.root, text='/', command=lambda: self.add_num('/'), font=('Arial', 12)))

        for i in range(14):
            self.number_buttons[i].config(width=4, height=1)

        self.input_label.bind('<Button-1>', self.label_to_entry)

        if DEBUG:
            self.input_label.config(bg='white', fg='black')
            self.ans_label.config(bg='white', fg='black')

        self.label_pos_x = (319 - self.input_label.winfo_reqwidth()) // 2
        self.input_label.place(x=self.label_pos_x, y=2)
        self.ans_label.place(x=self.label_pos_x, y=4 + self.input_label.winfo_reqheight())
        self.eq_button.place(x=319 - self.eq_button.winfo_reqwidth() - 5, y=486 - self.eq_button.winfo_reqheight() - 5)

        for i in range(4):
            for j in range(4):
                if i * 4 + j + 1 >= 13:
                    break
                try:
                    x = self.label_pos_x + j * (4 + self.number_buttons[0].winfo_reqwidth())
                    y = self.ans_label.winfo_reqheight() * 2 + 4 + i * (
                            4 + self.number_buttons[0].winfo_reqwidth()) + 80
                    self.number_buttons[i * 4 + j + 1].place(x=x, y=y)
                except IndexError:
                    break
        self.number_buttons[0].place(x=self.label_pos_x + 4 + self.number_buttons[0].winfo_reqwidth(),
                                     y=self.ans_label.winfo_reqheight() * 2 + 4 + 3 * (
                                             4 + self.number_buttons[0].winfo_reqwidth()) + 80)
        self.number_buttons[13].place(x=self.label_pos_x + 3 * (4 + self.number_buttons[0].winfo_reqwidth()),
                                      y=self.ans_label.winfo_reqheight() * 2 + 4 + 3 * (
                                              4 + self.number_buttons[0].winfo_reqwidth()) + 80)

    def mainloop(self):
        self.root.mainloop()

    def get(self):
        self.input_label.config(text=self.input_entry.get())
        self.input_entry.destroy()

    def label_to_entry(self, _):
        self.input_entry = tk.Entry(self.root, width=16, font=('Arial', 23))
        self.input_entry.insert(0, self.input_label.cget('text'))
        self.input_entry.bind('<Return>', lambda _: self.get())
        self.input_entry.bind('<FocusOut>', lambda _: self.get())

        self.input_entry.place(x=self.label_pos_x, y=2)

    def calculate(self):
        try:
            try:
                result = eval(self.input_entry.get())
            except TclError:
                result = eval(self.input_label.cget('text'))
            except AttributeError:
                result = eval(self.input_label.cget('text'))
            self.ans_label.config(text=str(result))
        except ZeroDivisionError:
            showwarning('Calculator ERROR', 'Math Error!')
        except SyntaxError:
            showwarning('Calculator ERROR', 'Expression Syntax Error!')
        except NameError:
            showwarning('Calculator ERROR', 'Expression Syntax Error!')

    def add_num(self, num):
        self.input_label.config(text=self.input_label.cget('text') + str(num))


if __name__ == '__main__':
    if DEBUG:
        print("DEBUG Mode!", file=sys.stderr)
    MainWindow().mainloop()
