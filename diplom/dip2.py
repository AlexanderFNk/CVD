#разбивка на изображен и классы
#классы возмем от минимума 3,5М это 2021_05_24_11_17_41
#обозначим классы с шагом 1/4 это (3.5;3.75;4;4.25;4.5;4.75;5;5.25;5.5;
#список файлов
import os
from datetime import datetime
pathfile1 = 'f://dip//imgcorrect'
arr = os.listdir(pathfile1)
myclass=[['2021_05_20_23_32_51','2021_05_21_04_13_51'], #5.5
       ['2021_05_21_09_33_52','2021_05_21_14_11_53'], #5.25
       ['2021_05_21_14_13_53','2021_05_21_15_51_54'], #5
       ['2021_05_21_15_53_54','2021_05_22_00_54_13'], #4.75
       ['2021_05_22_00_56_13','2021_05_22_04_24_14'], #4.5
       ['2021_05_22_04_26_14','2021_05_22_16_16_16'], #4.25
       ['2021_05_22_16_18_16','2021_05_23_01_50_19'], #4
       ['2021_05_24_12_25_41','2021_05_24_18_03_43'], #3.75]
       ['2021_05_23_22_39_38','2021_05_24_12_23_41']] #3.5
infoclass=[]

for file in arr:
       if file.endswith(".png"):
              dt=file.split(".")[0]
              date_time_fl = datetime.strptime(dt, '%Y_%m_%d_%H_%M_%S')
              for indx, cl in enumerate(myclass):
                     date_time_from = datetime.strptime(cl[0], '%Y_%m_%d_%H_%M_%S')
                     date_time_to = datetime.strptime(cl[1], '%Y_%m_%d_%H_%M_%S')
                     if date_time_fl>=date_time_from and date_time_fl<=date_time_to:
                            infoclass.append([pathfile1+'//'+file, indx])

#для теста отделим 10%
train=[]
test=[]
for i in range(9):
       a=[]
       for fileclass in infoclass:
              if (fileclass[1]==i):
                     a.append(fileclass)
       count = len(a)
       count1=count-count//10
       train=train+a[:count1]
       test=test+a[count1:count]


print(len(train))
print(len(test))

import shutil
#создадим image folder
pathfile2 = 'f://dip//imagclass/train'
for fileclass in train:
       dir=pathfile2+'//'+str(fileclass[1])
       if not os.path.exists(dir):
              os.makedirs(dir)
       shutil.copy2(fileclass[0], dir+"//"+ os.path.basename(fileclass[0]))
pathfile2 = 'f://dip//imagclass/test'
for fileclass in test:
       dir=pathfile2+'//'+str(fileclass[1])
       if not os.path.exists(dir):
              os.makedirs(dir)
       shutil.copy2(fileclass[0], dir+"//"+ os.path.basename(fileclass[0]))

