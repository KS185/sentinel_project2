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

##___________________________________________________________________
##whole rhein-main-region April 2020
#freq_bands = '../data/S2A_MSIL2A_20200404T103021_N0214_R108_T32UMA_20200404T135955.SAFE/GRANULE/L2A_T32UMA_A024987_20200404T103528/IMG_DATA/R10m/'
#nir = freq_bands + 'T32UMA_20200404T103021_B08_10m.jp2'
#red = freq_bands + 'T32UMA_20200404T103021_B04_10m.jp2'
#
#red = rasterio.open(red)
#red_band = red.read(1)
#red.close()
#
#nir = rasterio.open(nir)
#nir_band = nir.read(1)
#nir.close()
#
#ndvi_band_rm = ((nir_band.astype('float64')-red_band.astype('float64'))/
#              (nir_band+red_band))
#
##rasterio.plot.show_hist(rasterio.plot.adjust_band(ndvi_band_rm[0:1], kind='linear'), bins=30)     
#
#ndvi_fnan = np.nan_to_num(ndvi_band_rm, nan=-1)
#
#ndvi_ff = np.ravel(ndvi_fnan)
#ndvi_ff = np.reshape(ndvi_ff, (ndvi_ff.shape[0], 1))
#
#ndvi_km = kmeans.predict(ndvi_ff)
#
#
#ndvi_km_res = np.reshape(ndvi_km, (ndvi_fnan.shape[0], ndvi_fnan.shape[1]))
#ndvi_km_res = ndvi_km_res.astype('uint8')
#np.save('../data/ndvi_km_res20.npy', ndvi_km_res)
#vminrm = ndvi_km_res.min()
#vmaxrm = ndvi_km_res.max()
#
#plt.imshow(ndvi_km_res, vmin=vminrm, vmax=vmaxrm)
#plt.savefig(f'../pictures/ndvi_kmeans_rm{date20}.tiff', dpi=1000)
#plt.show()
#
#unique_elements, count_elements = np.unique(ndvi_km_res, return_counts=True )
#print(unique_elements)
#print(count_elements)

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
# 
rasterio.plot.show_hist(rasterio.plot.adjust_band(ndvi_band_rm2019[0:1], kind='linear'), bins=30)
# 
ndvi_fnan2019 = np.nan_to_num(ndvi_band_rm2019, nan=-1)

ndvi_ff2019 = np.ravel(ndvi_fnan2019)
ndvi_ff2019 = np.reshape(ndvi_ff2019, (ndvi_ff2019.shape[0], 1))

ndvi_km2019 = kmeans.predict(ndvi_ff2019)
#ndvi_km2019.to_csv('./kmeans2019.csv')

ndvi_km_res2019 = np.reshape(ndvi_km2019, (ndvi_fnan2019.shape[0], 
                                        ndvi_fnan2019.shape[1]))

ndvi_km_res2019 = ndvi_km_res2019.astype('uint8')
np.save('../data/ndvi_km_res19.npy', ndvi_km_res2019)
vminrm2019 = ndvi_km_res2019.min()
vmaxrm2019 = ndvi_km_res2019.max()

plt.imshow(ndvi_km_res2019, vmin=vminrm2019, vmax=vmaxrm2019)
plt.savefig(f'../pictures/ndvi_kmeans_rm{date19}.tiff', dpi=1000)
plt.show()
#
##unique_elements2019, count_elements2019 = np.unique(ndvi_km_res2019, return_counts=True )
##print(unique_elements2019)
##print(count_elements2019)
##
##sum2020 = count_elements.sum()
##sum2019 = count_elements2019.sum()
##
##diff=[]
##diff[0]=count_elements[0]-count_elements2019[0]
##diff[1]=count_elements[1]-count_elements2019[1]
##diff[2]=count_elements[2]-count_elements2019[2]
##
##print(diff[0], diff[1], diff[2], sum2019, sum2020)
##
##perc0 = diff[0]/sum2020*100
##perc1 = diff[1]/sum2020*100
##perc2 = diff[2]/sum2020*100
##
##
##print(f'0: {perc0}\%, 1: {perc1}\%, 2: {perc2}\%')