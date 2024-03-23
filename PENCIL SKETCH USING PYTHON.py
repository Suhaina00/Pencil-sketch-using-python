#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install opencv-python


# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[23]:



# Path to the image file
image_path = r"C:\Users\suhai\OneDrive\Desktop\IMAG\IMG.png"

# Read the image
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is not None:
    print("Image loaded successfully.")
else:
    print("Failed to load image.")

# Now you can use 'img' for further processing


# In[24]:


img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img)
plt.show()


# In[25]:


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.axis('off')
plt.imshow(gray_img)
plt.show()


# In[26]:


#inv_gray_img = 255 - gray_img
inv_gray_img = cv2.bitwise_not(gray_img)
plt.axis('off')
plt.imshow(inv_gray_img)
plt.show()


# In[27]:


blur_img = cv2.GaussianBlur(inv_gray_img,(21,21),0)
plt.axis('off')
plt.imshow(blur_img)
plt.show()


# In[28]:


#inv_blur_img = 255 - blur_img
inv_blur_img = cv2.bitwise_not(blur_img)
plt.axis('off')
plt.imshow(inv_blur_img)
plt.show()


# In[29]:


pencil_img = cv2.divide(gray_img,inv_blur_img,scale = 256.0)
plt.axis('off')
plt.imshow(pencil_img)
plt.show()


# In[30]:


cv2.imwrite("./output_image.png",pencil_img)


# In[31]:



# Path to the output image file
output_image_path = r"C:\Users\suhai\OneDrive\Desktop\IMAG\output_image.png"

# Assuming 'pencil_img' is the image you want to save
# cv2.imwrite() function is used to save the image
cv2.imwrite(output_image_path, pencil_img)

print(f"Output image saved at: {output_image_path}")


# In[ ]:





# In[ ]:




