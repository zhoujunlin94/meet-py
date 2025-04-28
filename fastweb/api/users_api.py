from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.user_model import User
from log.logger import getLogger

logger = getLogger(__name__)
router = APIRouter()


@router.get("/hello")
def hello():
    return 'hello world'

@router.get("/hello2")
def hello2():
    return JSONResponse(content={"code": 0, "msg": "success", "data": "hello world2"})

# 路由 - 获取用户信息
@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "username": f"user_{user_id}"}

# 路由 - 创建用户
@router.post("/")
def create_user(user: User):
    return {"username": user.username, "email": user.email}
