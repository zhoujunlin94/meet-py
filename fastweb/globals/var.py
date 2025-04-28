# globals.py
import contextvars

# 定义一个全局的 contextvar 来存储 request_id
var_request_id = contextvars.ContextVar('request_id', default=None)