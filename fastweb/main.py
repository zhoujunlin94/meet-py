from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.exceptions import HTTPException
from api import items_api, users_api, env_api, error
from middleware.BaseRequestMiddleware import BaseRequestMiddleware
from error.exception import MeetException

app = FastAPI()
# 注册中间件
app.add_middleware(BaseRequestMiddleware)

# 注册 API 路由
app.include_router(items_api.router, prefix="/items", tags=["items"])
app.include_router(users_api.router, prefix="/users", tags=["users"])
app.include_router(env_api.router, prefix="/configs", tags=["configs"])
app.include_router(error.router, prefix="/errors", tags=["errors"])

# 全局异常处理
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        content={
            "msg": f"An unexpected error occurred: {exc.detail}",
            "code": exc.status_code,
        }
    )


@app.exception_handler(MeetException)
async def meet_exception_handler(request, exc: MeetException):
    return JSONResponse(
        content={
            "msg": exc.detail,
            "code": exc.code,
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    return JSONResponse(
        content={
            "msg": f"An unexpected error occurred: {str(exc)}",
            "code": 500
        }
    )


@app.get("/")
def read_root():
    # 重定向到文档页面
    return RedirectResponse(url="/docs")
