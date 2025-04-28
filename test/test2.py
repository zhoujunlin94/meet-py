import threading

# 创建一个线程本地存储对象
thread_local = threading.local()

def worker():
    # 获取当前线程的变量
    if not hasattr(thread_local, 'value'):
        thread_local.value = 0
    thread_local.value += 1
    print(f"Thread {threading.current_thread().name}: value = {thread_local.value}")

# 创建多个线程
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()