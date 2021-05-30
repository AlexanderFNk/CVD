import cv2
import urllib.request
import numpy as np
import os
import time
from datetime import datetime
import threading


def savefile():
	pathfile='f://dip'
	with  urllib.request.urlopen('http://uznt42.ru/FTP/Webcam/cam_1.jpg') as url:
		now = datetime.now()  # current date and time
		arr = np.asarray(bytearray(url.read()), dtype=np.uint8)
		img = cv2.imdecode(arr, -1)
		date_time = now.strftime("//%Y_%m_%d_%H_%M_%S")
		cv2.imwrite(pathfile+date_time+".png",img)
		print("date and time:", date_time)


def printit():
  threading.Timer(120.0, printit).start()
  savefile()

printit()


if cv2.waitKey() & 0xff == 27:
	quit()


