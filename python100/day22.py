import json
import requests

my_dict = {
    'name': 'zhoujunlin',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

# dumps:将Python对象处理成JSON格式的字符串 
# print(json.dumps(my_dict)) # 中文字符都是用Unicode编码显示

# dump:将Python对象按照JSON格式序列化到文件中
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(my_dict, file)

# load将文件中的JSON数据反序列化成对象
# with open('data.json', 'r', encoding='utf-8') as file:
#     dict = json.load(file)
#     print(type(dict))
#     print(dict)

# loads将字符串反序列成对象
# str_data = '{"name": "zhoujunlin", "age": 40, "friends": ["王大锤", "白元芳"], "cars": [{"brand": "BMW", "max_speed": 240}, {"brand": "Audi", "max_speed": 280}, {"brand": "Benz", "max_speed": 280}]}'
# dict = json.loads(str_data)
# print(type(dict))
# print(dict)

resp = requests.post(url="https://apis.tianapi.com/enmaxim/index", data={
    "key": "c7fae6dac740ba3b1401cb4543ec1e10"
    })
if resp.status_code == 200:
    ret = resp.json()
    print(ret['result']['zh'])
    print(ret['result']['en'])