import glob
import os

raw_path = '/home/ljj/data/iwest/서부발전/Result/out_0'
dino_path = '/home/ljj/data/iwest/서부발전/Result/outputs0/raw'


raw_images = glob.glob(raw_path+'/*')
dino_images = glob.glob(dino_path+'/*')
print(len(raw_images))
print(len(dino_images))
num = 0
dino_paths = []
for dino in dino_images:
    dino_paths.append(os.path.basename(dino))
    
for img in raw_images:
    if os.path.basename(img)[:-4]+'.png' in dino_paths:
        os.remove(img)
    else:
        num+=1
        # print(img)
print(num)