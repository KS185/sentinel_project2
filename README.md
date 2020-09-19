# sentinel_project - purpose
Analyze Sentinel-2 data of Frankfurt-area, including Frankfurt, Mainz,
Wiesbaden and Darmstadt. Purpose was to find out which amount of vegetated
area was lost between April 2019 to April 2020.

## Packages:
- Sentinelsat: for downloading data from Copernicus Open Access Hub
- Rasterio: for handling datasets

## Theory
### NDVI: Normalized Difference Vegetation Index  
NDVI = (NIR-red)/(NIR+red)

This index is based on the assumption that an area with green vegetation 
reflects less red and more NIR than areas with less vegetation.
Result of this calculation is are values between -1 and 1, where positive
values corresponds to green areas.

### Used data
The datasets used are of Level2A, which contains Bottom of Atmosphere (BOA)
data. Each of it contains 13 frequency bands. Four of them which are used in 
the project are:  
B02: blue  
B03: green  
B04: red  
B08: NIR  
All of them have a pixelsize of 10x10m².

Geojson-files were build with geojson.io homepage.

Reference dataset for kmeans: Ruesselsheim - area, date: 20200404
Analyzed with kmeans 200 iterations.

## Result

year | vegetated area | other area  
---|---|---
2019 | 90 | 10  
2020 | 84 | 16  

For verification see:
https://umwelt.hessen.de/umwelt-natur/wald/waldzustand 




## Licenses:
- Copernicus Sentinel data [2020]
- Contains modified Copernicus Sentinel data [2020]
- © GeoBasis-DE / BKG (2020) 

## Nice-to-know
- https://earth.esa.int/web/sentinel/user-guides/sentinel-2-msi/product-types/level-2a

## Links:
- https://sentinelsat.readthedocs.io/en/stable/api.html
- https://rasterio.readthedocs.io/en/latest/quickstart.html
- http://geojson.io/#map=2/20.0/0.0

