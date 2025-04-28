import logging
from globals.var import var_request_id

def getLogger(logger_name='app_log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(request_id)s - %(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # file_handler = logging.FileHandler("app.log", encoding='utf-8')
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        # logger.addHandler(file_handler)

    if not logger.filters:
        logger.addFilter(RequestIdFilter())

    return logger

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        requestId = var_request_id.get()
        record.request_id = requestId if requestId else '-'
        return True