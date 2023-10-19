import os
import shutil

def seq_split(split_num, image_path, output_path, mode):
    i = 0
    if mode == "random" :
        file_list = os.listdir(image_path)          # 랜덤으로 읽어옴
    else :
        file_list = sorted(os.listdir(image_path))  # 오름차순 정렬
    for img_file in file_list:
        img_path = os.path.join(image_path, img_file)
        if (i % split_num) == (split_num - 1):  # split_num의 배수번째 이미지를 이동
            shutil.copy(img_path, os.path.join(output_path, img_file))
        i = i + 1

if __name__ == "__main__" :
    raw_path = "/home/ljj/data/people/PeopleDataset_v2.0.1/images/0"
    images_path = os.listdir(raw_path)
    mode = "random"                        # Fix , seq or random
    output_path = "/home/ljj/data/people/PeopleDataset_v2.0.1/images/0_0"        # FIx
    if not os.path.exists(output_path) :
        os.makedirs(mode + "_" + output_path)
        new_output_path = mode + "_" + output_path
    split_num = 3
    for Img_folder in images_path :
        Img_path = raw_path + "/" + Img_folder
        seq_split(split_num, Img_path, new_output_path, mode)
