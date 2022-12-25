import tkinter as tk
from tkinter import ttk
from error import showError
class Order(tk.Toplevel):
  def __init__(self, parent,api):
    super().__init__(parent)
    self.idCustomer = tk.StringVar()
    self.Date = tk.StringVar()
    self.Num = tk.StringVar()
    self.api=api
    self.connect=self.api.conToDat()
    self.tree = None
    self.entryIdCustomer = tk.Entry(self, textvariable=self.idCustomer)
    self.entryDate = tk.Entry(self, textvariable=self.Date)
    self.entryNum = tk.Entry(self, textvariable=self.Num)
    self.title("Заказ")
    self.printTable()
    btn = tk.Button(self, text="Добавить",command=self.insertOrder,width=20)
    tk.Label(self, text="Номер пользователя :").grid(row=1, column=0)
    tk.Label(self, text="Дата :").grid(row=2, column=0)
    tk.Label(self, text="Номер заказа :").grid(row=3, column=0)
    self.entryIdCustomer.grid(row=1, column=1)
    self.entryDate.grid(row=2, column=1)
    self.entryNum.grid(row=3, column=1)
    btn.grid(row=4, columnspan=1)


  def insertOrder(self):
    idCustomer = self.idCustomer.get()
    date = self.Date.get()
    num = self.Num.get()
    error=self.api.INS_ORDER(self.connect, idCustomer, date, num)
    print(error)
    if(error!=None):
        showError(self,error)
        return -1
    self.printTable()

  def printTable(self):
    rows,columns=self.api.select(self.connect,"ORDER1")
    self.tree = ttk.Treeview(self, show="headings", columns=columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0, columnspan=40)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i])
    self.entryIdCustomer.delete(0, tk.END)
    self.entryDate.delete(0, tk.END)
    self.entryNum.delete(0, tk.END)

