#!/usr/bin/python3


import urllib3,os
from PIL import Image
from io import BytesIO
from datetime import datetime 
from transformers import pipeline

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
    imageFilename = 'google-out.png'
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    newImageFilename = 'google-out-' + timestamp + '.png'
    if os.path.exists(imageFilename):
        print(f'文件已经存在，已保存为:{newImageFilename}')
        image.save(newImageFilename,'png')
    image.save(imageFilename,'png')
    image.close()
else:
    print(f"无法获取图像，状态码: {response.status}")
    
# 加载模型
checkpoint = "google/owlvit-base-patch32"   
detector = pipeline(module=checkpoint, task="zero-shot-object-detection")
print(image)