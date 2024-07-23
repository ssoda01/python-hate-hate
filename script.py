from pydantic import BaseModel, field_validator
import datetime as dt


class Order(BaseModel):
    id: int
    item_name: str
    quantity: int
    created_at: dt.datetime
    delivered_at: dt.datetime | None = None

    @field_validator("quantity")
    def validate_quantity(cls, value: int) -> int:
        if value < 1:
            raise ValueError("Quantity must be greater than 0")
        return value

    @field_validator("created_at")
    def validate_created_at(cls, value: dt.datetime) -> dt.datetime:
        if value > dt.datetime.now():
            raise ValueError("Created at must be in the past")
        return value


if __name__ == "__main__":
    o = Order(id=1,
              item_name="book",
              quantity=-1,
              created_at=dt.datetime.now())
    print(o)
    print(type(o.quantity))
