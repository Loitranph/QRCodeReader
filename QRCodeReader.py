"""
--------------------------------------------------------------------------
-*- coding: utf-8 -*-                    created on friday, May, 10, 2024

@author: Phuoc Loi Tran
@student code: 2101076 (from C.T.U.T)
@github: Loitranph (https://github.com/Loitranph)
@discr|pt|on: Scan QR codes using computer vision
@using:
  software:
            python:
                    version: 3.10.7
                    lib: openCV

-----------------------------------------------------------------------------

"""

import cv2 as cv

qrcode = cv.QRCodeDetector()
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        ret_qr, decoded_info, points, _ = qrcode.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    cv.putText(frame, s, (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv.LINE_AA)
                    print(s)
                else:
                    pass
                frame = cv.polylines(frame, [p.astype(int)], True, (0, 255, 0), 8)
        cv.imshow("QR CODE", frame)
    else:
        pass
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
