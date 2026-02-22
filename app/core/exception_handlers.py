from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

def validation_exception_handler(request: Request, exc: RequestValidationError):

    errors = []

    for e in exc.errors():
        loc = e.get("loc", [])
        field = ".".join([str(x) for x in loc if x not in ("body", "query", "path")])
        msg = e.get("msg", "Valor inválido.")
        errors.append({"field": field or "unknown", "message": msg})

    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "code": 422,
            "message": "Erro de validação.",
            "errors": errors
        }
    )

def http_exception_handler(request: Request, exc: HTTPException):
    message = exc.detail if isinstance(exc.detail, str) else "Erro";

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "code": exc.status_code,
            "message": message,
            "errors": [] if isinstance(exc.detail, str) else exc.detail,
        }
    )




