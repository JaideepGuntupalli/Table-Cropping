import cv2 as cv

#Defing a fn to crop tables from given coordinates
def crop_table(index,lst,scale, img_org, i):
    index_lst=lst[index]
    table_no= i+1
    window_name='Table '+ str(table_no)#Custom names for every window
    #Cropping img # Added and subtracted 5 pixels for aesthetics
    #rescaling pixel values to crop from orginal image for better quality
    wid1=int((index_lst[1]//scale)-5)
    wid2=int((index_lst[3]//scale)+5)
    hgt1=int((index_lst[0]//scale)-5)
    hgt2=int((index_lst[2]//scale)+5)
    cropped_img=img_org[wid1:wid2,hgt1:hgt2]
    cv.imshow(window_name,cropped_img)