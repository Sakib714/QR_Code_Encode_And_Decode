# from pyzbar.pyzbar import decode
# from PIL import Image
#
#
#
# img = Image.open('C:/Users/Public/Pictures/faltu_image.png')
#
# result = decode(img)
#
# print(result)
#
# # Could n't complete because of error

import cv2


detector = cv2.QRCodeDetector()

img = cv2.imread('text.png')

data, array,b = detector.detectAndDecode(img)

print(b)