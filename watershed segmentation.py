# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:04:41 2021

@author: AKSHANSH MISHRA
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/az31a.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

cv2.imwrite("F:/Opening image.png",opening)


############## IDENTIFYING THE PIXELS CORRESPONDING TO BACKGROUND ############


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/az31a.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

sure_bg=cv2.dilate(opening,kernel,iterations=2)

cv2.imwrite("F:/Sure Background.png",sure_bg)


############### DISTANCE TRANSFORMATION #######################

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/az31a.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

sure_bg=cv2.dilate(opening,kernel,iterations=2)

dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_bg=cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)

cv2.imwrite("F:/Distance Transform.png",dist_transform)


########################Sure FG ##############################

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/az31a.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

sure_bg=cv2.dilate(opening,kernel,iterations=2)

dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_fg=cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)

cv2.imwrite("F:/Sure FG.png",sure_fg)

#################### UNKNOWN PIXELS #######################


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/az31a.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

sure_bg=cv2.dilate(opening,kernel,iterations=2)

dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_fg=cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)
sure_fg=np.uint8(sure_fg)

unknown=cv2.subtract(sure_bg, sure_fg)

cv2.imwrite("F:/Unknown Pixels.png",unknown)

################# WATER SHED ########################


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/617 alloy.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

sure_bg=cv2.dilate(opening,kernel,iterations=2)

dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_fg=cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)
sure_fg=np.uint8(sure_fg)

unknown=cv2.subtract(sure_bg, sure_fg)

ret3,markers=cv2.connectedComponents(sure_fg)
markers=markers+10

markers[unknown==255]=0

plt.imshow(markers)
plt.imshow(markers,cmap="jet")



cv2.imwrite("F:/Unknown Pixels.png",unknown)

################# COLOR MICROSTRUCTURE #######################

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
img1=cv2.imread("F:/Grain Size Distribution Project/617 alloy.png")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

pixels_to_um=0.5

ret,thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)

opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

sure_bg=cv2.dilate(opening,kernel,iterations=2)

dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_fg=cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)
sure_fg=np.uint8(sure_fg)

unknown=cv2.subtract(sure_bg, sure_fg)

ret3,markers=cv2.connectedComponents(sure_fg)
markers=markers+10

markers[unknown==255]=0

img1[markers==-1]=[0,255,255]
img2=color.label2rgb(markers,bg_label=0)

cv2.imwrite("F:/Overlay Original Image.png",img1)
cv2.imwrite("F:/Coloured Grains.png",img2)

################# Geometrical Features ####################

clusters=measure.regionprops(markers,intensity_image=img)

propList = ['Area',
            'equivalent_diameter', #Added... verify if it works
            'orientation', #Added, verify if it works. Angle btwn x-axis and major axis.
            'MajorAxisLength',
            'MinorAxisLength',
            'Perimeter',
            'MinIntensity',
            'MeanIntensity',
            'MaxIntensity']  

output_file = open('image1_measurements.csv', 'w')
output_file.write(',' + ",".join(propList) + '\n') #join strings in array by commas, leave first cell blank
#First cell blank to leave room for header (column names)

for cluster_props in clusters:
    #output cluster properties to the excel file
    output_file.write(str(cluster_props['Label']))
    for i,prop in enumerate(propList):
        if(prop == 'Area'): 
            to_print = cluster_props[prop]*pixels_to_um**2   #Convert pixel square to um square
        elif(prop == 'orientation'): 
            to_print = cluster_props[prop]*57.2958  #Convert to degrees from radians
        elif(prop.find('Intensity') < 0):          # Any prop without Intensity in its name
            to_print = cluster_props[prop]*pixels_to_um
        else: 
            to_print = cluster_props[prop]     #Reamining props, basically the ones with Intensity in its name
        output_file.write(',' + str(to_print))
    output_file.write('\n')
output_file.close()   
 





