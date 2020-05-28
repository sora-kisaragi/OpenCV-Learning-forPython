import cv2

img = cv2.imread("Photo/lean.png")
# ソーベルフィルタを適用
img2 = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=5)
# ファイルに保存
cv2.imwrite("Photo/lean-sobel.jpg", img2)
