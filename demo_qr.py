import cv2
import numpy as np
from pyzbar.pyzbar import decode


def decoder(image):
    
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
        print("Barcode: " + barcodeData +" | Type: " + barcodeType)

# cap = cv2.VideoCapture(0)
# print(type(cap))

# while True:
if __name__ == "__main__":
    img = cv2.imread("E:\EKYC\lmao.png")
    frame = np.array(img)
    # print(type(frame))
    # print(frame)
    decoder(img)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(0)
    # if code == ord('q'):
    #     #break