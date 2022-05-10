import cv2 as cv
import time as t
from findfaceMODULE import faceDetection as fd         #to gat my class from findfaceMODULE module

def dis(a,b):                                          # to calculate distance bet 2 points
    return int(((a[1]-b[1])**2 + (a[2]-b[2])**2)**.5)

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    cap.set(3,800)
    cap.set(4,650)

    ptime = 0

    detector = fd()                                     #make an object to use its functions

    while 1:
        suc,img = cap.read()
        img = cv.flip(img,1)
        lms = detector.faceMesh(img,draw=1,landmarks=1) # to "draw" face landandmarks make draw = True
                                                        # to get face landandmarks make landmarks = True
                                                        # each landmark have [id,x,y]

        # if lms: # "this condition is must if you want to uselnadmarks"
        #         # becouse it is propaply to open program without anyone front of camera

            # # can help you to know if user "sleep" and take a pic in this condition or anything
            # # for example
            # for i in [[159,144],[385,374]]:
            #     d = dis(lms[i[0]], lms[i[1]])
            #     if d < 9:
            #         cv.putText(img,"warining, wkae up",(10,150),cv.FONT_HERSHEY_DUPLEX,1,(0,0,255),1)
            #
            # # can help you to know if user "bytaweb" and take a pic in this condition or anything
            # # for example
            # d1314 = dis(lms[13],lms[14])
            # if d1314 > 15:
            #     cv.putText(img,"warining, motawba",(10,100),cv.FONT_HERSHEY_DUPLEX,1, (0,0,255),1)


        ctime = t.time()                               # to know FPS to know the performans of your program
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv.putText(img,"FPS:" + str(int(fps)),(20,70),cv.FONT_HERSHEY_DUPLEX,2,(255,0,0),2)

        cv.imshow('0',img)
        if cv.waitKey(1) & 0xff == ord('q'):  #here to close ur prog when you click on "q"
            break