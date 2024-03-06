from schemas import SDepositCalc
from helpers import get_format_date_after_delta_months


class DepositCalculator:
    @classmethod
    async def calculate_deposit(cls, data: SDepositCalc) -> dict[str, float]:
        result = {}
        current_sum = data.amount
        for i in range(data.periods):
            current_date = get_format_date_after_delta_months(data.date, i)
            current_sum = current_sum + current_sum*data.rate/100/12
            result[current_date] = round(current_sum, 2)
        return result
