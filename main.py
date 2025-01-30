from skimage.filters import median
from skimage.morphology import ball

clean_image = median(image, ball(3))
from PIL import Image

edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt

perach = load_image('Snow.jpeg')
clean_image = median(perach, ball(3))
edge_mag = edge_detection(clean_image)

edge_binary = edge_mag > 40
plt.imshow(edge_binary, cmap='gray')

edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
