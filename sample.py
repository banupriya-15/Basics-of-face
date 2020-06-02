import cv2

img=cv2.imread('lena.jpg',1)
cv2.imshow('lena',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('lena_copy.jpg',img)
img2=cv2.imread('lena_copy.jpg',1)
cv2.imshow('nanhd',img2)