import cv2
import numpy as np
import os
import time

# UserID変数
User_id = 0

# アルゴリズムのインスタンス
recognizer = cv2.face_LBPHFaceRecognizer.create()
# 学習したファイルを読み出し
recognizer.read('trainer/trainer.yml')
# 顔認証で使用するxmlをパラメータとして顔認識のインスタンス生成
cascadePath = 'D:\\User\Documents\GitHub\OpenCV\data\haarcascades\haarcascade_frontalface_alt2.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
# 顔認証で使用するxmlをパラメータとして目認識のインスタンス生成
eye_cascadePath = 'D:\\User\Documents\GitHub\OpenCV\data\haarcascades\haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascadePath)
# 学習した際のUserIDと人物の名前を変換するための配列(ここではUseID = 01まで UserIDを増やしたい場合はここを増やす)
names = ['Sora', 'Dear']

# VideoCapture用のインスタンス生成
cap = cv2.VideoCapture(0)

# 画像サイズをVGAサイズに変更する
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 最小Windowサイズの定義
minW = 0.1*cap.get(cv2.CAP_PROP_FRAME_WIDTH)
minH = 0.1*cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:

    # FPS算出用の時間取得
    tick = cv2.getTickCount()
    # カメラから画像データを取得
    ret, img = cap.read()
    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 顔検出
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(int(minW), int(minH)),
    )

    # 顔検出した人物認証のためのグループ
    for(x, y, w, h) in faces:

        # 顔の箇所を四角で描画
        cv2.rectangle(img, (x, y), (x+y, y+h), (0, 255, 0), 2)
        # 顔の上半分を検出対象とする
        eyes_gray = gray[y:y+int(h/2), x:x+w]
        # 目検出
        eyes = eye_cascade.detectMultiScale(
            eyes_gray,
            scaleFactor=1.11,
            minNeighbors=3,
            minSize=(8, 8)
        )

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh),
                          (255, 255, 255), 2)
        # 推論時間にかかる時間を知るために時間を取得
        t1 = time.time()
        # 学習した顔から推論をかける、戻値が認識した番号と信頼度
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        # 推論時間取得のため
        t2 = time.time()
        # 検出時間を算出
        dt1 = t2-t1

        # confidece(信頼度)を40%100%とする(信頼度を低めからしている)
        if confidence < 60 and confidence > 0:
            # USER IDから名前を取得
            id = names[id]
            confidence = "{0}%".format(round(100-confidence))
        else:
            id = 'unknown'
            confidence = "{0}%".format(round(100 - confidence))

        # 名前表示と,推論時間のテキスト文字を画像に貼り付け
        cv2.putText(img, "confidence: " + str(confidence),
                    (x+5, y+20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        cv2.putText(img, str(id)+' Time'+str(round(dt1, 3)) + 'sec',
                    (x+5, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

    # FPS算出と表示用のテキスト作成
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - tick)
    # FPSを左上に表示
    cv2.putText(img, " FPS:{} ".format(int(fps)), (10, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2, cv2.LINE_AA)

    # 画像表示
    cv2.imshow('camera', img)

    # ESCキーで終了
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

# Do a bit of cleanup
print("\n Exit Program")
cap.release()
cv2.destroyAllWindows()
