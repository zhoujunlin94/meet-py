from fastapi import APIRouter
from log.logger import getLogger
from error.exception import MeetException

router = APIRouter()
logger = getLogger(__name__)

@router.get("/{type}")
def get_items(type: int):
    match type:
        case 0:
            return 1/0
        case 1:
            raise MeetException.SystemError()
        case 2:
            return "success"
