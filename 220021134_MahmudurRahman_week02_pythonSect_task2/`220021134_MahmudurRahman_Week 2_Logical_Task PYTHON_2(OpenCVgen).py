import cv2 as cv
import numpy as np
kernel = np.ones((3*3), np.uint8) #kernel modifies the amount of pixels that would be 
#eroded or diluted. E.g. Use 5*5 for more drastic effect.
def contrast(img):
    # cv.convertScaleAbs(img_PATH, alpha, beta) where
    #alpha controls contrast and beta controls brightness
    #ref: https://docs.opencv.org/4.x/d3/dc1/tutorial_basic_linear_transform.html
    contrastedImg= cv.convertScaleAbs(img, 2, 1)
    cv.imwrite("FilteredImgs/Cat-contrast.jpg", contrastedImg)
    return contrastedImg
def grayscale(img):
    gsedImg= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("FilteredImgs/Cat-Grayscale.jpg", gsedImg)
    return gsedImg
def Inversion(img):
    inv= cv.bitwise_not(img)
    cv.imwrite("FilteredImgs/Cat-Inversion.jpg", inv)
    return inv
def erosion(img): 
    #makes darker areas bigger
    eroded= cv.erode(img, kernel, 1) #1 is the number of iterations, same for dilate func.
    cv.imwrite("FilteredImgs/Cat-erosion.jpg", eroded)
    return eroded
def dilution(img):
    dilated= cv.dilate(img, kernel, 1)
    cv.imwrite("FilteredImgs/Cat-Dilation.jpg", dilated)
    return dilated
def noise(img):
    row, col, channel= img.shape
    mean=0
    var= 0.1
    sigma= np.sqrt(var)
    #var mean sigma comes from gaussian noise formula.
    #ref video: https://www.youtube.com/watch?app=desktop&v=-Vk23ye2o_I
    noise_n= np.random.normal(mean, sigma, (row, col, channel))
    noisyImg= (img/255) + noise_n
    cv.imwrite("FilteredImgs/Cat-Noise.jpg", noisyImg)
    return noisyImg

#start of main func 
img= cv.imread("cat.jpg", cv.IMREAD_COLOR)
#cv.imshow("Normal Cat", img)
#cv.waitKey(0)
img_filtered= noise(img)
cv.imshow("filtered cat", img_filtered)
cv.waitKey(0)
