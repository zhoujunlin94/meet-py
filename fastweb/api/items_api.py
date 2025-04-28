from fastapi import APIRouter
from model.item_model import Item
from log.logger import getLogger

router = APIRouter()

logger = getLogger(__name__)

# 路由 - 获取所有 Items
@router.get("/")
def get_items():
    logger.info('mock items')
    return {"items": ["item1", "item2", "item3"]}

# 路由 - 创建 Item
@router.post("/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}
