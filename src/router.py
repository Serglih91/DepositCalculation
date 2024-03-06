from fastapi import APIRouter, Body
from typing import Annotated


from schemas import SDepositCalc
from service import DepositCalculator



router = APIRouter(
    prefix="/deposit-calculation",
    tags=["Deposit"]
)


@router.post("")
async def calculate_deposit(data: Annotated[SDepositCalc, Body()]) -> dict[str, float]:
    res = await DepositCalculator.calculate_deposit(data)
    return res
