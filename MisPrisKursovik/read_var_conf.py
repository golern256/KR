import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

class readVarConf(tk.Toplevel):
  
  def __init__(self, parent,api):
    super().__init__(parent)
    self.api=api
    self.connect=self.api.conToDat()

    self.api.READ_VAR_CONF(self.connect,193)

    self.tree = None
    self.columns = None

    self.label = tk.Label(self, text='ID_PROD: ', padx=10, pady=10)
    self.label.grid(row=1, columnspan=1)

    self.id_prod = tk.StringVar()
    self.id_prod = tk.Entry(self, textvariable=self.id_prod)
    self.id_prod.grid(row=2, column=0)

    btn = tk.Button(self, text="Вывести",command=self.printTable)
    btn.grid(row=3, columnspan=2, pady=10, padx=10)

  def open(self):
    rows,self.columns=self.api.select(self.connect, 'PARAM')

    self.tree=ttk.Treeview(self, show="headings", columns=self.columns)
    
    for row in rows:
      self.tree.insert("", tk.END, values=' ')
      self.tree.grid(row=5, column=0)

    for i in range(len(self.columns)):
      self.tree.heading(self.columns[i], text=self.columns[i])  

  def printTable(self):
    rows = self.api.READ_VAR_CONF(self.connect,self.id_prod.get())
    print(rows)
    if type(rows)!=list:
      rows = [' ' for i in self.columns]

    self.tree=ttk.Treeview(self, show="headings", columns=self.columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0)

    for i in range(len(self.columns)):
      self.tree.column(self.columns[i], anchor="s")
      self.tree.heading(self.columns[i], text=self.columns[i]) 