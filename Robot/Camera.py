from Robot import ser, cap
import numpy as np
import cv2

def move_camera(cX,cY,shape):
    
    if cX > (shape[1]/2)+25:
        if cX-(shape[1]/2) < 50:
            ser.write(str(5).encode("utf-8"))
        else:
            ser.write(str(1).encode("utf-8"))
            
    elif cX < (shape[1]/2)-25:
        if (shape[1]/2)-cX < 50:
            ser.write(str(6).encode("utf-8"))
        else:
            ser.write(str(2).encode("utf-8"))
        
    if cY > (shape[0]/2)+25:
        if cY-(shape[0]/2) < 50:
            ser.write(str(7).encode("utf-8"))
        else:
            ser.write(str(3).encode("utf-8"))
            
    elif cY < (shape[0]/2)-25:
        if (shape[0]/2)-cY < 50:
            ser.write(str(8).encode("utf-8"))
        else:
            ser.write(str(4).encode("utf-8"))


def find_centroid():
    _, frame = cap.read()
    frame = cv2.flip(frame, 0)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 40])     #low_blue=94,80,2         low_green=25,52,72
    high_red = np.array([179, 255, 255])   #high_blue=126,255,255    high_green=102,255,255
    mask = cv2.inRange(hsv_frame, low_red, high_red)

    _, thresh = cv2.threshold(mask,127,255,0)
    M = cv2.moments(thresh)
    if M["m00"] > 10000:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = int(frame.shape[1]/2), int(frame.shape[0]/2)
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)  #Upkey: 82, Rightkey: 83, Downkey: 84, Leftkey: 81
    if key == 27:
        return 0,0,0
    return cX, cY, frame.shape
   
    
    
    