import glob
import os
from pathlib import Path
import shutil

path = '/home/ljj/data/iwest/서부발전/Result/out_0'
path2 = '/home/ljj/data/iwest/서부발전/Result/backup_0'
os.makedirs(path2, exist_ok=True)

images = glob.glob(path+'/*')

for image in images:
    if int(os.path.basename(image)[-5]) !=0: 
        shutil.move(image, os.path.join(path2, os.path.basename(image)))