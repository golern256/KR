import tkinter as tk
from tkinter import ttk
from error import showError
class paramValue(tk.Toplevel):
  def __init__(self, parent,api):
    super().__init__(parent)
    self.idProd = tk.StringVar()
    self.idPar = tk.StringVar()
    self.Value = tk.StringVar()
    self.api=api
    self.connect=self.api.conToDat()
    self.tree = None
    self.entryIdProd = tk.Entry(self, textvariable=self.idProd)
    self.entryIdPar = tk.Entry(self, textvariable=self.idPar)
    self.entryValue = tk.Entry(self, textvariable=self.Value)
    self.title("Параметры")
    self.printTable()
    btn = tk.Button(self, text="Добавить",command=self.insertParam,width=20)
    tk.Label(self, text="Номер Продукта :").grid(row=1, column=0)
    tk.Label(self, text="Номер Параметра :").grid(row=2, column=0)
    tk.Label(self, text="Значение :").grid(row=3, column=0)
    self.entryIdProd.grid(row=1, column=1)
    self.entryIdPar.grid(row=2, column=1)
    self.entryValue.grid(row=3, column=1)
    btn.grid(row=4, columnspan=1)


  def insertParam(self):
    idProd = self.idProd.get()
    idPar = self.idPar.get()
    Value= self.Value.get()
    error=self.api.WRITE_PAR2(self.connect,idProd,idPar,Value)
    print(error)
    if(error!=None):
        showError(self,error)
        return -1
    self.printTable()

  def printTable(self):
    rows,columns=self.api.select(self.connect,"PARAM_VALUE")
    self.tree = ttk.Treeview(self, show="headings", columns=columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0, columnspan=40)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i])

    self.entryIdProd.delete(0, tk.END)
    self.entryIdPar.delete(0, tk.END)
    self.entryValue.delete(0, tk.END)