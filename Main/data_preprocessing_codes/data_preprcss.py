import numpy as np

"""
이 모듈은 모든 매개변수에 필수적으로 이미지 리스트를 포함합니다.
이미지 파일 경로는 매개변수로 허용하지 않습니다.
반드시 사전에 이미지를 리스트로 만드시고 매개변수로 넣으세요.
"""

# p는 시간당 이미지 개수, h는 1p에 들어갈 이미지 개수
def splitImgs_with_Nhours(image_list, h, p=12):
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
