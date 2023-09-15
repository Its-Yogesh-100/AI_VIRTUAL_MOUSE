import cv2
import mediapipe
import os

#variables
width,height=1280,720
folderPath="images"


# camera setup

cap=cv2.VideoCapture(1)
cap.set(3,width)
cap.set(4,height)


# list of presentation images

pathImages=sorted(os.listdir(folderPath),key=len)
print(pathImages)

#variables

imgNumber=0


while True:
    # importing the presentation images

    success, img=cap.read()
    pathFullImage=os.path.join(folderPath.pathImages[imgNumber])
    imgCurrent=cv2.imread(pathFullImage)
    
    
    cv2.imshow("image",img)
    cv2.imshow("slides",imgCurrent)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break