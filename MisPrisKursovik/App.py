import tkinter as tk
from insertOrder import Order
from addParamValue import paramValue
from createTypeProd import typeProd
from addProdInOrder import ProdInOrder
from show_tables import showTables
from read_var_conf import readVarConf
from add_prod import addProd
class App(tk.Tk):
  def __init__(self, api):
    super().__init__()
    self.api = api
    label_space = tk.Label(text="    ")
    label_space.pack()
    label_name = tk.Label(text="Приемы моделирования заказов на изделия", font=("Arial", 14))
    label_name.pack()
    label_name = tk.Label(text="с вариантами исполнения", font=("Arial", 14))
    label_name.pack()
    label_space = tk.Label(text="    ")
    label_space.pack()
    btn = tk.Button(self, text="Добавленные товара без конфигурации в заказ", width=45, command=self.openAddProdInOrderWindow)
    btn.pack(padx=100, pady=10)
    btn = tk.Button(self, text="Задать величину параметра", width=45, command=self.openAddParWindow)
    btn.pack(padx=15, pady=10)
    btn = tk.Button(self, text="Отображение параметров типового изделия", width=45, command=self.openReadConfWindow)
    btn.pack(padx=15, pady=10)
    btn = tk.Button(self, text="Создание типового изделия", width=45, command=self.openCreateTypeProdWindow)
    btn.pack(padx=15, pady=10)
    btn = tk.Button(self, text="Добавить заказ", width=45, command=self.openOrderWindow)
    btn.pack(padx=15, pady=10)
    btn = tk.Button(self, text="Вывести содержимое таблиц", width=45, command=self.openAllTablesWindow)
    btn.pack(padx=15, pady=10)
    btn = tk.Button(self, text="Добавить продукт", width=45, command=self.openAddProdWindow)
    btn.pack(padx=15, pady=10)
    label_space = tk.Label(text="    ")
    label_space.pack()
    btn = tk.Button(self, text="Выход", command=self.quit, width=45)
    btn.pack(padx=15, pady=10)
    label_space = tk.Label(text="    ")
    label_space.pack()
    self.title("Приемы моделирования заказов на изделия с вариантами исполнения")

  def openOrderWindow(self):
    Order(self,self.api)

  def openAddParWindow(self):
    paramValue(self,self.api)

  def openCreateTypeProdWindow(self):
    typeProd(self,self.api)

  def openAddProdInOrderWindow(self):
    ProdInOrder(self,self.api)

  def openAllTablesWindow(self):
    window =showTables(self,self.api)
    window.open()

  def openReadConfWindow(self):
    window = readVarConf(self, self.api)
    window.open()

  def openAddProdWindow(self):
    addProd(self, self.api)