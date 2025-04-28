from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse
import uuid
import time
from log.logger import getLogger
from globals.var import var_request_id
import json

exclue_path = ["/openapi.json"]

class BaseRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in exclue_path:
            return await call_next(request)
        logger = getLogger(__name__)

        requestId = request.headers.get('X-REQUEST-ID', str(uuid.uuid4()))
        var_request_id.set(requestId)
        logger.info(f"开始请求{request.method} {request.url}, client-ip: {request.client.host}")
        logger.info(f"请求头: {dict(request.headers)}")
        logger.info(f"请求参数: {dict(request.query_params)}")
        """ 记录请求 JSON，但不影响请求 """
        if request.method in ["POST", "PUT", "PATCH"]:  # 仅对需要请求体的方法生效
            request_body = await request.body()  # 读取原始 body
            if request_body:
                logger.info(f"请求JSON: {json.loads(request_body)}")

            async def new_receive():
                return {"type": "http.request", "body": request_body, "more_body": False}
            request._receive = new_receive

        try:
            startTime = time.time()
            response = await call_next(request)
            endTime = time.time()
            
            content_type = response.headers.get('Content-Type', '').lower()
            if 'application/json' in content_type and response.status_code in [200, 201, 202, 204]:
                response_body = b""
                async for chunk in response.body_iterator:
                    response_body += chunk

                response_dict = json.loads(response_body.decode('utf-8'))
                logger.info(f"响应: {response_dict}")
                ret = {'code': 0, 'msg': 'success', 'data': None}
                if type(response_dict) != dict or ('code' not in response_dict):
                    ret.update({'data': response_dict})
                else:
                    ret.update(response_dict)
                response = JSONResponse(content=ret, status_code=response.status_code)
            
            response.headers['X-REQUEST-ID'] = requestId
            response.headers['X-PROCESS-TIME'] = f"{(endTime-startTime)*1000:.2f}ms"
            logger.info(f"结束请求: {request.url},耗时:{(endTime-startTime)*1000:.2f}ms")
            return response
        except Exception as e:
            # exc_info=True 会将完整的异常堆栈信息添加到日志中，方便调试。
            logger.error(f"请求失败: {request.url}, 错误信息: {str(e)}", exc_info=True)
            raise e