import numpy as np  
import cv2
rad = 9
color = (0,255,0)
width = -5
point = (0,0)
clicked = False




canvas = np.ones([400,400,3],"uint8")*255


def click(event,x,y,flags,param):
    global canvas, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        point=(x,y)
        cv2.circle(canvas,point,rad,color,-1)
        clicked = True
    elif event == cv2.EVENT_MOUSEMOVE and clicked == True:
        point=(x,y)
        cv2.circle(canvas,point,rad,color,-1)
    elif event == cv2.EVENT_LBUTTONUP:
        clicked = False






cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)

while True:
    cv2.imshow("canvas",canvas)
    ch = cv2.waitKey(1)
    if ch & 0xFF==ord('q') or ch & 0xFF == ord('Q'):
        break
    elif ch & 0xFF == ord('b') :
        color = (255,0,0)
    elif ch & 0xFF == ord('r'):
        color = (0,0,255)
    


cv2.waitKey(0)
cv2.destroyAllWindows()
