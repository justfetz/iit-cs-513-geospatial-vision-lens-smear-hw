
# coding: utf-8

# fetzer, jason, geo, hw_One


import numpy as np
import os
import sys
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import glob
import imutils
from imutils import contours


# In[71]:


'''print("Hello, Welcome to Image Smear Detection.")
fileLocation = input("Input the exact file path to your sequence of images.\n You do not need the final forward slash.\n This assumes all files are jpg's.\n If you are on Windows, some modification to source may be needed i.e. change slash direction in the code.")
'''

#fileLocation


# In[73]:

#CURRENT OPERATIONAL LINE OF CODE HAS MY LOCAL FOLDER.  PLEASE TYPE IN YOUR FOLDER PATH.

try:
    #images = [cv2.imread(file) for file in glob.glob("TYPE_YOUR_FILE_LOCATION_HERE/*.jpg")]
    images = [cv2.imread(file) for file in glob.glob("/Users/MYNAME/MYDESKTOP/PICTUREFOLDER/*.jpg")]
except IOError:
    print("Couldn't find jpg's in this folder.")
finally:
    print("Method Complete. You have read in your images.")


# In[74]:


amount = len(images)
print("There are " + str(amount) + " images read.")


# In[83]:


if amount > 0:
    print("Continuing...")
    print("Initial Shape = " + str(images[0].shape))
else:
    print("You may face some errors here in the near future! Check your folder path.")


# In[84]:


# resize all the images in the list
resizedImageList = [imutils.resize(image, width=500,height=500) for image in images]
print("Images have all been resized to " + str(resizedImageList[0].shape))


# In[85]:


blurList = []
for i in resizedImageList:
    i = cv2.GaussianBlur(i, (3,3), 0)
    blurList.append(i)



print("Applied Gaussian Blur to each file.")


# In[88]:


x=np.array(sum(blurList))


# In[89]:


#average of the images from passed in folder in resized Format

y = x/len(blurList)


# In[90]:


#Show default Average Image

cv2.imshow('First Average Image From Resized Set', y)
cv2.waitKey(0)
cv2.destroyWindow("First Average Image From Resized Set")


# In[98]:



#Distort Some Blur to give a basis
kernel2 = np.ones((5,5), np.float32)/100
distort2 = np.float32(cv2.filter2D(y,-1,kernel2))


# In[92]:

cv2.imshow('2D Trial Distorted', distort2)
cv2.waitKey(0)
cv2.destroyWindow("2D Trial Distorted")


# In[93]:


#reshade
y.shape
imAv = np.array(y,dtype=np.uint8)*10000



cv2.imshow('First Image from Gaussian Blur', blurList[0])
cv2.waitKey(0)
print("Press Enter To Continue")


# In[95]:



cv2.imshow('Amplified Average uint8', imAv)
cv2.waitKey(0)
print("Press Enter To Continue")


# In[96]:


newer = cv2.cvtColor(imAv, cv2.COLOR_RGB2GRAY)


# In[99]:


newer2 = cv2.cvtColor(distort2, cv2.COLOR_RGB2GRAY)


# In[100]:


pass


# In[ ]:


#GrayScale Differences


# In[101]:

#detailed grayscale
cv2.imshow('2D Filter GrayScale', newer)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[102]:


cv2.imshow('Amplified Average', newer2)
cv2.waitKey(0)




#same as above sequential, in plt form. 
plt.subplot(121),plt.imshow(newer),plt.title('Gray One')
plt.subplot(122),plt.imshow(newer2),plt.title('Gray Two')
plt.show()


# In[103]:


#2D Filter
kernel = np.ones((5,5), np.float32)/100
distort = np.float32(cv2.filter2D(newer,-1,kernel))


# In[105]:


plt.subplot(121),plt.imshow(blurList[0]),plt.title('Original')
plt.subplot(122),plt.imshow(distort),plt.title('Average of Blur Of Grayscale')
plt.show()


# In[107]:



gray = cv2.medianBlur(cv2.cvtColor(imAv, cv2.COLOR_RGB2GRAY), 5)
cannyImageVar = np.uint8(gray)


# In[111]:


plt.subplot(121),plt.imshow(gray),plt.title('Gray Out')
plt.subplot(122),plt.imshow(cannyImageVar),plt.title('Median Blur of Blur Of Grayscale')
plt.show()




cannyVar = np.uint8(imAv)
cannyVar2 = np.uint8(distort)
cannyVar3 = np.uint8(gray)
cannyCanny = np.uint8(cannyImageVar)


# In[118]:


plt.subplot(121),plt.imshow(cannyVar),plt.title('First Var')
plt.subplot(122),plt.imshow(cannyVar2),plt.title('Second Var')
plt.show()


# In[120]:


plt.subplot(121),plt.imshow(cannyVar3),plt.title('Third Var')
plt.subplot(122),plt.imshow(cannyCanny),plt.title('Fourth Var')
plt.show()





thresh = 127
imBin = cv2.threshold(gray, thresh, 25, cv2.THRESH_BINARY)[1]


# In[122]:


edgeTwo = cv2.Canny(cannyVar2,100,200)

plt.subplot(121),plt.imshow(images[0],cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edgeTwo,cmap = 'gray')
plt.title('Edge Image Little Effect'), plt.xticks([]), plt.yticks([])
plt.show()



# In[123]:


edgeThree = cv2.Canny(cannyVar3,100,200)

plt.subplot(121),plt.imshow(images[0],cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edgeThree,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


# In[136]:


edgeAverage = cv2.Canny(cannyCanny,100,200)

plt.subplot(121),plt.imshow(images[0],cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edgeAverage,cmap = 'gray')
plt.title('Edge Trial'), plt.xticks([]), plt.yticks([])
plt.show()


# In[124]:


edgeBest = cv2.Canny(cannyVar,100,200)

plt.subplot(121),plt.imshow(images[0],cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edgeBest,cmap = 'gray')
plt.title('Edge Best'), plt.xticks([]), plt.yticks([])
plt.show()


thresh = 150
finalDisplay = cv2.threshold(edgeBest, thresh, 25, cv2.THRESH_BINARY)[1]


# In[139]:


#cv2.drawContours(finalDisplay, contours, -1, (0,255,0), 3)


# In[140]:


cv2.imshow('Final Result from edges', finalDisplay)
cv2.waitKey(0)



print('This concludes our process, and what we have accomplished for the assignment. To try another folder, please run the executable again. Thanks.')
cv2.destroyAllWindows()



# In[ ]:


sys.exit()
quit()

