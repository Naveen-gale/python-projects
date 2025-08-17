import cv2

x = cv2.QRCodeDetector()

val,points,straight_qrcode = x.detectAndDecode(cv2.imread('naveenweb.png'))
print(val)