import tkinter as tk

def button_pressed(button):
    previous = equation.get()
    equation.set(previous + button)


def clear_s():
    equation.set('')

def equal():
    try:
        equation.set(eval(equation.get()))
    except:
        pass

Janela = tk.Tk()
Janela.title('tk calculator')

pixel = tk.PhotoImage(width=1, height=1)#jeitinho pra controlar tamanho por pixel

equation = tk.StringVar() #texto da janela entry
Display = tk.Entry(Janela, textvariable=equation, width=27)
Display.grid(row= 0,columnspan=4)



Clear = tk.Button(Janela, text='C', command=clear_s,
                  height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Clear.grid(row=1,column=0)

Divi = tk.Button(Janela, text='/', command=lambda: button_pressed('/'),
                 height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Divi.grid(row=1,column=1)

Mult = tk.Button(Janela, text='*', command=lambda: button_pressed('*'),
                 height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Mult.grid(row=1,column=2)

Minus = tk.Button(Janela, text='-', command=lambda: button_pressed('-'),
                  height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Minus.grid(row=1,column=3)

Number_7 = tk.Button(Janela, text='7', command=lambda: button_pressed('7'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_7.grid(row=2, column=0)

Number_8 = tk.Button(Janela, text='8', command=lambda: button_pressed('8'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_8.grid(row=2, column=1)

Number_9 = tk.Button(Janela, text='9', command=lambda: button_pressed('9'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_9.grid(row=2, column=2)

Plus = tk.Button(Janela, text='+', command=lambda: button_pressed('+'),
                 height=106, width=50, compound='c', image=pixel, padx=0, pady=0)
Plus.grid(rowspan=2,row=2, column=3)

Number_4 = tk.Button(Janela, text='4', command=lambda: button_pressed('4'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_4.grid(row=3, column=0)

Number_5 = tk.Button(Janela, text='5', command=lambda: button_pressed('5'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_5.grid(row=3, column=1)

Number_6 = tk.Button(Janela, text='6', command=lambda: button_pressed('6'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_6.grid(row=3, column=2)

Number_1 = tk.Button(Janela, text='1', command=lambda: button_pressed('1'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_1.grid(row=4, column=0)

Number_2 = tk.Button(Janela, text='2', command=lambda: button_pressed('2'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_2.grid(row=4, column=1)

Number_3 = tk.Button(Janela, text='3', command=lambda: button_pressed('3'),
                     height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Number_3.grid(row=4, column=2)

Equal = tk.Button(Janela, text='=', command=equal,
                  height=106, width=50, compound='c', image=pixel, padx=0, pady=0)
Equal.grid(row=4, column=3, rowspan=2)

Number_0 = tk.Button(Janela, text='0', command=lambda: button_pressed('0'),
                     height=50, width=106, compound='c', image=pixel, padx=0, pady=0)
Number_0.grid(row=5, column=0,columnspan=2)

Decimal = tk.Button(Janela, text=',', command=lambda: button_pressed('.'),
                    height=50, width=50, compound='c', image=pixel, padx=0, pady=0)
Decimal.grid(row=5,column=2)



Janela.mainloop()
