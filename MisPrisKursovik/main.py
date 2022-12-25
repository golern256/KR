from App import App
from Backend import Backend

if __name__ == "__main__":
    api=Backend()
    app = App(api)
    app.mainloop()

