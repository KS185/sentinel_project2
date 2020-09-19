'''
1. creating tiffs from each raw-dataset
2. combine them with mask data
3. store the masked pictures
'''
import rasterio
import rasterio.mask
from rasterio import plot
import matplotlib.pyplot as plt 
import geopandas as gpd

def write_band(color, color_band, name):
    '''create a .tiff-file with one chosen color-band
        color=path to color-file,
        color_band=opened color-file,
        name=str(color)'''
    pic = rasterio.open(f'../pictures/{name}_fullsize_{date}.tiff', 'w',
                        width=color.width,
                        height=color.height,
                        count=1,
                        driver='GTiff',
                        dtype=color_band.dtype,
                        crs=color.crs,
                        transform=color.transform,
                        nodata=None) 
    pic.write(color_band, 1)
    pic.close()


date = '20200404'

freq_bands = '../data/S2A_MSIL1C_20200404T103021_N0209_R108_T32UMA_20200404T124447.SAFE/GRANULE/L1C_T32UMA_A024987_20200404T103528/IMG_DATA/'

nir = freq_bands + f'T32UMA_{date}T103021_B08.jp2'
red = freq_bands + f'T32UMA_{date}T103021_B04.jp2'

with rasterio.open(red) as red:
    red_band = red.read(1)

with rasterio.open(nir) as nir:
    nir_band = nir.read(1)

write_band(nir, nir_band, 'nir')
write_band(red, red_band, 'red')


rheim = gpd.read_file('./rheim_rect_coords.json')
rheim_mask_nir = rheim.to_crs(nir.crs)
rheim_mask_red = rheim.to_crs(red.crs)

pic_nirsm = rasterio.open(f'../pictures/nir_fullsize_{date}.tiff', 'r')
masked_pic_nir, out_transform_nir = rasterio.mask.mask(pic_nirsm,
                                                   rheim_mask_nir.geometry,
                                                   crop=True,
                                                   filled=True)
pic_nirsm.close()

pic_redsm = rasterio.open(f'../pictures/red_fullsize_{date}.tiff', 'r')
masked_pic_red, out_transform_red = rasterio.mask.mask(pic_redsm,
                                                   rheim_mask_red.geometry,
                                                   crop=True,
                                                   filled=True)
pic_redsm.close()

rio = rasterio.open(f'../pictures/nir_rheim_{date}.tiff', 'w',
                    driver='Gtiff',
                    height=masked_pic_nir.shape[1],
                    width=masked_pic_nir.shape[2],
                    count=masked_pic_nir.shape[0],
                    dtype=masked_pic_nir.dtype,
                    crs=pic_nirsm.crs,
                    transform=out_transform_nir)
rio.write(masked_pic_nir)
rio.close()

rio_red = rasterio.open(f'../pictures/red_rheim_{date}.tiff', 'w',
                        driver='Gtiff',
                        height=masked_pic_red.shape[1],
                        width=masked_pic_red.shape[2],
                        count=masked_pic_red.shape[0],
                        dtype=masked_pic_red.dtype,
                        crs=pic_redsm.crs,
                        transform=out_transform_red)
rio_red.write(masked_pic_red)
rio_red.close()