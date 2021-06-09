from pyzbar.pyzbar import decode
import cv2
import numpy as np

def convert(qr_image):
    image = cv2.cvtColor(qr_image, cv2.COLOR_BGR2RGB)
    barcodes = decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),5)
        barcodeData = barcode.data.decode("utf-8")
        return barcodeData

# def convert(image):
    
#     #gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#     barcode = decode(image)

#     for obj in barcode:
#         points = obj.polygon
#         (x, y, w, h) = obj.rect
#         pts = np.array(points, np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(image, [pts], True, (0, 255, 0), 3)

#         barcodeData = obj.data.decode("utf-8")
#         barcodeType = obj.type
#         string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
        
#         cv2.putText(image, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
#         print("Barcode: " + barcodeData +" | Type: " + barcodeType)