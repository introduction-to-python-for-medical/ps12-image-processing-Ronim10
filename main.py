from skimage.filters import median
from skimage.morphology import ball
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from image_utils import load_image, edge_detection
image=load_image('פרח.jpg')
plt.imshow(image)
clean_image = median(image, ball(3))
edgeMAG = edge_detection(clean_image)
threshold = 40 
edge_binary = edgeMAG > threshold
plt.imshow(edge_binary, cmap='gray')
edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
