%load_ext autoreload
%autoreload 2

!wget https://raw.githubusercontent.com/yotam-biu/ps12/main/image_utils.py -O /content/image_utils.py

from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def load_image(file_path):
    image = Image.open(file_path)
    image_array = np.array(image)
    return image_array

def edge_detection(image_array):
    if image_array.ndim == 3:  # אם התמונה צבעונית
        gray_image = np.mean(image_array, axis=2)
    else:
        gray_image = image_array  # אם התמונה כבר בגווני אפור
    kernelY = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    kernelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    edgeY = convolve2d(gray_image, kernelY, mode="same", boundary="fill", fillvalue=0.0)
    edgeX = convolve2d(gray_image, kernelX, mode="same", boundary="fill", fillvalue=0.0)
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)  
    return edgeMAG
