from Determinant import Matrix_determinant
from tkinter import *
from tkinter import messagebox
from math import floor
class Matrix_inverse:
        #Inverzni matici nejdrive vyresime pro 2. 
        #Pomocí toho, že prvky vydeli determinantem a prehodime prvni a posledni prvek a druhy a treti vynasobime -1.
        #Pro vetsi matice pouzijeme kofaktory pro zjisteni inverzni matice.
        #Nasledne typy prvky matice prevedeme na int nebo na float.
        def inverse(self):
            if len(self.matrix_a) == 2:
                mat = [[self.matrix_a[1][1]/self.determinant, -1*self.matrix_a[0][1]/self.determinant],[-1*self.matrix_a[1][0]/self.determinant, self.matrix_a[0][0]/self.determinant]]
            self.m = []
            for i in range(len(self.matrix_a)):
                n = []
                for j in range(len(self.matrix_a)):
                    minor = [r[:j]+r[j+1:] for r in (self.matrix_a[:i]+self.matrix_a[i+1:])]
                    self.rows_int = self.cols_int = len(minor)
                    n.append(((-1)**(i+j))*Matrix_determinant.det(self, minor))
                self.m.append(n)
            mat = [[self.m[j][i] for j in range(len(self.m))] for i in range(len(self.m[0]))]
            for i in range(len(mat)):
                for j in range(len(mat)):
                    mat[i][j] = round(mat[i][j]/self.determinant, 2)
                    if floor(mat[i][j])-mat[i][j] == 0:
                        mat[i][j] = int(mat[i][j])
            return mat
        #Upravi matici, aby prvky byly typu float.
        #Zkontroluje, aby nebyl determinant nulovy.
        #Spusti funkci inverse.
        #Vytvori okno kam vytiskne inverzni matici.
        def output(self):
            self.input.destroy()
            self.matrix_a=[]
            for i in range(self.rows_int):
                self.matrix_a.append([])
                for j in range(self.cols_int):
                    self.matrix_a[i].append(float(self.var_a[i][j].get()))

            self.output = Toplevel()
            Label(self.output, text="Inverse matrix:", font=("arial", 10, "bold")).grid(row=1, column=1)
            self.determinant = Matrix_determinant.det(self, self.matrix_a)
            if int(self.determinant)==0:
                 self.output.destroy()
                 messagebox.showwarning("Warning!", "Determinant of matrix is 0.")
                 return
            self.output_matrix = self.inverse()
            for i in range(len(self.output_matrix)):
                for j in range(len(self.output_matrix[i])):
                    Label(self.output, text=self.output_matrix[i][j], bd=5).grid(row=i+2, column=3+j)
            self.output.mainloop()
        #Zpracuje matici, jestli neni prazdne 'n' nebo jestli neni mensi nez 2 nebo vetsi nez 10.
        #Vytvori okno na zadani prvku matice.
        def matrix_1(self):
            if self.rows.get()=="":
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_inverse.destroy()
                return
            self.rows_int = int(self.rows.get())
            self.cols_int = self.rows_int
            if self.rows_int<=1 or self.rows_int>10:
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_inverse.destroy()
                return
            self.gui_inverse.destroy()
            self.input = Toplevel()
            Label(self.input, text="Enter matrix:", font=('arial', 10, 'bold')).grid(row=1, column=1)
            entries_a = []
            self.var_a=[]
            for i in range(self.rows_int):
                entries_a.append([])
                self.var_a.append([])
                for j in range(self.cols_int):
                    self.var_a[i].append(StringVar())
                    entries_a[i].append(Entry(self.input, textvariable=self.var_a[i][j], width=5))
                    entries_a[i][j].grid(row=i+2, column=j+2)
            Button(self.input, text="Enter", width=8, command=self.output).grid(row=self.rows_int+self.cols_int+10, column=1)
            self.input.mainloop()
        #Vytvori okno na vstup inverzni matice. Musi byt regularni.
        def __init__(self):
            self.gui_inverse = None
            self.input = None
            self.determinant = None
            self.matrix_a = None
            self.rows = None
            self.cols =None
            self.gui_inverse = Toplevel()
            self.gui_inverse.geometry("270x80")
            self.rows = Entry(self.gui_inverse)
            self.rows.grid(row=3, column=1)
            self.cols =self.rows
            Label(self.gui_inverse, text=' x n').grid(row=3, column=2)
            Button(self.gui_inverse, text='Enter',padx=20, pady=4, command=self.matrix_1).grid(row=4, column=3)