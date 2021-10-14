import cv2 as cv

def rescale_Image(image, scale=0.3):
    scale_given=scale
    height=int(image.shape[0]*scale)
    width=int(image.shape[1]*scale)
    dimensions=(width,height)
    return cv.resize(image,dimensions,interpolation=cv.INTER_AREA),scale_given