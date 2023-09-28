import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype="uint8") # 3 is for the colour dimensions

# paint
blank[0:100, 0:100] = 0,162,248

# draw a rectangle -- note: cv.FILLED = -1
cv.rectangle(blank, (10,0), (20, 500), (0,255,0), thickness=cv.FILLED) # arg 1= image to draw on, arg2 = starting pt, arg3 = finishing pt, arg 4 = color, arg5= thickness of the line
cv.imshow("Blank", blank)

# draw a circle
cv.circle(blank, (blank.shape[0]//2 ,blank.shape[1]//2), 40, (0,0,255), thickness=3) # arg1=image to draw on, arg2= center of circle coord, arg3=radius, thickness
cv.imshow("Circle", blank)

# draw a line
cv.line(blank, (0,0), (250,250), (255,0,0), thickness=8)
cv.imshow("Line", blank)

# draw text over an image
cv.putText(blank, "Hello Image", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Text over Image", blank)

cv.waitKey(0)
