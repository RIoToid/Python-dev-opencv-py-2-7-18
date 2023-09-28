import cv2 as cv

capture = cv.VideoCapture(0) # 0 references from webcam; could provide the path of the video

# function to rescale the video -- !! only works with live video
def changeRes(width, height):
    capture.set(3, width) # 3 is to reference the width
    capture.set(4, height) # 4 is to reference the height

# changeRes(300,300)


# function to rescale the video -- !! works with image, video and live video
def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * 0.75)
    height = int(frame.shape[0] * 0.75)
    dimensions = (width, height) # tuple

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = capture.read() # read the video frame by frame and returns if the frame was successfully read and the frame itself
    cv.imshow("Video", frame)
    #cv.imshow("Video Resized", rescale(frame))
    

    if cv.waitKey(20) & 0xFF==ord("d"): # stop the video from playing infinitely -- press d key to exit
        break

capture.release() # release the pointer
capture.destroyAllWindows()

cv.waitKey(0)