import cv2 as cv
from rescale import *
from identifyTable import *
from cropTable import *

def tableCropping():

    #Taking input from user about address of image
    img_address=input("Please Enter the address of the image : ")

    #Reading the image
    img_org = cv.imread(img_address)

    #Rescaling the image
    img_rescaled,scale=rescale_Image(img_org)

    #GrayScaling for better results
    img_gray=cv.cvtColor(img_rescaled,cv.COLOR_BGR2GRAY)

    #Finding coordinates of the tables in given image
    coordinates=identify_table(img_gray)

    #Appling for loop to show all tables
    for i in range(len(coordinates)):
        crop_table(i,coordinates,scale,img_org , i)

    cv.waitKey(0)



if __name__=="__main__":
  tableCropping()