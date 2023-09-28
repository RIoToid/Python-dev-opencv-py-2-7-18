import cv2 as cv

img = cv.imread("C:\Users\ELHELOUJana\Pictures\Saved Pictures\cat.jfif")
cv.imshow("Original", img)

# grayscale img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur img
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT) # kernel is usually odd and the higher values in kernel, the more blurry it is
cv.imshow("Blur", blur)

cv.waitKey(0)