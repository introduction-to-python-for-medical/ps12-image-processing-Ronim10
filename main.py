from skimage.filters import median
from skimage.morphology import ball
from PIL import Image

image=load_image('פרח.jpg')
plt.imshow(image)
clean_image = median(image, ball(3))
edgeMAG = edge_detection(clean_image)
plt.imshow(edgeMAG, cmap='gray')
plt.show()
# prompt: Convert the resulting edgeMAG array into a binary array (values of 0 and 1, or True and False) by choosing a threshold value.
# To choose the threshold value, it is recommended to look at the histogram of the image, as demonstrated in the practice session.

import matplotlib.pyplot as plt
threshold = 40 
edge_binary = edgeMAG > threshold
plt.imshow(edge_binary, cmap='gray')
plt.show()
from PIL import Image
edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
