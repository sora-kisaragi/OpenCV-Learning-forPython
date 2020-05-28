import cv2


img = cv2.imread("lean.png")
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("lean-gray.jpg", gry)
