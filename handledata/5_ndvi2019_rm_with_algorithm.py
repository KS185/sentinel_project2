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
#whole rhein-main-region April 2019
freq_bands2019 = '../data/S2A_MSIL2A_20190430T103031_N0211_R108_T32UMA_20190430T140106.SAFE/GRANULE/L2A_T32UMA_A020125_20190430T103551/IMG_DATA/R10m/'
nir2019 = freq_bands2019 + 'T32UMA_20190430T103031_B08_10m.jp2'
red2019 = freq_bands2019 + 'T32UMA_20190430T103031_B04_10m.jp2'

red2019 = rasterio.open(red2019)
red_band2019 = red2019.read(1)
red2019.close()

nir2019 = rasterio.open(nir2019)
nir_band2019 = nir2019.read(1)
nir2019.close()

ndvi_band_rm2019 = ((nir_band2019.astype('float64')-
                  red_band2019.astype('float64'))/
                  (nir_band2019+red_band2019))

ndvi_fnan2019 = np.nan_to_num(ndvi_band_rm2019, nan=-1)

ndvi_ff2019 = np.ravel(ndvi_fnan2019)
ndvi_ff2019 = np.reshape(ndvi_ff2019, (ndvi_ff2019.shape[0], 1))

ndvi_km2019 = kmeans.predict(ndvi_ff2019)

ndvi_km_res2019 = np.reshape(ndvi_km2019, (ndvi_fnan2019.shape[0], 
                                        ndvi_fnan2019.shape[1]))

ndvi_km_res2019 = ndvi_km_res2019.astype('uint8')
np.save('../data/ndvi_km_res19.npy', ndvi_km_res2019)
vminrm2019 = ndvi_km_res2019.min()
vmaxrm2019 = ndvi_km_res2019.max()

plt.imshow(ndvi_km_res2019, vmin=vminrm2019, vmax=vmaxrm2019)
plt.savefig(f'../pictures/ndvi_kmeans_rm{date19}.tiff', dpi=1000)
plt.show()
