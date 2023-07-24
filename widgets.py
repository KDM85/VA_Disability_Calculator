import customtkinter as ctk


class Frame(ctk.CTkFrame):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.configure(fg_color="#202020")


class Percentage(ctk.CTkButton):
    def __init__(self, parent: object, percent: int):
        super().__init__(parent)
        self.parent = parent
        self.percent = percent
        self.configure(
            text=str(percent) + "%",
            height=10,
            corner_radius=20,
            fg_color="orangered",
            hover_color="chocolate1",
            font=("Tahoma", 12, "bold"),
            command=lambda: self.parent.set_percentage(percent),
        )

    def __str__(self):
        return str(self.percent)


class Extremity(ctk.CTkButton):
    def __init__(self, parent: object, key: str, value: str):
        super().__init__(parent)
        self.parent = parent
        self.has_focus = False
        self.configure(
            text=value,
            corner_radius=20,
            fg_color="#505050",
            hover_color="chocolate1",
            font=("Tahoma", 12, "bold"),
            command=lambda: self.parent.set_focus(key),
        )

    def set_has_focus(self, focus: bool):
        self.has_focus = focus
        self.set_color()

    def set_color(self):
        if self.has_focus:
            self.configure(fg_color="orangered")
        else:
            self.configure(fg_color="#505050")


class Label(ctk.CTkLabel):
    def __init__(self, parent: object, text: str):
        super().__init__(parent)
        self.configure(text=text, font=("Tahoma", 14))

    def big(self):
        self.configure(font=("Tahoma", 24, "bold"))


class Option(ctk.CTkOptionMenu):
    def __init__(self, parent: object, values: list):
        super().__init__(parent)
        self.parent = parent
        self.configure(
            height=20,
            width=20,
            corner_radius=20,
            font=("Tahoma", 16, "bold"),
            fg_color="#202020",
            button_color="orangered",
            button_hover_color="chocolate1",
            dropdown_fg_color="#202020",
            dropdown_hover_color="chocolate1",
            values=values,
            anchor="w",
            command=self.parent.update_rating,
        )
        self.set(values[0])
