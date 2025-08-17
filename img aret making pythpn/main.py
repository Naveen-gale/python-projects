import cv2
img = cv2.imread('boy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(invert, (21, 21), 0)    
inverted_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray, inverted_blur, scale=256.0)
cv2.imwrite('sketch.png', sketch)
cv2.imshow('Sketch', sketch)