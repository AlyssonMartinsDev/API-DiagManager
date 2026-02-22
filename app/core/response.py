from fastapi.responses import JSONResponse

# Padrao de resposta para quando obtiver SUCESSO
def success (message="Success", code=200, data=None):
    return JSONResponse(
        status_code=code,
        content={
            "status": "success",
            "code": code,
            "message": message,
            "data": data,
        },
    )

# Padrao de resposta para quando tiver um erro
def error(message="Error", code=400, errors=None):
    return JSONResponse(
        status_code=code,
        content={
            "status": "error",
            "code": code,
            "message": message,
            "errors": errors or [],
        },
    )