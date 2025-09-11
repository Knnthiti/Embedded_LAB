import cv2
import numpy as np
kernel1 = np.array([[ 0, 0, 0],
                    [ 0, 1, 0],
                    [ 0, 0, 0]]) # Identity kernel

kernel2 = np.array([[ 1, 4, 6, 4, 1],
                    [ 4, 16, 24, 16, 4],
                    [ 6, 24, 36, 24, 6],
                    [ 4, 16, 24, 16, 4],
                    [ 1, 4, 6, 4, 1]]) / 256 # Gaussian blur

kernel3 = np.array([[ 1, 1, 1],
                    [ 1, 1, 1],
                    [ 1, 1, 1]]) / 9 # Box blur

kernel4 = np.array([[ 0, -1, 0],
                    [-1, 5, -1],
                    [ 0, -1, 0]]) # Sharpen

kernel5 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]]) # Edge detection

kernel6 = np.array([[-2, -1, 0],
                    [-1, 1, 1],
                    [ 0, 1, 2]]) # Emboss

kernel7 = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]]) # right sobel

image = cv2.imread('car.jpg')
print('Image Dimensions : ',image.shape) # height, width, number of channels
cv2.imshow('original image', image)
dst = cv2.filter2D(src=image, ddepth=-1, kernel= kernel5) # depth is same as original
cv2.imshow('filter2d image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()