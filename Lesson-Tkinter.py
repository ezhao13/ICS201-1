from tkinter import *

def calc():
  answer.set(f'{eval(exp.get())}')
  print(eval(exp.get()))

window = Tk()
window.geometry('300x200')
window.title("Evan Zhao")

myfont = "Helvetica 12 bold"

lbl = Label(window, text = 'Calculator', font = myfont,\
           bg = '#F3A332', fg = 'white')
lbl.grid(row = 0, column = 0, pady = 10, padx = 40)

exp = StringVar()
txt_input = Entry(window, font = myfont, width = 15, textvariable = exp)
txt_input.grid(row = 1, column = 0, pady = 10)

btn_equal = Button(window, text = '=', width = 15, font = myfont,\
                  command = calc)
btn_equal.grid(row = 2, column = 0, pady = 10)

answer = StringVar()
txt_answer = Entry(window, font = myfont, width = 15, textvariable = answer,\
                  fg = 'red')
txt_answer.grid(row = 3, column = 0, pady = 10)

window.mainloop()