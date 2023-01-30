import cv2 as cv
import time as t
from findfaceMODULE import faceDetection as fd  # to gat my class from findfaceMODULE module


def dis(a, b):  # to calculate distance bet 2 points
    return int(((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** .5)


def makeTracking(lms, img):
    cv.line(img, (lms[54][1] - 20, lms[54][2] - 20), (lms[284][1] + 10, lms[284][2] - 20), (255, 0, 0), 2)

    cv.line(img, (lms[54][1] - 20, lms[54][2] - 20), (lms[176][1] - 60, lms[176][2]), (255, 0, 0), 2)

    cv.line(img, (lms[378][1] + 30 + 10, lms[378][2]), (lms[284][1] + 10, lms[284][2] - 20), (255, 0, 0), 2)

    cv.line(img, (lms[378][1] + 30 + 10, lms[378][2]), (lms[176][1] - 60, lms[176][2]), (255, 0, 0), 2)


if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    cap.set(3, 800)
    cap.set(4, 650)

    ptime = 0

    detector = fd()

    while 1:
        suc, img = cap.read()
        img = cv.flip(img, 1)
        lms = detector.faceMesh(img, draw=0, landmarks=1)
        if lms and len(lms) > 0:
            # for i in [54,284,176,378]:
            makeTracking(lms, img)

        ctime = t.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv.putText(img, "FPS:" + str(int(fps)), (20, 70), cv.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)

        cv.imshow('0', img)
        if cv.waitKey(1) & 0xff == ord('q'):  # here to close ur prog when you click on "q"
            break
