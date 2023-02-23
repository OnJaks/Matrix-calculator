from tkinter import *
from tkinter import messagebox
from math import floor
class Matrix_gauss_jordan_elimination:
        #Nejdrive upravi tak, aby na diagonale nebyla nula, potom upravi radek, tento proces se opakuje dokud nedostane upravenou matici.
        def RREF(self):
            for i in range(self.rows_int):
                if self.matrix_a[i][i]==0:
                    a = 1
                    while (i+a)<self.rows_int and self.matrix_a[i+a][i]==0:
                        a+=1
                    if (i+a)==self.rows_int:
                        break
                    for k in range(1+self.rows_int):
                        tt = self.matrix_a[i][k]
                        self.matrix_a[i][k] = self.matrix_a[i+a][k] 
                        self.matrix_a[i+a][k] = tt
                for j in range(self.rows_int):
                    if i != j:
                        t = (self.matrix_a[j][i]/self.matrix_a[i][i])
                        for k in range(self.rows_int+1):
                            self.matrix_a[j][k] = self.matrix_a[j][k]-self.matrix_a[i][k]*t
        #Nejdrive spusti funkci RREF.
        #Nasledne secte prvky a potom pokud vychazi jedno reseni, tak upravuje prvky, tak aby vysel RREF.
        #Nasledne prvky prevede na int nebo na float.
        def GJ_elimination(self):
            self.RREF()
            for i in range(self.rows_int):
                if self.matrix_a[i][i] != 0:
                    self.matrix_a[i][self.rows_int] = self.matrix_a[i][self.rows_int]/self.matrix_a[i][i]
                    self.matrix_a[i][i] = self.matrix_a[i][i]/self.matrix_a[i][i]
            for i in range(len(self.matrix_a)):
                for j in range(len(self.matrix_a[i])):
                    if floor(self.matrix_a[i][j])-self.matrix_a[i][j] == 0:
                        self.matrix_a[i][j] = int(self.matrix_a[i][j])
                    else:
                        self.matrix_a[i][j] = round(self.matrix_a[i][j], 2)
            return self.matrix_a
        #Upravi matici, aby prvky byly typu float.
        #Spusti funkci GJ_elimination.
        #Vytvori okno kam vytiskne upravenou matici.
        def output(self):
            self.input.destroy()
            self.matrix_a=[]
            for i in range(self.rows_int):
                self.matrix_a.append([])
                for j in range(self.cols_int):
                    self.matrix_a[i].append(float(self.var_a[i][j].get()))
            self.output = Toplevel()
            Label(self.output, text="RREF matrix:", font=("arial", 10, "bold")).grid(row=1, column=1)
            self.output_matrix = self.GJ_elimination()
            for i in range(len(self.output_matrix)):
                for j in range(len(self.output_matrix[i])):
                    Label(self.output, text=self.output_matrix[i][j], bd=5).grid(row=i+2, column=3+j)
            self.output.mainloop()
        #Zpracuje matici, jestli neni prazdne 'n' nebo jestli neni mensi nez 2 nebo vetsi nez 10.
        #Vytvori okno na zadani prvku matice.
        def matrix_1(self):
            if self.rows.get()=="" or self.cols.get() == "":
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_elimination.destroy()
                return
            self.rows_int = int(self.rows.get())
            self.cols_int = int(self.cols.get())
            if self.rows_int<=1 or self.rows_int>10 or self.cols_int <=1 or self.cols_int>10:
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_elimination.destroy()
                return
            self.gui_elimination.destroy()
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
        #Vytvori okno kam zasadime rozmery matice pro RREF.
        def __init__(self):
            self.gui_elimination = None
            self.input = None
            self.matrix_a = None
            self.rows = None
            self.cols =None
            self.gui_elimination = Toplevel()
            self.gui_elimination.geometry("270x80")
            self.rows = Entry(self.gui_elimination)
            self.rows.grid(row=2, column=1)
            self.cols = Entry(self.gui_elimination)
            self.cols.grid(row=2, column=3)
            Label(self.gui_elimination, text=' x').grid(row=2, column=2)
            Button(self.gui_elimination, text='Enter',padx=20, pady=4, command=self.matrix_1).grid(row=4, column=3)