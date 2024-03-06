from fastapi.exceptions import RequestValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Функция для получения описания ошибки из RequestValidationError
async def get_exception_text_from_request_validation_error(exc: RequestValidationError) -> str:
    err_desc_arr = []
    for el_err in exc.errors():
        el_err_desc = f"'{el_err['loc'][1]}'{el_err['msg'].replace('Input', '')}"
        err_desc_arr.append(el_err_desc)
    err_desc = ';'.join(err_desc_arr)
    return err_desc

def get_format_date_after_delta_months(current_date_str: str, delta_months: int) -> str:
    res_date = datetime.strptime(current_date_str, "%d.%m.%Y").date() + relativedelta(months=delta_months)
    res_date_str = datetime.strftime(res_date, "%d.%m.%Y")
    return res_date_str
