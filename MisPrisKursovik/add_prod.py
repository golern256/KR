import tkinter as tk
from tkinter import ttk
from error import showError

class addProd(tk.Toplevel):
  def __init__(self, parent,api):
    super().__init__(parent)
    self.name = tk.StringVar()
    self.idClass = tk.StringVar()
    self.conf = tk.StringVar()
    self.typeProd = tk.StringVar()
    self.api=api
    self.connect=self.api.conToDat()
    self.entryName = tk.Entry(self, textvariable=self.name)
    self.entryIdClass = tk.Entry(self, textvariable=self.idClass)
    self.entryConf = tk.Entry(self, textvariable=self.conf)
    self.entryTypeProd = tk.Entry(self, textvariable=self.typeProd)
    self.title("Добавление продукта")
    self.printTable()
    btn = tk.Button(self, text="Добавить",command=self.addProd,width=20)
    tk.Label(self, text="NAME: ").grid(row=1, column=0)
    tk.Label(self, text="ID_CLASS: ").grid(row=2, column=0)
    tk.Label(self, text="CONF: ").grid(row=3, column=0)
    tk.Label(self, text="TYPE_PROD: ").grid(row=4, column=0)
    self.entryName.grid(row=1, column=1)
    self.entryIdClass.grid(row=2, column=1)
    self.entryConf.grid(row=3, column=1)
    self.entryTypeProd.grid(row=4, column=1)
    btn.grid(row=5, columnspan=1)


  def addProd(self):
    name = self.name.get()
    idClass = self.idClass.get()
    conf = self.conf.get()
    typeProd = self.typeProd.get()

    error=self.api.ADD_PROD(self.connect, name, idClass, conf, typeProd)
    print(error)
    if(error!=None):
        showError(self,error)
        return -1
    self.printTable()

  def printTable(self):
    rows,columns=self.api.select(self.connect,"PROD")

    self.tree=ttk.Treeview(self, show="headings", columns=columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=6, column=0,columnspan=40)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i])

    self.entryName.delete(0, tk.END)
    self.entryIdClass.delete(0, tk.END)
    self.entryConf.delete(0, tk.END)
    self.entryTypeProd.delete(0, tk.END)