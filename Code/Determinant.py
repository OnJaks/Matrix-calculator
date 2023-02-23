from tkinter import *
from tkinter import messagebox
class Matrix_determinant:
        #Nejdrive je vypocet pro matice 2x2, vynasobenim diagonaly a odecteni druhe diagonaly.
        #Pro vetsi matice vypocita det. pomoci rekurze. 
        #Secitame dilci determinanty az zjistime vysledny det a ten orizne 2 des. cisla.
        def det(self, mat):
            n = len(mat)
            if n == 2: return round(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1], 2)
            determinant = 0          
            for i in range(n):
                deter = Matrix_determinant.det(self, [r[:i]+r[i+1:] for r in (mat[:0]+mat[1:])])
                determinant += ((-1)**i)*mat[0][i]*deter
            return round(determinant, 2)
        #Upravi matici, aby prvky byly typu float.
        #Spusti funkci det.
        #Vytvori okno kam vytiskne determinant.
        def output(self):
            self.input.destroy()
            self.matrix_a=[]
            for i in range(self.rows_int):
                self.matrix_a.append([])
                for j in range(self.cols_int):
                    self.matrix_a[i].append(float(self.var_a[i][j].get()))
            self.output = Toplevel()
            Label(self.output, text="Determinat:", font=("arial", 10, "bold")).grid(row=1, column=1)
            self.determinant = self.det(self.matrix_a)
            Label(self.output, text= self.determinant, bd=5).grid(row=1, column=3)
            self.output.mainloop()
        #Zpracuje matici, jestli neni prazdne 'n' nebo jestli neni mensi nez 2 nebo vetsi nez 10.
        #Vytvori okno na zadani prvku matice.
        def matrix_1(self):
            if self.rows.get()=="":
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_det.destroy()
                return
            self.rows_int = int(self.rows.get())
            self.cols_int = self.rows_int
            if self.rows_int<=1 or self.rows_int>10:
                messagebox.showwarning("Warning!", "Maximum size of matrix can be 10x10 and minimum size of matrix can be 2x2.")
                self.gui_det.destroy()
                return
            self.gui_det.destroy()
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
        #Vytvori okno na vstup inverzni matice. Musi byt ctvercova
        def __init__(self):
            self.gui_det = None
            self.input = None
            self.determinant = None
            self.matrix_a = None
            self.rows = None
            self.cols =None
            self.gui_det = Toplevel()
            self.gui_det.geometry("270x80")
            self.rows = Entry(self.gui_det)
            self.rows.grid(row=3, column=1)
            self.cols =self.rows
            Label(self.gui_det, text=' x n').grid(row=3, column=2)
            Button(self.gui_det, text='Enter',padx=20, pady=4, command=self.matrix_1).grid(row=4, column=3)
