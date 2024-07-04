import cv2 as cv
import numpy as np
a=142
kernel = np.ones((3*3), np.uint8) 
def contrast(img):
    global a
    contrastedImg= cv.convertScaleAbs(img, 2, 7)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", contrastedImg)
    a=a+1
    return contrastedImg
def grayscale(img):
    global a
    gsedImg= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", gsedImg)
    a=a+1
    return gsedImg
def Inversion(img):
    global a
    inv= cv.bitwise_not(img)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", inv)
    a=a+1
    return inv
def erosion(img): 
    global a
    eroded= cv.erode(img, kernel, 1) #1 is the number of iterations, same for dilate func.
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", eroded)
    a=a+1
    return eroded
def dilution(img):
    global a
    dilated= cv.dilate(img, kernel, 1)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", dilated)
    a=a+1
    return dilated
def dark(img):
    global a
    darkenedImg = cv.convertScaleAbs(img, alpha=0.5, beta=0)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", darkenedImg)
    a=a+1
    return darkenedImg
def gaussian_blur(img):
    global a
    blurred_img = cv.GaussianBlur(img, (31, 31), 0)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", blurred_img)
    a=a+1
    return blurred_img

def median_blur(img):
    global a
    blurred_img = cv.medianBlur(img, 11)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", blurred_img)
    a=a+1
    return blurred_img
    
def bilateral_filter(img):
    global a
    filtered_img = cv.bilateralFilter(img, 30, 79, 79)
    cv.imwrite(f"E:\Bird species\TEST_n\DATA\{a}.jpg", filtered_img)
    a=a+1
    return filtered_img
#start of the main function
img= cv.imread(r"E:\Bird species\TEST_n\DATA\141.jpg", cv.IMREAD_COLOR)
contrast(img)
grayscale(img)
erosion(img)
dark(img)
dilution(img)
Inversion(img)
bilateral_filter(img)
median_blur(img)
gaussian_blur(img)


