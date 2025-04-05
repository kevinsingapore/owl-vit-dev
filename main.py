#!/usr/bin/python3

# from transformers import pipeline

# checkpoint = "google/owlvit-base-patch32"   
# detector = pipeline(module=checkpoint, task="zero-shot-object-detection")

import urllib3
from PIL import Image
from io import BytesIO

url = "https://unsplash.com/photos/oj0zeY2Ltk4/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MTR8fHBpY25pY3xlbnwwfHx8fDE2Nzc0OTE1NDk&force=true&w=640"

# 创建一个http连接池
http = urllib3.PoolManager()
# 发送请求并获取响应
response = http.request('GET', url, preload_content=False)

if response.status == 200:
    image_data = response.data
    image = Image.open(BytesIO(image_data))
    print('image:',image)
    
    # 展示图片进行确认
    image.show()
    image.close()
else:
    print(f"无法获取图像，状态码: {response.status}")