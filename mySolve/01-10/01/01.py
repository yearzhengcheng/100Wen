import cv2

# cv2.imread()的系数是按BGR顺序排列的
img = cv2.imread('imori.jpg')
cv2.imshow("str0", img)
red = img[:, :, 2].copy()
blue = img[:, :, 0].copy()
img[:,:,0] = red
img[:,:,2] = blue
cv2.imshow('str', img)
cv2.waitKey(0)
cv2.destroyWindow('str')
cv2.destroyWindow('str0')
