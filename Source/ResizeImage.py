import cv2
import numpy as np


filename = "Photo/sorachan.png"
# 白黒画像で読み込み
img = cv2.imread(filename, 1)
# 画像の高さ幅を指定
width, height = 60, 60
# 画像をリサイズ
img = cv2.resize(img, (width, height))

cv2.imwrite("Photo/resize_sorachan.png", img)
