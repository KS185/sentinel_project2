"""Load data from Copernicus Open Access Hub"""

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from config import STARTDATE as startdate
from config import ENDDATE as enddate
from config import PLATFORM as platform
from config import CLOUDCOVERING_UPPER as cloudcovering_upper


api = SentinelAPI(None, None)
footprint = geojson_to_wkt(read_geojson('./rm_coord.json'))
request = api.query(footprint,
                    date=(startdate, enddate),
                    platformname=platform,
                    cloudcoverpercentage=(0, cloudcovering_upper))

request_df = api.to_dataframe(request)
request_df_ingestion = request_df.sort_values(['ingestiondate'],
                                              ascending=False)

api.download_all(request_df.index)
