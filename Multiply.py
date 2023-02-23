from tkinter import *
from tkinter import messagebox
from math import floor
class Matrix_multiply:
    #Vynasobi mezi sebou prvky radku prvni matice a sloupce druhe a secte je k sobe.
    #Vystupni matici pretvori,tak aby mela na vystupu int nebo float.
    def mult(self):
        self.output_matrix = []
        for i in range(self.rows_int_a):
            self.output_matrix.append([])
            for j in range(self.cols_int_b):    
                self.output_matrix[i].append([])
                self.output_matrix[i][j] = 0
                for k in range(self.rows_int_b):
                    self.output_matrix[i][j]+=self.matrix_a[i][k]*self.matrix_b[k][j]
        for i in range(len(self.output_matrix)):
            for j in range(len(self.output_matrix[i])):
                if floor(self.output_matrix[i][j])-self.output_matrix[i][j] == 0:
                    self.output_matrix[i][j] = int(self.output_matrix[i][j])
                else:
                    self.output_matrix[i][j] = round(self.output_matrix[i][j], 2)
        return self.output_matrix
    #Vytvari okno kde se zobrazi vystupni matice a spousti metodu mult.
    def output_matrix(self):
        self.input.destroy()
        self.output = Toplevel()
        Label(self.output, text="Ouptut matrix:", font=("arial", 10, "bold")).grid(row=1, column=1)
        self.output_matrix = self.mult()
        for i in range(len(self.output_matrix)):
            for j in range(len(self.output_matrix[i])):
                Label(self.output, text=self.output_matrix[i][j], bd=5).grid(row=i+2, column=3+j)
        self.output.mainloop()
    #Pretvari vstupy na matice s prvky typu float.
    def matrices(self):
        self.matrix_a=[]
        self.matrix_b=[]
        for i in range(self.rows_int_a):
            self.matrix_a.append([])
            for j in range(self.cols_int_a):
                self.matrix_a[i].append(float(self.var_a[i][j].get()))
        for i in range(self.rows_int_b):
            self.matrix_b.append([])
            for j in range(self.cols_int_b):
                self.matrix_b[i].append(float(self.var_b[i][j].get()))
        self.output_matrix()
    #Zpracovava druhou matice a kontroluje jestli je mensi nebo rovno 10x10 nebo alespon 2x2.
    #Vytvari okno na vlozeni prvku matice.
    def matrix_2(self):
        self.input.destroy()
        self.input = Toplevel()
        Label(self.input, text="Enter matrix B:", font=('arial', 10, 'bold')).grid(row=1, column=1)
        entries_b = []
        self.var_b=[]
        for i in range(self.rows_int_b):
            entries_b.append([])
            self.var_b.append([])
            for j in range(self.cols_int_b):
                self.var_b[i].append(StringVar())
                entries_b[i].append(Entry(self.input, textvariable=self.var_b[i][j], width=5))
                entries_b[i][j].grid(row=i+2, column=j+2)
        Button(self.input, text="Enter", width=8, command=self.matrices).grid(row=self.cols_int_b + self.cols_int_b + 10, column=1)
    #Zpracovava prvni matice a kontroluje jestli je mensi nebo rovno 10x10 nebo alespon 2x2.
    #Vytvari okno na vlozeni prvku matice.
    def matrix_1(self):
        if self.cols_a.get()=='' or self.rows_a.get()=="" or self.rows_b.get()=="" or self.cols_b.get()=="":
            messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
            self.gui_multiply.destroy()
            return
        self.rows_int_a = int(self.rows_a.get())
        self.cols_int_a = int(self.cols_a.get())
        self.rows_int_b = int(self.rows_b.get())
        self.cols_int_b = int(self.cols_b.get())
        if self.rows_int_a<=1 or self.rows_int_a>10 or self.cols_int_a <=1 or self.cols_int_a>10 or self.rows_int_b<=1 or self.rows_int_b>10 or self.cols_int_b <=1 or self.cols_int_b>10:
            messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
            self.gui_multiply.destroy()
            return
        self.gui_multiply.destroy()
        self.input = Toplevel()
        Label(self.input, text="Enter matrix A:", font=('arial', 10, 'bold')).grid(row=1, column=1)
        entries_a = []
        self.var_a=[]
        for i in range(self.rows_int_a):
            entries_a.append([])
            self.var_a.append([])
            for j in range(self.cols_int_a):
                self.var_a[i].append(StringVar())
                entries_a[i].append(Entry(self.input, textvariable=self.var_a[i][j], width=5))
                entries_a[i][j].grid(row=i+2, column=j+2)
        Button(self.input, text="Enter", width=8, command=self.matrix_2).grid(row=self.rows_int_a+self.cols_int_a+10, column=1)
        self.input.mainloop()
    #Vytvori okno kam se zada velikost prnvi matice a pocet sloupcu druhe.
    def __init__(self):
            self.gui_multiply = None
            self.input = None
            self.output = None
            self.matrix_a = None
            self.matrix_b =None
            self.rows_a = None
            self.cols_a = None
            self.rows_b = None
            self.cols_b = None
            self.gui_multiply = Toplevel()
            self.gui_multiply.geometry("270x80")
            self.rows_a = Entry(self.gui_multiply)
            self.rows_a.grid(row=1, column=1)
            Label(self.gui_multiply, text=' x').grid(row=1, column=2)
            self.cols_a = Entry(self.gui_multiply)
            self.cols_a.grid(row=1, column=3)
            self.rows_b = self.cols_a
            Label(self.gui_multiply, text="p").grid(row=2, column=1)
            Label(self.gui_multiply, text=" x").grid(row=2, column=2)
            self.cols_b = Entry(self.gui_multiply)
            self.cols_b.grid(row=2, column=3)
            Button(self.gui_multiply, text='Enter',padx=20, pady=4, command=self.matrix_1).grid(row=3, column=3)