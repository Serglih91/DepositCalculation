from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class SDepositCalc(BaseModel):
    date: str
    periods: int = Field(ge=1, le=60)
    amount: int = Field(ge=10000, le=3000000)
    rate: float = Field(ge=1, le=8)

    @field_validator("date")
    def validate_date(cls, origin: object) -> object:
        temp = datetime.strptime(origin, "%d.%m.%Y").date()
        return origin
