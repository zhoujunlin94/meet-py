启动服务：uvicorn main:app --reload

指定配置文件启动服务：
$env:ENV_FILE=".env.test"
uvicorn main:app --reload
