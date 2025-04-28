from ds import pool

conn = pool.connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM t_user")
result = cursor.fetchall()
print(result)

# 归还连接到池（实际是关闭游标和连接）
cursor.close()
conn.close()  # 注意：此处不是真正关闭，而是归还到池