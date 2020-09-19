'''
Implementing an algorithm for calculating green area/built-up area
'''

import rasterio
from rasterio import plot
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pickle

date20 = '20200404'
date19 = '20190430'


with open('model_kmeans.pickle', 'rb') as f:
                kmeans = pickle.load(f)

#___________________________________________________________________
#whole rhein-main-region April 2020
freq_bands = '../data/S2A_MSIL2A_20200404T103021_N0214_R108_T32UMA_20200404T135955.SAFE/GRANULE/L2A_T32UMA_A024987_20200404T103528/IMG_DATA/R10m/'
nir = freq_bands + 'T32UMA_20200404T103021_B08_10m.jp2'
red = freq_bands + 'T32UMA_20200404T103021_B04_10m.jp2'

red = rasterio.open(red)
red_band = red.read(1)
red.close()

nir = rasterio.open(nir)
nir_band = nir.read(1)
nir.close()

ndvi_band_rm = ((nir_band.astype('float64')-red_band.astype('float64'))/
             (nir_band+red_band))   

ndvi_fnan = np.nan_to_num(ndvi_band_rm, nan=-1)

ndvi_ff = np.ravel(ndvi_fnan)
ndvi_ff = np.reshape(ndvi_ff, (ndvi_ff.shape[0], 1))

ndvi_km = kmeans.predict(ndvi_ff)

ndvi_km_res = np.reshape(ndvi_km, (ndvi_fnan.shape[0], ndvi_fnan.shape[1]))
ndvi_km_res = ndvi_km_res.astype('uint8')
np.save('../data/ndvi_km_res20.npy', ndvi_km_res)
vminrm = ndvi_km_res.min()
vmaxrm = ndvi_km_res.max()

plt.imshow(ndvi_km_res, vmin=vminrm, vmax=vmaxrm)
plt.savefig(f'../pictures/ndvi_kmeans_rm{date20}.tiff', dpi=1000)
plt.show()

unique_elements, count_elements = np.unique(ndvi_km_res, return_counts=True )
print(unique_elements)
print(count_elements)
