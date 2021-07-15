import tkinter as tk


class Slide(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.slide = Slide()
