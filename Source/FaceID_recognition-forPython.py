import cv2
import numpy as np
import os
import time

# UserID変数
User_id = 0

# アルゴリズムのインスタンス
recognizer = cv2.face_LBPHFaceRecognizer.create()
# 学習したファイルを読み出し
recognizer.read('')
