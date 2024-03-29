import time
import ddddocr
import os
from PIL import Image


def Identify_Verification_Code(driver, location):
    # 1.把截屏放到screenshots文件夹中
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    storage_location = path + '\\' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.png'
    driver.save_screenshot(storage_location)

    # 2.找到验证码的位置坐标
    all_screenshot = driver.find_element(*location)
    left = all_screenshot.location['x']
    top = all_screenshot.location['y']
    right = all_screenshot.size['width'] + left
    below = all_screenshot.size['height'] + top

    # 3.利用PIL中的Image模块抠图
    image = Image.open(storage_location)
    Cutout_image = image.crop((left, top, right, below))
    Cutout_storage_location = path + '\\' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.png'
    Cutout_image.save(Cutout_storage_location)

    # 4.利用ddddorc模块进行识别
    orc = ddddocr.DdddOcr(show_ad=False)
    with open(Cutout_storage_location, 'rb') as f:  # 打开图片
        img_bytes = f.read()
    result = orc.classification(img_bytes)

    return result
