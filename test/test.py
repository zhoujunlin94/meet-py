import concurrent.futures
import time
from datetime import datetime
import random

def doSomething():
    time.sleep(random.randint(1, 10))
    print("end...")
    print(datetime.now())




with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    print(datetime.now())

    f1 = executor.submit(doSomething)
    f2 = executor.submit(doSomething)
    f3 = executor.submit(doSomething)
    
    f1.result()
    f2.result()
    f3.result()

    print(datetime.now())

