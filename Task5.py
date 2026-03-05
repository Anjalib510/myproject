from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# load images
content = Image.open("content.jpg").resize((256,256))
style = Image.open("style.jpg").resize((256,256))

# convert images to arrays
content_array = np.array(content)
style_array = np.array(style)

# simple style transfer (blend the images)
output_array = (0.6 * content_array + 0.4 * style_array).astype(np.uint8)

# convert back to image
output = Image.fromarray(output_array)

# display images
plt.figure()
plt.title("Content Image")
plt.imshow(content)

plt.figure()
plt.title("Style Image")
plt.imshow(style)

plt.figure()
plt.title("Output Image")
plt.imshow(output)

plt.show()