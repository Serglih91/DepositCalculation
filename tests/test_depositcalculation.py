from httpx import AsyncClient
from fastapi.exceptions import RequestValidationError

from src.helpers import get_exception_text_from_request_validation_error, get_format_date_after_delta_months
from src.service import DepositCalculator
from src.schemas import SDepositCalc


async def test_api_calculate_deposit(ac: AsyncClient):
    response = await ac.post("/deposit-calculation", json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    })
    assert response.status_code == 200
    response_data = response.json()
    assert type(response_data) == dict
    assert 'error' not in response_data.keys()
    for key, value in response_data.items():
        assert type(key) == str
        assert type(value) == float



async def test_api_calculate_deposit_validation_error(ac: AsyncClient):
    response = await ac.post("/deposit-calculation", json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 1,
        "rate": 6
    })
    assert response.status_code == 400
    response_data = response.json()
    assert type(response_data) == dict
    assert 'error' in response_data.keys()


async def test_get_exception_text_from_request_validation_error():
    # Описание ошибки из документации
    test_errors =[
            {
                "type": "greater_than_equal",
                "loc": [
                    "body",
                    "amount"
                ],
                "msg": "Input should be greater than or equal to 10000",
                "input": 10,
                "ctx": {
                    "ge": 10000
                },
                "url": "https://errors.pydantic.dev/2.6/v/greater_than_equal"
            }
        ]
    expected_message = "'amount' should be greater than or equal to 10000"
    err = RequestValidationError(errors=test_errors)
    res = await get_exception_text_from_request_validation_error(err)
    assert res == expected_message


async def test_calculate_deposit():
    data = {
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    }
    expected_res = {
        "31.01.2021": 10050.0,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75
    }
    s_data = SDepositCalc(**data)
    res = await DepositCalculator.calculate_deposit(s_data)
    assert type(res) == dict
    assert len(res) == data["periods"]
    assert res == expected_res


def test_get_format_date_after_delta_months():
    test_date = "31.01.2021"
    expected_date_after_1_month = "28.02.2021"
    expected_date_after_2_months = "31.03.2021"
    res_date_after_1_month = get_format_date_after_delta_months(test_date, 1)
    res_date_after_2_months = get_format_date_after_delta_months(test_date, 2)
    assert res_date_after_1_month == expected_date_after_1_month
    assert res_date_after_2_months == expected_date_after_2_months
