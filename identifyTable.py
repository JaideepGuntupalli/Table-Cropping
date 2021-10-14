import cv2 as cv

#Defining a fn to identify table coordinates
def identify_table(img):
    #Inverse binary threshold to increase clarity of required pixels
    ret,thresh=cv.threshold(img.copy(), 200,255,cv.THRESH_BINARY_INV)

    #Finding Contours to get coordinates
    contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

    #Appending a list of whose contours are big enough to be a table
    coordinates_list=[]
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        if w>(img.shape[0])//2:
            coordinates_list.append((x,y,x+w,y+h))
    
    return coordinates_list