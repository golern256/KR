import tkinter as tk
from tkinter import ttk
from error import showError
class typeProd(tk.Toplevel):
  def __init__(self, parent,api):
    super().__init__(parent)
    self.idProd = tk.StringVar()
    self.api=api
    self.connect=self.api.conToDat()
    self.tree = None
    self.entryIdProd = tk.Entry(self, textvariable=self.idProd)
    self.title("Типовое изделие")
    self.printTable()
    btn = tk.Button(self, text="Добавить",command=self.addProd,width=20)
    tk.Label(self, text="Номер Тип. Изделия :").grid(row=1, column=0)
    self.entryIdProd.grid(row=1, column=1)
    btn.grid(row=4, columnspan=1)

  def addProd(self):
    idProd = self.idProd.get()
    error=self.api.NEW_VAR_PROD(self.connect,idProd)
    if(error!=None):
        showError(self,error)
        return -1
    self.printTable()

  def printTable(self):
    rows,columns=self.api.select(self.connect,"PROD")
    self.tree = ttk.Treeview(self, show="headings", columns=columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0, columnspan=40)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i])

    self.entryIdProd.delete(0, tk.END)
