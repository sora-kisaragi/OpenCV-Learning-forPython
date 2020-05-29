# https://qrunch.net/@Atom/entries/Q9fV8JEIQJVCDVId?ref=qrunch
# このソースコードがwindows10の環境で動作するかどうかの確認
import cv2
import os
import numpy as np
from PIL import Image

# 学習画像データ枚数取得変数初期化
sample_cnt = 0


# VideoCapture用インスタンス生成
cap_Inst = cv2.VideoCapture(0)

# 画像サイズをVGAサイズに変更
# 自作する場合ここに手を加えると高速化や信頼性を左右させられるかもしれない
cap_Inst.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap_Inst.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# 顔検出を認識する
# カスケード検出器はこちらから  <https://github.com/opencv/opencv/tree/master/data/haarcascades>
face_detector = cv2.CascadeClassifier(
    'D:\\User\Documents\GitHub\OpenCV\data\haarcascades\haarcascade_frontalface_alt2.xml')


# 学習画像用データから顔認証データymlファイル差s区政するメソッド
# このファイルを顔認証データのモデルファイルとして使用する


def image_learning_make_Labels():

    # リスト保存用変数
    face_list = []
    ids_list = []

    # 学習画像データ保存領域パス情報
    # path = '/image_data'
    path = 'D:\\User\Documents\GitHub\Python\OpenCV Learning\image_data'
    recognizer = cv2.face_LBPHFaceRecognizer.create()

    # 学習画像ファイルパスをすべて取得
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # 学習画像ファイル分 ループ
    for imagePath in imagePaths:

        # グレースケールに変換
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        # UserIDが入っているファイル名からUserID番号として取得
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        # 物体認識の実行
        faces = face_detector.detectMultiScale(img_numpy)

        # 認識した顔認識情報を取得
        for (x, y, w, h) in faces:
            face_list.append(img_numpy[y:y+h, x:x+w])
            ids_list.append(id)

    print("\n Training Start ...")
    # 学習スタート
    recognizer.train(face_list, np.array(ids_list))

    # 学習した結果をymlファイルに保存する
    recognizer.save('trainer/trainer.yml')

    # 学習した顔種類を標準出力
    print("\n User {0} trained. Program end".format(len(np.unique(ids_list))))


# 顔認証したい人物の通し番号を入力させる
User_id = input('\n User Id Input <ex:001> >>> ')
print("\n Face capture Wait ..........")

# 学習用データ取得と保存
while(True):

    # カメラで顔データを取得する
    ret, img = cap_Inst.read()
    # 画像でグレースケールに変換する
    image_pil = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # NumPyの配列に格納
    gray = np.array(image_pil, 'uint8')
    # Hear-like特徴分類器で顔を検知
    faces = face_detector.detectMultiScale(gray)
    # 学習用データを作成
    for (x, y, w, h) in faces:

        # 顔部分を切り取り
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        sample_cnt += 1

        # 画像ファイル名にUSERIDを付与して保存
        cv2.imwrite("image_data/User." + str(User_id) + '.' +
                    str(sample_cnt) + ".jpg", image_pil[y:y+h, x:x+w])

        # 画像データを画面表示
        cv2.imshow('image', img)

    # 認証学習画像を10枚
    if sample_cnt >= 10:
        break

print("\n Face capture End")
# 学習ファイルを作成
image_learning_make_Labels()

# カメラ開放
cap_Inst.release()
cv2.destroyAllWindows()
