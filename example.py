import cv2 as cv
from findfaceMODULE import faceDetection as fd

cap = cv.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 700)
ptime = 0

detector = fd()
while 1:
    suc, img = cap.read()
    img = cv.flip(img, 1)

    detector.faceMesh(img, draw=True)

    cv.imshow("0", img)
    if cv.waitKey(1) & 0xff == ord('q'):  # here to close ur prog when you click on "q"
        break
