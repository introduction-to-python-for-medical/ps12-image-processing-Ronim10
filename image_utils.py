from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    pass # Replace the pass with your code

def edge_detection(image):
    pass # Replace the pass with your code
def load_image(file_path):
  image = Image.open(file_path)
  image_array = np.array(image)
  return image_array

load_image('פרח.jpeg')
def edge_detection(image_array):
  gray_image = np.mean(image_array, axis=2)
  kernelY = np.array([
      [1, 2, 1],
      [0, 0, 0],
      [-1, -2, -1]
  ])
  kernelX = np.array([
      [-1, 0, 1],
      [-2, 0, 2],
      [-1, 0, 1]
  ])
  edgex= convolve2d(gray_image, kernelX, mode = 'same', boundary= 'fill', fillvalue = 0 )
  edgey= convolve2d(gray_image, kernelY, mode = 'same', boundary= 'fill', fillvalue = 0)
  edgemag = np.sqrt(edgex*2 + edgey*2)
  return edgemag

edge_detection(load_image('פרח.jpeg')
