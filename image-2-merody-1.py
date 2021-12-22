# 이미지를 멜로디로 만들기

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import numpy
import time

# 이미지 읽기
file = './test-7.jpg'
img = cv2.imread(file)

# 이미지 크기
ws, hs, c = img.shape
print(ws, hs, c)

# 음계 리스트
eum = ['B1', 'C1', 'C1#', 'D1', 'D1#', 'E1', 'F1', 'F1#', 'G1', 'G1#', 'A1', 'A1#', 'B2', 'C2', 'C2#', 'D2']

# 음표 리스트
ttt = ['1', '1', '1', '1', '4', '4', '4', '4', '8', '8', '8', '8', '16', '16', '16', '16'] 

print(len(eum), len(ttt))

for w in range(0, ws):
    for h in range(0, hs):

# RGB 차이 구하기
        p = np.max(img[w, h, :]) - np.min(img[w, h, :]) 

# 16비트의 2진수 구하기
        b = format(p, 'b')
        b = b.zfill(8)
        
# 앞쪽 8비트를 정수로       
        A = int(b[0])*8 + int(b[1])*4 + int(b[2])*2 + int(b[3])*1

# 뒤쪽 8비트를 정수로
        B = int(b[4])*8 + int(b[5])*4 + int(b[6])*2 + int(b[7])*1

# 앞쪽 8비트를 음계로, 뒤쪽 8비트를 음표로
        print(eum[A], ttt[B])
        time.sleep(1)
