import numpy as np
from PIL import Image
import os
"""
This function is for academic festival in Kyunghee High School.
"""
def preprocess_images(image_folder, target_size=(850, 850)):
    image_files = os.listdir(image_folder)
    images = []

    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        with Image.open(img_path) as img:
            width, height = img.size
            
            # 이미지 왼쪽 상단을 원점으로 하고 상대적인 거리를 좌표처럼 여긴다.
            left = (width - target_size[0]) / 2
            top = (height - target_size[1]) / 2
            right = (width + target_size[0]) / 2
            bottom = (height + target_size[1]) / 2
            img_cropped = img.crop((left, top, right, bottom))
            img_cropped = img.resize(target_size)
            img_array = np.array(img_cropped) / 255.0
            images.append(img_array)

    images_tensor = np.array(images)
    return images_tensor