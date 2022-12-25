import tkinter as tk
from tkinter import ttk
from error import showError

class ProdInOrder(tk.Toplevel):
  def __init__(self, parent,api):
    super().__init__(parent)
    self.idProd = tk.StringVar()
    self.idOrder = tk.StringVar()
    self.amount=tk.StringVar()
    self.api=api
    self.connect=self.api.conToDat()
    self.tree = None
    self.entryIdProd = tk.Entry(self, textvariable=self.idProd)
    self.entryIdOrder = tk.Entry(self, textvariable=self.idOrder)
    self.entryAmount = tk.Entry(self, textvariable=self.amount)
    self.title("Заказы")
    self.printTable()
    btn = tk.Button(self, text="Добавить",command=self.insertProd,width=20)
    tk.Label(self, text="Номер Заказа :").grid(row=1, column=0)
    tk.Label(self, text="Номер Продукта :").grid(row=2, column=0)
    tk.Label(self, text="Количество :").grid(row=3, column=0)
    self.entryIdOrder.grid(row=1, column=1)
    self.entryIdProd.grid(row=2, column=1)
    self.entryAmount.grid(row=3, column=1)
    btn.grid(row=4, columnspan=1)


  def insertProd(self):
    idProd = self.idProd.get()
    idOrder = self.idOrder.get()
    Amount= self.amount.get()
    error=self.api.ADD_PROD_ORDER(self.connect,idOrder,idProd,Amount)
    print(error)
    if(error!=None):
        showError(self,error)
        return -1
    self.printTable()

  def printTable(self):
    rows,columns=self.api.select(self.connect,"POS_ORDER")
    self.tree = ttk.Treeview(self, show="headings", columns=columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0, columnspan=40)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i])

    self.entryIdProd.delete(0, tk.END)
    self.entryIdOrder.delete(0, tk.END)
    self.entryAmount.delete(0, tk.END)