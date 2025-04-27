# import datetime from datetime
from datetime import datetime


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, dt):
        return cls(dt.year, dt.month, dt.day)


# You should be able to run the code below with no errors:
today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)