from settings import *


class VA_Rating:
    def __init__(
        self,
        rating_list: list,
        mar_status: str = "S",
        under18: int = 0,
        over18: int = 0,
        parents: int = 0,
        aid: str = False,
    ):
        self.rating_list = rating_list
        self.mar_status = mar_status
        self.under18 = under18
        self.over18 = over18
        self.parents = parents
        self.aid = aid
        self.va_rating = self.rating()

    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def rating(self) -> int:
        remaining = 100
        subtotal = 0
        for i in self.rating_list:
            subtotal += remaining * (i / 100)
            remaining -= remaining * (i / 100)
        return subtotal

    def text(self) -> str:
        return "${:,.2f}".format(self.payment())

    def payment(self):
        temp = round(self.rating() / 10) * 10
        self.set(va_rating=temp)
        match self.va_rating:
            case 10:
                return TEN_PCT
            case 20:
                return TWENTY_PCT
            case 30:
                i = 0
            case 40:
                i = 1
            case 50:
                i = 2
            case 60:
                i = 3
            case 70:
                i = 4
            case 80:
                i = 5
            case 90:
                i = 6
            case 100:
                i = 7

        if self.under18 > 0 or self.over18 > 0:
            chart = WITH_CHILD
        else:
            chart = NO_CHILD

        if self.mar_status == "S":
            if self.parents == 0:
                j = 0
            elif self.parents == 1:
                j = 4
            elif self.parents >= 2:
                j = 5
        elif self.mar_status == "M":
            if self.parents == 0:
                j = 1
            elif self.parents == 1:
                j = 2
            elif self.parents >= 2:
                j = 3

        under18_multiplier = self.under18 - 1
        over18_multiplier = self.over18 - 1

        output = chart[i][j]

        if self.aid:
            output += DEP_PAY[i][2]

        if under18_multiplier > 0:
            output += DEP_PAY[i][0] * under18_multiplier

        if over18_multiplier > 0:
            output += DEP_PAY[i][1] * over18_multiplier

        return output
