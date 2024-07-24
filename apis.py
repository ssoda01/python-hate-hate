import datetime as dt
import requests

from pydantic import BaseModel, Field

URL = "https://www.gov.uk/bank-holidays.json"


class Event(BaseModel):
    title: str
    date: dt.date
    notes: str
    bunting: bool
    @property
    def is_passed(self)->bool:
        return self.date < dt.date.today()

class Division(BaseModel):
    name: str = Field(alias="division")
    # division: str
    events: list[Event]


class BankHolidays(BaseModel):
    england_and_wales: Division
    scotland: Division
    northern_ireland: Division

    class Config:
        def alias_generator(x): return x.replace("_", "-")


if __name__ == "__main__":
    data = requests.get(URL).json()
    holidays = BankHolidays(**data)
    print(holidays.england_and_wales.events[0].is_passed)
    # print(holidays.england_and_wales.division)
