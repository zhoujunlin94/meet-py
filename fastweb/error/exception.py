# 自定义异常类
class MeetException(Exception):
    def __init__(self, code: int, detail: str):
        self.code = code
        self.detail = detail

    @staticmethod
    def SystemError():
        return MeetException(500, '系统异常,请稍后再试')