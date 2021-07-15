import tkinter as tk
from tkinter import ttk
from win32api import GetSystemMetrics

width_screen_this_computer = GetSystemMetrics(0)
height_screen_this_computer = GetSystemMetrics(1)
font = "Times 14"


class Slide(ttk.Frame):
    """
    Слайд с кнопкой(ами) в необходимой конфигурации.
    """

    def __init__(self, master, slide_variant):
        super().__init__(master)

        if slide_variant == 1:
            self.btn_back, self.btn_next = None, ttk.Button(master, text="Далее >")
        elif slide_variant == 2:
            self.btn_back, self.btn_next = ttk.Button(master, text="< Назад"), \
                                           ttk.Button(master, text="Далее >")
        elif slide_variant == 3:
            self.btn_back, self.btn_next = ttk.Button(master, text="< Назад"), None
        else:
            self.btn_back, self.btn_next = None, None


class InputInitialDataSlide(Slide):
    """
    Слайд, на котором вводятся входные данные.
    """

    def __init__(self, master, slide_variant=1):
        super().__init__(master, slide_variant)
        self.frame = tk.Frame(master)


class OutputResultSlide(Slide):
    """
    Слайд, на котором выводится результат расчёта.
    """

    def __init__(self, master, slide_variant=2):
        super().__init__(master, slide_variant)
        self.frame = tk.Frame(master)


class EndSlide(Slide):
    """
    Итоговый слайд.
    """

    def __init__(self, master, slide_variant=3):
        super().__init__(master, slide_variant)
        self.frame = tk.Frame(master)


class ColumnData(ttk.Frame):
    set_vidgets = None

    def __init__(self, master, data, index):
        super().__init__(master)
        self.frame = tk.Frame(master)

        if index == "Label":
            self.set_vidgets = [ttk.Label(self.frame, text=f"{row}", font=font) for row in data]
        elif index == "Entry":
            self.set_vidgets = [ttk.Entry(self.frame, font=font) for _ in range(len(data))]


class ColumnDataLabel(ColumnData):
    def __init__(self, master, data, index="Label"):
        super().__init__(master, data, index)


class ColumnDataEntry(ColumnData):
    def __init__(self, master, data, index="Entry"):
        super().__init__(master, data, index)


class App:
    width = 720
    height = 150

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}+"
                           f"{int((width_screen_this_computer - self.width) / 2)}+"
                           f"{int((height_screen_this_computer - self.height) / 2)}")

        self.root.resizable(width=False, height=False)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack()

        self.create_initial_slide()

    def create_initial_slide(self):
        input_initial_data_slide = InputInitialDataSlide(self.main_frame)

        data = [[" Сила, вызывающая разрыв проушины - P: ", " Число поверхностей среза болта - m: ",
                 " Предел прочности материала болта - σ:"], [None, None, None],
                [" [тс] ", " [шт.] ", " [(даН)/(мм^2)] "]]

        for info in data:
            self.create_data_column(input_initial_data_slide.frame, info)

        input_initial_data_slide.frame.pack()
        input_initial_data_slide.btn_next.pack(side=tk.RIGHT, padx=30, pady=10)

    @staticmethod
    def create_data_column(master, data):
        if isinstance(data[0], str):
            column = ColumnDataLabel(master, data)

            for obj in column.set_vidgets:
                obj.pack(padx=10, pady=3, anchor=tk.W)

            column.frame.pack(side=tk.LEFT)

        elif isinstance(data[0], type(None)):
            column = ColumnDataEntry(master, data)

            for obj in column.set_vidgets:
                obj.pack(padx=10, pady=3, anchor=tk.W)

            column.frame.pack(side=tk.LEFT)

        else:
            pass

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
