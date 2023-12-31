# -*- coding: utf-8 -*-
from google.colab import drive
drive.mount('/content/drive')

import sys
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

image = cv2.imread("/content/drive/MyDrive/Colab Notebooks/images/menganti.jpeg")

cv2_imshow(image)

print("image")
print(image.shape)

imageabu = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imagehsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

print("Image Abu")
cv2_imshow(imageabu)

print("Image RGB")
cv2_imshow(imagergb)

print("Image HSV")
cv2_imshow(imagehsv)

B, G, R = cv2.split(image)
print(B.shape)
print(G.shape)
print(R.shape)

print("Blue")
cv2_imshow(B)

print("Green")
cv2_imshow(G)

print("Red")
cv2_imshow(R)

gabung = cv2.merge([B,G,R])
print("Gabung")
cv2_imshow(gabung)

plt.figure(figsize=[10,10])
plt.subplot
plt.imshow(imagergb)
plt.show()

plt.figure(figsize=[10,10])
plt.subplot(231)
plt.imshow(imagergb)
plt.subplot(232)
plt.imshow(imagergb)
plt.subplot(233)
plt.imshow(imagergb)
plt.subplot(234)
plt.imshow(imagergb)
plt.subplot(235)
plt.imshow(imagergb)
plt.subplot(236)
plt.imshow(imagergb)

plt.show()