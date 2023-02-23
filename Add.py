from tkinter import *
from tkinter import messagebox
from math import floor
class Matrix_add:
        #Tato metoda secte prvky mezi sebou a vytvori vystupni matici, tak aby ve vystupni matici byly prvky typu float nebo int.
        def sum(self):
            self.output_matrix = []
            for i in range(self.rows_int):
                self.output_matrix.append([])
                for j in range(self.cols_int):
                    self.output_matrix[i].append(0)
                    self.output_matrix[i][j] = (self.matrix_a[i][j]+self.matrix_b[i][j])
            for i in range(len(self.output_matrix)):
                for j in range(len(self.output_matrix[i])):
                    if floor(self.output_matrix[i][j])-self.output_matrix[i][j] == 0:
                        self.output_matrix[i][j] = int(self.output_matrix[i][j])
                    else:
                        self.output_matrix[i][j] = round(self.output_matrix[i][j], 2)
            return self.output_matrix
        #Vytvari okno kde se zobrazi vystupni matice a spousti metodu sum.
        def output_matrix(self):
            self.input.destroy()
            self.output = Toplevel()
            Label(self.output, text="Ouptut matrix:", font=("arial", 10, "bold")).grid(row=1, column=1)
            self.output_matrix = self.sum()
            for i in range(len(self.output_matrix)):
                for j in range(len(self.output_matrix[i])):
                    Label(self.output, text=self.output_matrix[i][j], bd=5).grid(row=i+2, column=3+j)
            self.output.mainloop()
        #Pretvari vstupy na matice s prvky typu float.
        def matrices(self):
            self.matrix_a=[]
            self.matrix_b=[]
            for i in range(self.rows_int):
                self.matrix_a.append([])
                self.matrix_b.append([])
                for j in range(self.cols_int):
                    self.matrix_a[i].append(float(self.var_a[i][j].get()))
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
            for i in range(self.rows_int):
                entries_b.append([])
                self.var_b.append([])
                for j in range(self.cols_int):
                    self.var_b[i].append(StringVar())
                    entries_b[i].append(Entry(self.input, textvariable=self.var_b[i][j], width=5))
                    entries_b[i][j].grid(row=i+2, column=j+2)
            Button(self.input, text="Enter", width=8, command=self.matrices).grid(row=self.cols_int + self.cols_int + 10, column=1)
        #Zpracovava prvni matice a kontroluje jestli je mensi nebo rovno 10x10 nebo alespon 2x2.
        #Vytvari okno na vlozeni prvku matice.
        def matrix_1(self):
            if self.cols.get()=='' or self.rows.get()=="":
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_add.destroy()
                return
            self.rows_int = int(self.rows.get())
            self.cols_int = int(self.cols.get())
            if self.rows_int<=1 or self.rows_int>10 or self.cols_int <=1 or self.cols_int>10:
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_add.destroy()
                return
            self.gui_add.destroy()
            self.input = Toplevel()
            Label(self.input, text="Enter matrix A:", font=('arial', 10, 'bold')).grid(row=1, column=1)
            entries_a = []
            self.var_a=[]
            for i in range(self.rows_int):
                entries_a.append([])
                self.var_a.append([])
                for j in range(self.cols_int):
                    self.var_a[i].append(StringVar())
                    entries_a[i].append(Entry(self.input, textvariable=self.var_a[i][j], width=5))
                    entries_a[i][j].grid(row=i+2, column=j+2)
            Button(self.input, text="Enter", width=8, command=self.matrix_2).grid(row=self.rows_int+self.cols_int+10, column=1)
            self.input.mainloop()
        #Vytvari okno na vlozeni velikosti matic.
        def __init__(self):
            self.gui_add = None
            self.input = None
            self.output = None
            self.matrix_a = None
            self.matrix_b =None
            self.rows = None
            self.cols = None
            self.gui_add = Toplevel()
            self.gui_add.geometry("270x80")
            self.rows = Entry(self.gui_add)
            self.rows.grid(row=3, column=1)
            Label(self.gui_add, text=' x').grid(row=3, column=2)
            self.cols = Entry(self.gui_add)
            self.cols.grid(row=3, column=3)
            Button(self.gui_add, text='Enter',padx=20, pady=4, command=self.matrix_1).grid(row=4, column=3)
