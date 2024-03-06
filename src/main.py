from fastapi import FastAPI, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from router import router as router_deposit
from helpers import get_exception_text_from_request_validation_error


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    err_desc = await get_exception_text_from_request_validation_error(exc)
    return JSONResponse({'error': err_desc}, status_code=status.HTTP_400_BAD_REQUEST)


app.include_router(router_deposit)
