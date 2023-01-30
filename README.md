# Find-Face-Module
**Computer vision project** that enables when you run it and put someone's face in front of the camera <br>
* Draw a rectangle on anybody's face.
* Draw Face Mesh.
* Can access  Face's Landmark by its IDs.

This module uses libraries Mediapipe and OpenCV.


# Steps
1. install Library required 
```
pip install opencv-python
```
```
pip install mediapipe
```

2. import Class from the MODULE `from findfaceMODULE import faceDetection as fd`

3. Make an Object               `detector = fd()`

5. put img in specific function `detector.faceMesh(img, draw=True)`




