import cv2 as cv

image = cv.imread("C:\Users\ELHELOUJana\Pictures\Saved Pictures\cat.jfif")

cv.imshow("Cat", image) # display image, arg1 = name of window, arg 2 = the image itself

cv.waitKey(0) # waits an infinite amount of time to a key to be pressed