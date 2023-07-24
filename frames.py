from widgets import *


class Bilateral(Frame):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.parent = parent
        self.extremeties = {
            "l_leg": "Left Leg",
            "r_leg": "Right Leg",
            "l_arm": "Left Arm",
            "r_arm": "Right Arm",
            "other": "Other",
        }
        self.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.08)

        self.build()

    def build(self):
        i = 0
        for key, value in self.extremeties.items():
            extremity = Extremity(self, key, value)
            extremity.place(relx=i * 0.2 + 0.01, rely=0, relwidth=0.18, relheight=1)
            setattr(self, key, extremity)
            i += 1
        self.set_focus("other")

    def set_focus(self, key: str):
        for item in list(self.extremeties.keys()):
            focus = True if item == key else False
            getattr(self, item).set_has_focus(focus)
            if focus:
                self.parent.set_extremity(item)


class Percentages(Frame):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.parent = parent
        self.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.16)

        self.build()

    def build(self):
        percentages = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]]
        for i in range(2):
            for j in range(5):
                percentage = Percentage(self, percentages[i][j])
                percentage.place(
                    relx=j * 0.2 + 0.01,
                    rely=i * 0.52 + 0.01,
                    relwidth=0.18,
                    relheight=0.48,
                )
                setattr(self, "percent" + percentage.__str__(), percentage)

    def set_percentage(self, percent: int):
        self.parent.set_percentage(percent)


class Demographics(Frame):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.parent = parent

        self.place(relx=0.01, rely=0.28, relwidth=0.98, relheight=0.32)

        self.build()

    def build(self):
        num_list = [str(i) for i in range(0, 11)]
        marital_status_label = Label(self, "Marital Status")
        self.marital_status = Option(self, ["S", "M"])
        under_18_label = Label(self, "Children Under 18")
        self.under_18 = Option(self, num_list)
        over_18_label = Label(self, "Children Over 18")
        self.over_18 = Option(self, num_list)
        dep_parents_label = Label(self, "Dependent Parents")
        self.dep_parents = Option(self, ["0", "1", "2"])
        aid_label = Label(self, "Does Spouse Require Aid and Attendance?")
        self.aid = Option(self, ["No", "Yes"])

        marital_status_label.grid(row=0, column=0, padx=5, pady=5)
        self.marital_status.grid(row=0, column=1, padx=5, pady=5)
        under_18_label.grid(row=0, column=2, padx=5, pady=5)
        self.under_18.grid(row=0, column=3, padx=5, pady=5)
        over_18_label.grid(row=1, column=0, padx=5, pady=5)
        self.over_18.grid(row=1, column=1, padx=5, pady=5)
        dep_parents_label.grid(row=1, column=2, padx=5, pady=5)
        self.dep_parents.grid(row=1, column=3, padx=5, pady=5)
        aid_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.aid.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def update_rating(self, option: any):
        try:
            self.parent.set_percentage(0)
        except UnboundLocalError:
            return

    def get_values(self):
        return [
            self.marital_status.get(),
            int(self.under_18.get()),
            int(self.over_18.get()),
            int(self.dep_parents.get()),
            True if self.aid.get() == "Yes" else False,
        ]


class Information(Frame):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.parent = parent

        self.ratings_list = Label(self, "")
        self.rating = Label(self, str(self.parent.rating) + "%")
        self.rating.big()
        self.va_payment = Label(self, "")
        self.va_payment.big()

        self.place(relx=0.01, rely=0.7, relwidth=0.98, relheight=0.28)

        self.ratings_list.pack()
        self.rating.pack()
        self.va_payment.pack()
