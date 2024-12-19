from PIL import Image
import numpy as np
import tensorflow as tf
import os
"""
이 모듈은 이미지 전처리에 관련된 모듈입니다.
이 모듈은 해당 프로젝트의 이미지 처리를 위한
함수를 순차적으로 담았습니다.
"""


def preprocess_images(image_folder, target_size=(850, 850), start_i = 0, end_i = 10):
    """
    이 함수는 이미지 경로와 이미지 리스트 인덱스 범위, 
    그리고 목표 사이즈(튜플)을 입력하면 사진을 원하는 크기로 
    절단하는 함수입니다.
    """
    img_file = os.listdir(image_folder)
    images = []

    for image in img_file[start_i:end_i]:
        img_path = os.path.join(image_folder, image)
        with Image.open(img_path) as img:
            width, height = img.size

            # 이미지 왼쪽 상단을 원점으로 하고 상대적인 거리를 좌표처럼 여긴다.
            left = (width - target_size[0]) / 2
            top = (height - target_size[1]) / 2
            right = (width + target_size[0]) / 2
            bottom = (height + target_size[1]) / 2
            # 상대적 거리 좌표에 따라 이미지 자르기
            img_cropped = img.crop((left, top, right, bottom))
            # 이미지 리사이징으로 크기 변형 방지
            img_resized = img_cropped.resize(target_size)
            img_array = np.array(img_resized) / 255.0   # 이미지 정규화
            # 해당 이미지를 새로운 이미지 리스트에 넣기
            images.append(img_array)

    return np.array(images)


def resize_images(dataset, target_size=(40, 40)):
    resized_dataset = tf.image.resize(dataset, target_size, method='bilinear')
    return resized_dataset


def splitImgs_with_Nhours(image_list, h, p=12):
    """
    이 함수는 이미지 리스트와 시간당 사진 개수,
    그리고 시간 블록 수를 받아서 1시간 간격으로
    찍힌 사진 리스트를 input data와 output data로
    나눠서 반환하는 함수입니다.
    """
    # p는 시간당 이미지 개수, h는 1p에 들어갈 이미지 개수

    input_imgs = []
    output_imgs = []
    r = len(image_list) // (h*p)


    # 가능한 덩어리 연산
    for i in range(r):
        # 1차 임시 리스트
        splited_by_r = np.reshape(image_list[:h*p], (p, h, 40, 40, 4))
        # 리스트 업데이트
        image_list = image_list[h*p:]
        temp = []
        

        # 이중 반복문으로 차례대로 리스트화해서 넣기 -> 매우 어려움
        for l in range(h):
            for j in range(p):
                temp.append(splited_by_r[j][l])
            input_imgs.append(temp[:p-1])
            output_imgs.append([temp[p-1]])


    return np.array(input_imgs), np.array(output_imgs)

def merge_40x40(start=22, end=30):
    merged_list = np.zeros((0,40,40,4))
    for i in range(start, end+1):
        file_str = str(i)
        file = np.load(f'../data/refined_data/trainData/2m/trainData_11{file_str}_40_2m.npy')
        merged_list = np.concatenate((merged_list, file), axis=0)
    print(merged_list.shape)

    return merged_list

def merge_40x40_(start=1, end=3):
    merged_list = np.zeros((0,40,40,4))
    for i in range(start, end+1):
        file_str = "0"+str(i) if i < 10 else str(i)
        file = np.load(f'../data/refined_data/trainData/2m/trainData_12{file_str}_40_2m.npy')
        merged_list = np.concatenate((merged_list, file), axis=0)
    print(merged_list.shape)

    return merged_list

def merge_40x40_1(start=16, end=21):
    merged_list = np.zeros((0,40,40,4))
    for i in range(start, end+1):
        file_str = str(i)
        file = np.load(f'../data/refined_data/testData/testData_11{file_str}_40_2m.npy')
        merged_list = np.concatenate((merged_list, file), axis=0)
    print(merged_list.shape)

    return merged_list
