from dbutils.pooled_db import PooledDB
import pymysql

pool = PooledDB(
    creator=pymysql,
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='test',
    charset='utf8mb4',
    maxconnections=10,  # 最大连接数
    blocking=True,      # 无空闲连接时阻塞等待
    cursorclass=pymysql.cursors.DictCursor
)

# pymysql.connect()