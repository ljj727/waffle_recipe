import glob
import os
path = '/home/ljj/data/people/PeopleDataset_else_v1.0.0/images/40000'
images = glob.glob(path+'/*.jpg')

num = 0
a=0
for img_path in sorted(images):
    num+=1
    if num %4==0:
        pass
    else:
        a +=1
        os.remove(img_path)

print(a)

