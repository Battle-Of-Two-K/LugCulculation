import tkinter as tk
from win32api import GetSystemMetrics

width_screen_this_computer = GetSystemMetrics(0)
height_screen_this_computer = GetSystemMetrics(1)


class Slide(tk.Frame):
    """
    Слайд с кнопкой(ами) в необходимой конфигурации.
    """

    def __init__(self, master, slide_variant):
        super().__init__(master)

        if slide_variant == 1:
            self.btn_back, self.btn_next = None, tk.Button(master, text="Далее >")
        elif slide_variant == 2:
            self.btn_back, self.btn_next = tk.Button(master, text="< Назад"), \
                                           tk.Button(master, text="Далее >")
        elif slide_variant == 3:
            self.btn_back, self.btn_next = tk.Button(master, text="< Назад"), None
        else:
            self.btn_back, self.btn_next = None, None


class InputInitialDataSlide(Slide):
    """
    Слайд, на котором вводятся входные данные.
    """

    frames = []

    def __init__(self, master, amount_data_lines, slide_variant=1):
        super().__init__(master, slide_variant)

        for i in range(amount_data_lines):
            self.frames.append(tk.Frame(master))


class OutputResultSlide(Slide):
    """
    Слайд, на котором выводится результат расчёта.
    """

    def __init__(self, master, slide_variant=2):
        super().__init__(master, slide_variant)


class EndSlide(Slide):
    """
    Итоговый слайд.
    """

    def __init__(self, master, slide_variant=3):
        super().__init__(master, slide_variant)


class App:
    width = 720
    height = 400

    initial_slide_data = [[" Сила, вызывающая разрыв проушины - P: ", " [тс] "],
                          [" Число поверхностей среза болта - m: ", " [шт.] "],
                          [" Предел прочности материала болта - σ", " [(даН)/(мм^2)] "]]

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}+"
                           f"{int((width_screen_this_computer - self.width) / 2)}+"
                           f"{int((height_screen_this_computer - self.height) / 2)}")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.create_initial_slide()

    def create_initial_slide(self):
        all_lines = []  # необходим, чтобы "отловить" объекты для последующих махинаций с ними

        input_initial_data_slide = InputInitialDataSlide(self.main_frame, len(self.initial_slide_data))

        def create_line(text: list, master):
            return tk.Label(master, text=f"{text[0]}"), tk.Entry(master), tk.Label(master, text=f"{text[1]}"),\
                   tk.Checkbutton(master)

        def pack_line(line: tuple):
            for widget in line:
                widget.pack(side=tk.LEFT)
                widget.master.pack()

        if len(self.initial_slide_data) == len(input_initial_data_slide.frames):
            for i in range(0, len(self.initial_slide_data)):
                pack_line(create_line(self.initial_slide_data[i], input_initial_data_slide.frames[i]))
                all_lines.append(create_line(self.initial_slide_data[i], input_initial_data_slide.frames[i]))

        input_initial_data_slide.btn_next.pack(side=tk.RIGHT)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
