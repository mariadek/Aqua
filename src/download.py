from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

def Sentinel3MarineL1(footprint, date):
    api = SentinelAPI('aqualedger', 'aqualedger2021', 'https://coda.eumetsat.int/')

    products = api.query(footprint,
                         date,
                         producttype = 'OL_1_EFR___',
                         platformname = 'Sentinel-3'
                        )

    products_df = api.to_dataframe(products)

    if products_df.shape[0] > 0:
        print(f"Sentinel-3 Marine Data (Level 1) found: {products_df.shape[0]}")
        for i in products_df['uuid']:
            api.download(i, directory_path = "./input/Sentinel3/Level1")
    else:
        print("No Sentinel-3 Marine Data (Level 1) :(")

def Sentinel3MarineL2(footprint, date):
    api = SentinelAPI('aqualedger', 'aqualedger2021', 'https://coda.eumetsat.int/')

    products = api.query(footprint,
                         date,
                         producttype = 'OL_2_WFR___',
                         platformname = 'Sentinel-3'
                        )

    products_df = api.to_dataframe(products)

    if products_df.shape[0] > 0:
        print(f"Sentinel-3 Marine Data (Level 2) found: {products_df.shape[0]}")
        for i in products_df['uuid']:
            api.download(i, directory_path = "./input/Sentinel3/Level2")
    else:
        print("No Sentinel-3 Marine Data (Level 2) :(")

def Sentinel2(footprint, date):
    api = SentinelAPI('aqualedger', 'aqualedger2021', 'https://apihub.copernicus.eu/apihub')

    products = api.query(footprint,
                         date,
                         producttype = 'S2MSI1C',
                         platformname = 'Sentinel-2',
                         tileid = '34SDJ'
                        )

    products_df = api.to_dataframe(products)

    if products_df.shape[0] > 0:
        print(f"Sentinel-2 Data (Level 1) found: {products_df.shape[0]}")
        for i in products_df['uuid']:
            api.download(i, directory_path = "./input/Sentinel2/Level1")
    else:
        print("No Sentinel-2 Data (Level 1) :(")

if __name__ == "__main__":

    footprint = geojson_to_wkt(read_geojson('/app/src/aoi.geojson'))

    Sentinel3MarineL1(footprint, date = ("NOW-1DAY", "NOW"))
    Sentinel3MarineL2(footprint, date = ("NOW-1DAY", "NOW"))
    Sentinel2(footprint, date = ("NOW-1DAY", "NOW"))
