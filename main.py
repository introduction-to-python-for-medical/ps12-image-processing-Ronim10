from PIL import Image
import numpy as np
from scipy.ndimage import convolve
from image_utils import load_image, edge_detection
from skimage.filters import median
import matplotlib.pyplot as plt
from skimage.morphology import ball


def suppress_noise(image_array):
    clean_image = median(image_array, ball(3))
    return clean_image

# המרה לבינארי
def convert_to_binary(edges, threshold):
    binary_image = (edges > threshold).astype(np.uint8)
    return binary_image

# שמירת תמונה בינארית
def save_binary_image(binary_image, file_name):
    edge_image = Image.fromarray(binary_image * 255)  # המרה לסקלת 0-255
    edge_image.save(file_name)

# הרצת הקוד
image_array = load_image('Snow.jpeg')
clean_image = suppress_noise(image_array)
edges = edge_detection(clean_image)
binary_edges = convert_to_binary(edges, threshold=50)  # סף מתאים בהתאם לתמונה
save_binary_image(binary_edges, 'my_edges.png')
plt.imshow(binary_edges, cmap='gray')
plt.title("Binary Edges")
plt.show()
