#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
cv2.namedWindow("preview")
#opening live stream on camera
vc = cv2.VideoCapture(0)
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(1)
    if key == 27: 
        #Take a picture on ESC
        cv2.imwrite("test.png", frame) 
        # exit after that
        break 
    else:
        #creating rectangle on the camera
        cv2.rectangle(frame, (80,75), (1165,630), (212,130,171), thickness=5, lineType=8)
        
vc.release()
cv2.destroyWindow("preview")   


# In[28]:


#get input from user
height= int(input ("Enter approximated height in meters: "))
width= int(input ("Enter approximated width in meters: "))


# In[29]:


#show image taken from camera
import matplotlib.image as im
import matplotlib.pyplot as plt
wall= im.imread("test.png")
plt.imshow(wall)
plt.show()


# In[30]:


#find the wall shape
wall.shape


# In[31]:


#load bed image
bed= im.imread("/projectFurniture/bed.png")
plt.imshow(bed)
plt.show()


# In[32]:


#check image shape
bed.shape


# In[33]:


from PIL import Image
import cv2
background = Image.open('test.png')
img = cv2.imread("test.png")
#check the difference between cv2.shape and PIL.size
img.shape


# In[34]:


background.size


# In[41]:


#function to get the horizontal and vertical ratio of the background (wall)
def ratio (background_w, background_h, background):
    vertical_ratio= background.size[1] // background_h
    horizontal_ratio= background.size[0] // background_w
    
    return vertical_ratio, horizontal_ratio


# In[42]:


import cv2
from PIL import Image
def beds(background_w, background_h, background,bed_height = 2,bed_width = 1.5):
    #find the vertical and horizontal ratio of background
    vertical_ratio, horizontal_ratio= ratio(background_w, background_h, background)
    
    #open bed image with cv2
    bed= cv2.imread("/projectFurniture/bed.png", 
                    cv2.IMREAD_UNCHANGED)
    
    #get the new sizes basid on background ratio
    bed_width= int ( bed_width* horizontal_ratio)
    bed_height= int (bed_height* vertical_ratio)
    #print(bed_width,',',bed_height)
    
    #resize the image and save it
    bed= cv2.resize(bed, (bed_width, bed_height), interpolation = cv2.INTER_AREA)
    cv2.imwrite("resized_bed.png", bed)
    
    #open the resized image with PIL
    bed2=Image.open("/resized_bed.png")
    #print(bed2.size)
    
    #shift distance
    h_distance=4
    #bed location
    horizontal= int(h_distance* horizontal_ratio)
    vertical= int(background.size[1]-bed_height)
    bed_shift=(horizontal, vertical)
    
    #combine two background with resized image
    background.paste(bed2,bed_shift, bed2)
    background.save("Designed.png")


# In[43]:


import cv2
from PIL import Image
def drawers(background_w, background_h, background,drawer_height = 1.4,drawer_width = 1):
    #find the ratio of background
    vertical_ratio, horizontal_ratio= ratio(background_w, background_h, background)
    
    #open bed image with cv2
    drawer= cv2.imread("/projectFurniture/drawers.png", 
                    cv2.IMREAD_UNCHANGED)
    
    #get the new sizes basid on background ratio
    drawer_width= int ( drawer_width* horizontal_ratio)
    drawer_height= int (drawer_height* vertical_ratio)
    
    #resize the image and save it
    drawer= cv2.resize(drawer, (drawer_width, drawer_height), 
                       interpolation = cv2.INTER_AREA)
    cv2.imwrite("resized_drawer.png", drawer)
    
    #open the resized image with PIL
    drawer2=Image.open("/resized_drawer.png")
    
    #shift distance
    h_distance= 1.7
    #bed location
    horizontal= int(h_distance* horizontal_ratio)
    vertical= int(background.size[1]-drawer_height)
    drawer_shift=(horizontal, vertical)
    
    #combine two background with resized image
    background.paste(drawer2,drawer_shift, drawer2)
    background.save("Designed.png")


# In[44]:


import cv2
from PIL import Image
def mirrors(background_w, background_h, background, mirror_height=1.2, mirror_width=0.7):
    #find the ratio of background
    vertical_ratio, horizontal_ratio= ratio(background_w, background_h, background)
    
    #open bed image with cv2
    mirror= cv2.imread("/projectFurniture/mirror.png", 
                    cv2.IMREAD_UNCHANGED)
    
    #get the new sizes basid on background ratio
    mirror_width= int ( mirror_width* horizontal_ratio)
    mirror_height= int (mirror_height* vertical_ratio)
    
    #resize the image and save it
    mirror= cv2.resize(mirror, (mirror_width, mirror_height), 
                       interpolation = cv2.INTER_AREA)
    cv2.imwrite("resized_mirror.png", mirror)
    
    #open the resized image with PIL
    mirror2=Image.open("/resized_mirror.png")
    
    h_distance, v_distance= 1,1.5
    #bed location
    horizontal= int(h_distance* horizontal_ratio)
    vertical= int(v_distance* vertical_ratio)
    mirror_shift=(horizontal, vertical)
    
    #combine two background with resized image
    background.paste(mirror2,mirror_shift, mirror2)
    background.save("Designed.png")
    


# In[45]:


import cv2
from PIL import Image
def tables(background_w, background_h, background, table_height=0.66, table_width=0.54):
    #find the ratio of background
    vertical_ratio, horizontal_ratio= ratio(background_w, background_h, background)
    
    #open bed image with cv2
    table= cv2.imread("/projectFurniture/bedside table.png", 
                    cv2.IMREAD_UNCHANGED)
    
    #get the new sizes basid on background ratio
    table_width= int ( table_width* horizontal_ratio)
    table_height= int (table_height* vertical_ratio)
    
    #resize the image and save it
    table= cv2.resize(table, (table_width, table_height), 
                       interpolation = cv2.INTER_AREA)
    cv2.imwrite("resized_table.png", table)
    
    #open the resized image with PIL
    table2=Image.open("/resized_table.png")
    
    h_distance= 1
    #bed location
    horizontal= int(h_distance* horizontal_ratio)
    vertical= int(background.size[1]-table_height)
    table_shift=(horizontal, vertical)
    
    #combine two background with resized image
    background.paste(table2,table_shift, table2)
    background.save("Designed.png")


# In[46]:


import cv2
from PIL import Image
def benchs(background_w, background_h, background, bench_height= 0.6, bench_width= 1.1):
    #find the ratio of background
    vertical_ratio, horizontal_ratio= ratio(background_w, background_h, background)
    
    #open bed image with cv2
    bench= cv2.imread("/projectFurniture/bench.png", 
                    cv2.IMREAD_UNCHANGED)
    
    #get the new sizes basid on background ratio
    bench_width= int (bench_width* horizontal_ratio)
    bench_height= int (bench_height* vertical_ratio)
    
    #resize the image and save it
    bench= cv2.resize(bench, (bench_width, bench_height), 
                       interpolation = cv2.INTER_AREA)
    cv2.imwrite("resized_bench.png", bench)
    
    #open the resized image with PIL
    bench2=Image.open("/resized_bench.png")
    
    h_distance= 2.7
    #bed location
    horizontal= int(h_distance* horizontal_ratio)
    vertical= int(background.size[1]-bench_height)
    bench_shift=(horizontal, vertical)
    
    #combine two background with resized image
    background.paste(bench2,bench_shift, bench2)
    background.save("Designed.png")


# In[40]:


beds(width, height, background)
drawers(width, height, background)
mirrors(width, height, background)
tables(width, height, background)
benchs(width, height, background)


# In[ ]:




