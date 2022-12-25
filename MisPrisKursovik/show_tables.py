import tkinter as tk
from tkinter import ttk


class showTables(tk.Toplevel):

  def __init__(self, parent,api):
    super().__init__(parent)
    self.api=api
    self.connect=self.api.conToDat()
    self.tablesNames = self.api.getTablesNames(self.connect)

    self.combobox = ttk.Combobox(self, values=self.tablesNames)
    self.combobox.grid(row=0, column=0, pady=10, padx=10)
    self.tree = None
    btn = tk.Button(self, text="Вывести",command=self.printTable)
    btn.grid(row=1, columnspan=1, pady=10, padx=10)
    self.label = tk.Label(self, text=self.tablesNames[0], font=("Arial", 14),
                          padx=10, pady=10)
    self.label.grid(row=2, columnspan=1)

  def open(self):
    rows,columns=self.api.select(self.connect, self.tablesNames[0])
    self.tree=ttk.Treeview(self, show="headings", columns=columns)

    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i])



  def printTable(self):
    self.tree.destroy()
    self.label.config(text = self.combobox.get())
    rows,columns=self.api.select(self.connect, self.combobox.get())

    self.tree=ttk.Treeview(self, show="headings", columns=columns)
    for row in rows:
      self.tree.insert("", tk.END, values=row)
      self.tree.grid(row=5, column=0)

    for i in range(len(columns)):
      self.tree.column(columns[i], anchor="s")
      self.tree.heading(columns[i], text=columns[i]) 
