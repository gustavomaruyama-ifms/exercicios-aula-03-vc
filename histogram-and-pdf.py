from skimage import io, color
import numpy as np

img = io.imread('lenna-master.jpg')
w, h, _ = img.shape

gray_image = color.rgb2gray(img);

# Montando histograma
histogram = np.zeros(256, dtype=np.int64)
for x in range(w):
    for y in range(h):
        gray_nivel = np.uint8(gray_image[x,y] * 255)
        histogram[gray_nivel]+=1

# Calculando PDF
pdf = histogram/(w*h)

print("Histograma: \n",histogram)
print("PDF: \n",pdf)
print("Soma PDF: \n",pdf.sum())