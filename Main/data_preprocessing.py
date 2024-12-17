import numpy as np
from PIL import Image
import os
"""
This module is for academic festival in Kyunghee High School.
"""
def preprocess_images(image_folder, target_size=(850, 850), num_images=10):
    image_files = os.listdir(image_folder)
    images = []

    for image_file in image_files[:num_images]:
        img_path = os.path.join(image_folder, image_file)
        with Image.open(img_path) as img:
            width, height = img.size
            
            # 이미지 왼쪽 상단을 원점으로 하고 상대적인 거리를 좌표처럼 여긴다.
            left = (width - target_size[0]) / 2
            top = (height - target_size[1]) / 2
            right = (width + target_size[0]) / 2
            bottom = (height + target_size[1]) / 2
            img_cropped = img.crop((left, top, right, bottom))
            img_resized = img_cropped.resize(target_size)
            img_array = np.array(img_resized) / 255.0
            images.append(img_array)

    images_tensor = np.array(images)
    return images_tensor


def split_images(image_folder, p=15, r=48):
    print("아잉 너무 어려워요~")
    image_files = os.path.join(image_folder)
    splited_images = []

    for repeats in range(r):
        print(f'{r+1}p를 생성합니다.')
        # rp 배열에 p단위수로 끊어서 넣기
        rp = image_files[:p]
        print(rp, '---> 이야...')
        # 기존 배열에서 앞부분은 삭제하면서 당기기
        image_files = image_files[p:]
        print('다음 놈!:', image_files[:p])
        splited_images.append(rp)   # 큰 배열에 삽입하기

    return splited_images