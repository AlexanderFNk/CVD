import cv2
import numpy as np
import os


pathfile = 'f://dip'
pathfile1 = 'f://dip//imgcorrect'


def correctImg(name):
    img1=cv2.imread(pathfile+name)
    crop_img = img1[10:470, 0:720]    
    r = 150.0 / crop_img.shape[1]
    dim = (150, int(crop_img.shape[0] * r))
    aaa = cv2.resize(crop_img, dim, interpolation=cv2.INTER_AREA)
    return aaa

arr = os.listdir(pathfile)
if (not os.path.exists(pathfile1)):
   os.makedirs(pathfile1)

#получим сокращенные фото
for name in arr:
    if file.endswith(".png"):
        img=correctImg("//"+name)
        cv2.imwrite(pathfile1+"//" + name, img)