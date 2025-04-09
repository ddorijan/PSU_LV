import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image_path = 'example.png'  
image = mpimg.imread(image_path)

print(f"Originalna slika dimenzije: {image.shape}")

pixels = image.reshape(-1, 3) 

n_clusters = 10  
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(pixels)

quantized_pixels = kmeans.cluster_centers_[kmeans.labels_]
quantized_image = quantized_pixels.reshape(image.shape)


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Originalna slika')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(quantized_image.astype(int)) 
plt.title(f'Kvantizirana slika s {n_clusters} boja')
plt.axis('off')

plt.show()
