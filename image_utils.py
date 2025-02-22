from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def load_image(file_path):
    image = Image.open(file_path)
    image_array = np.array(image)
    return image_array
load_image('פרח.jpg')    
def edge_detection(image_array):
    grayscale_image = np.mean(image_array, axis=2)
    kernelY = np.array([[1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]])
    kernelX = np.array([[1, 2, 1],
                       [0, 0, 0],
                       [-1, -2, -1]])
    edgeX = convolve2d(grayscale_image, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(grayscale_image, kernelY, mode='same', boundary='fill', fillvalue=0) 
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG

edge_detection(load_image('פרח.jpg'))
