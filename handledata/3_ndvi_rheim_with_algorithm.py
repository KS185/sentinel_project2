'''
Implementing an algorithm for calculating green area/built-up area
'''

import rasterio
from rasterio import plot
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pickle


date = '20200404'

with rasterio.open(f'../pictures/red_rheim_{date}.tiff', 'r') as roi_red_band:
    roi_red = roi_red_band.read(1)


with rasterio.open(f'../pictures/nir_rheim_{date}.tiff', 'r') as roi_nir_band:
    roi_nir = roi_nir_band.read(1)


ndvi_band = ((roi_nir.astype('float64')-roi_red.astype('float64'))/
             (roi_nir+roi_red))


# -----------------------------------------------
# k-means

ndvi_band_filled = np.nan_to_num(ndvi_band, nan=-1)

#plot.show(ndvi_band_filled)

ndvi_band_ff = np.ravel(ndvi_band_filled)
ndvi_band_ff = np.reshape(ndvi_band_ff, (ndvi_band_ff.shape[0], 1))

levels = 3 
max_iter = 200

kmeans = KMeans(n_clusters=levels, max_iter=max_iter)
kmeans.fit(ndvi_band_ff)

with open('./model_kmeans.pickle', 'wb') as f:
                pickle.dump(kmeans, f)


ndvi_kmeans = kmeans.predict(ndvi_band_ff)
ndvi_kmeans_reshape = np.reshape(ndvi_kmeans, (ndvi_band_filled.shape[0],
                                                ndvi_band_filled.shape[1]))

ndvi_kmeans_reshape = ndvi_kmeans_reshape.astype('uint8')
vmin = ndvi_kmeans_reshape.min()
vmax = ndvi_kmeans_reshape.max()

plt.imshow(ndvi_kmeans_reshape, vmin=vmin, vmax=vmax)
plt.savefig(f'../pictures/ndvi_kmeans{max_iter}_rheim_{date}.png')
plt.show()
