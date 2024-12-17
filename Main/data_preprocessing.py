import numpy as np
from PIL import Image
import os
"""
This module is for academic festival in Kyunghee High School.
"""
def preprocess_images(image_folder, target_size=(850, 850), start_i = 0, end_i = 10):
    image_files = os.listdir(image_folder)
    images = []

    for image_file in image_files[start_i:end_i]:
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


"""def split_images(image_files, p=15, r=48):
    splited_images = []

    for repeats in range(r):
        print(f'{repeats+1}p를 생성합니다.')
        # rp 배열에 p단위수로 끊어서 넣기
        rp = image_files[:p]
        print(rp.shape[:], '---> 이야...')
        # 기존 배열에서 앞부분은 삭제하면서 당기기
        image_files = image_files[p:]
        print('남은 놈!:', image_files.shape[:])
        splited_images.append(rp)   # 큰 배열에 삽입하기
        if len(image_files) < 15:
            break

    return splited_images"""

def split_images(image_files, p=15, input_length=14):
    input_images = []
    output_images = []
    r = len(image_files)//p if(len(image_files)%p==0) else len(image_files)//p + 1
    for repeats in range(r):
        # rp 배열에 p단위수로 끊어서 넣기
        i_rp = image_files[:p][:input_length]
        o_rp = image_files[:p][input_length:]
        # 기존 배열에서 앞부분은 삭제하면서 당기기
        image_files = image_files[p:]
        # 배열에 삽입 해버렷
        input_images.append(i_rp)
        output_images.append(o_rp)
        # 버렷!
        if len(image_files) < p:
            break
    # 넘파이 배열로 전환 후 내보내기
    return np.array(input_images), np.array(output_images)