import cv2


img = cv2.imread("Photo/lean.png")
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Photo/lean-gray.jpg", gry)
