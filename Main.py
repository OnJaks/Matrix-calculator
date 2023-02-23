from tkinter import *
import Add
import Sub
import Multiply
import Determinant
import Inverse
import RREF
#Vytvoreni hlavniho menu s tlacitky.
class Menu:
    def __init__(self):
        menu = Tk()
        menu.title("Matrix calculator")
        menu.geometry('350x350')
        heading = Label(menu, text="Numeric matrix calculator", font = ("Arial", 17))
        add = Button(menu, text="Add", height=2, width=15, command=Add.Matrix_add)
        subtract = Button(menu, text="Subtract", height=2, width=15, command=Sub.Matrix_sub)
        multiple = Button(menu, text="Multiply", height=2, width=15, command=Multiply.Matrix_multiply)
        inverse = Button(menu, text="Inverse", height=2, width=15, command=Inverse.Matrix_inverse)
        determinant = Button(menu, text="Determinant", height=2, width=15, command=Determinant.Matrix_determinant)
        RREFs = Button(menu, text= "RREF", height =2, width=15, command=RREF.Matrix_gauss_jordan_elimination)
        heading.pack()
        add.pack()
        subtract.pack()
        multiple.pack()
        inverse.pack()
        determinant.pack()
        RREFs.pack()
        menu.mainloop()
if __name__ == '__main__':
    Menu()
