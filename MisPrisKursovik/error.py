import tkinter.messagebox as mb
def showError(window,msg):
  mb.showerror("Ошибка", msg)
  window.destroy()
