import cv2 as cv
import mediapipe as mp

class faceDetection():
    def __init__(self,mindetectionCon=.5):
        self.mpDraw = mp.solutions.drawing_utils
        self.minDetectionCOn = mindetectionCon

        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMech = self.mpFaceMesh.FaceMesh(max_num_faces=1)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1,circle_radius=1,color=(0,255,0))

        self.mpfaceDetect = mp.solutions.face_detection
        self.facesDect = self.mpfaceDetect.FaceDetection(self.minDetectionCOn)

    def faceMesh(self,img,draw=True,landmarks=False,headShotdraw=False,headshotpoint=False,headShotColor=(0,0,255)):
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        result = self.faceMech.process(imgRGB)
        facelmandMarks = []

        if result.multi_face_landmarks:
            for faceslms in result.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceslms,connections=self.mpFaceMesh.FACEMESH_CONTOURS,
                                               connection_drawing_spec=self.drawSpec,
                                               landmark_drawing_spec=self.drawSpec)

                if headShotdraw or headshotpoint:
                    for id,lms in enumerate(faceslms.landmark):
                        h,w,c = img.shape
                        cx,cy = int(lms.x * w),int(lms.y * h)
                        if headShotdraw:
                            if id == 9:
                                cv.circle(img,(cx,cy),5,headShotColor,cv.FILLED)
                        if headshotpoint:
                            return [cx,cy]

                if landmarks:
                    for id,lms in enumerate(faceslms.landmark):
                        h,w,c = img.shape
                        cx,cy = int(lms.x * w),int(lms.y * h)
                        facelmandMarks.append([id,cx,cy])  # id landmark in face and x,x loc
                    return facelmandMarks

    def findFaces(self,img,gbboxs=False,draw=True):

        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        results = self.facesDect.process(imgRGB)

        bboxs = []
        nbrOffaces = 0
        if results.detections:
            nbrOffaces = len(results.detections)
            cv.putText(img,"n faces:" + str(nbrOffaces),(20,120),cv.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)

            for id,face in enumerate(results.detections):
                # print( face.location_data.relative_bounding_box)
                # mpDraw.draw_detection(img, face)  to draw nromal squar araound face
                bboxC = face.location_data.relative_bounding_box
                ih,iw,ic = img.shape
                bbox = [int(bboxC.xmin * iw),int(bboxC.ymin * ih),
                        int(bboxC.width * iw),int(bboxC.height * ih)]

                if gbboxs and not draw:
                    bboxs.append([bbox,face.score[0]])
                    return bboxs

                if draw:
                    img = self.fancyDraw(img,bbox)
                    cv.putText(img,str(int(face.score[0] * 100)) + '%',(bbox[0],bbox[1] - 20),cv.FONT_HERSHEY_DUPLEX,.8,
                               (255,0,0),1)
        return img

    @staticmethod
    def fancyDraw(img,bbox,thick=6):
        x,y,w,h = bbox
        x1,y1 = x + w,h + y
        l = int(h / 4.7)
        cv.rectangle(img,bbox,(255,0,0),1)
        cv.line(img,(x,y),(x + l,y),(255,0,0),thick)
        cv.line(img,(x,y),(x,y + l),(255,0,0),thick)

        cv.line(img,(x1,y),(x1 - l,y),(255,0,0),thick)
        cv.line(img,(x1,y),(x1,y + l),(255,0,0),thick)

        cv.line(img,(x,y1),(x,y1 - l),(255,0,0),thick)
        cv.line(img,(x,y1),(x + l,y1),(255,0,0),thick)

        cv.line(img,(x1,y1),(x1 - l,y1),(255,0,0),thick)
        cv.line(img,(x1,y1),(x1,y1 - l),(255,0,0),thick)
        return img