import numpy as np
import matplotlib.pyplot as plt

# Create a black and white image (e.g., 5x5 pixels)
img = np.array([[0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [1, 1, 1, 1, 1],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0]])
img[2,1]=0
# Plot the image
plt.imshow(img, cmap='gray')
plt.title('Black and White Image')
plt.axis('off')  # Turn off axis labels
plt.show()
