import customtkinter as ctk
import math
from frames import *
from va_rating import VA_Rating
from settings import WIDTH, HEIGHT


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VA Disability Calculator")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.minsize(WIDTH, HEIGHT)
        self.configure(fg_color="#202020")

        self.extremity = "other"
        self.l_arm, self.r_arm, self.l_leg, self.r_leg, self.other = [], [], [], [], []
        self.rating = 0
        self.leg_bilateral_factor = 0
        self.arm_bilateral_factor = 0

        self.bilateral = Bilateral(self)
        self.percentage = Percentages(self)
        self.demographics = Demographics(self)
        self.information = Information(self)

    def set_extremity(self, extremity: str):
        self.extremity = extremity

    def compile_extremity_ratings(self, extremity: str):
        compiled_ratings = []
        for i in range(len(getattr(self, "l_" + extremity))):
            compiled_ratings.append(getattr(self, "l_" + extremity)[i])
        for j in range(len(getattr(self, "r_" + extremity))):
            compiled_ratings.append(getattr(self, "r_" + extremity)[j])
        setattr(self, extremity, compiled_ratings)
        if (
            len(getattr(self, "l_" + extremity)) > 0
            and len(getattr(self, "r_" + extremity)) > 0
        ):
            setattr(
                self,
                extremity + "_bilateral_factor",
                VA_Rating(getattr(self, extremity)).rating() * 0.1,
            )

    def set_percentage(self, percentage: int):
        if percentage != 0:
            match self.extremity:
                case "l_leg":
                    self.l_leg.append(percentage)
                case "r_leg":
                    self.r_leg.append(percentage)
                case "l_arm":
                    self.l_arm.append(percentage)
                case "r_arm":
                    self.r_arm.append(percentage)
                case "other":
                    self.other.append(percentage)

        self.compile_extremity_ratings("leg")
        self.compile_extremity_ratings("arm")

        total_rating = []
        for leg in range(len(self.leg)):
            total_rating.append(self.leg[leg])
        total_rating.append(self.leg_bilateral_factor)
        for arm in range(len(self.arm)):
            total_rating.append(self.arm[arm])
        total_rating.append(self.arm_bilateral_factor)
        for other in range(len(self.other)):
            total_rating.append(self.other[other])

        self.information.ratings_list.configure(
            text=str(self.leg + self.arm + self.other)
            + " Bilateral Factor: "
            + str(round(self.leg_bilateral_factor + self.arm_bilateral_factor, 1))
            + "%"
        )

        self.payment = VA_Rating(total_rating)

        rounded_rating = round(math.floor(self.payment.rating()) / 10) * 10
        self.information.rating.configure(
            text="VA Rating: " + str(rounded_rating) + "%"
        )

        values = self.demographics.get_values()

        self.payment.set(
            mar_status=values[0],
            under18=values[1],
            over18=values[2],
            parents=values[3],
            aid=values[4],
        )

        self.information.va_payment.configure(text=self.payment.text())


if __name__ == "__main__":
    app = App()
    app.mainloop()
