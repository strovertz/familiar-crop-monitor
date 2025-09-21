import pynmea2
import pandas as pd
import geopandas as gpd

nmea_data = open("geo/gps_data_20220215-070028.nmea", "rb")

coordinates_data = []

for message_bytes in nmea_data.readlines():    
    try:
        message = message_bytes.decode("utf-8").replace("\n", "").replace("\r", "")
        parsed_message = pynmea2.parse(message)
    except:
        # skip invalid sentences
        continue

    cga_data = {}
    
    # process only GGA messages
    if parsed_message.sentence_type == "GGA":
        for attr in ["timestamp", "latitude", "longitude", "latitude", "horizontal_dil", "num_sats", "gps_qual"]:
            cga_data[attr] = getattr(parsed_message, attr)
        coordinates_data.append(cga_data)
        
df = pd.DataFrame(coordinates_data)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude, crs="EPSG:4326"))
print(gdf)
import matplotlib.pyplot as plt
import xyzservices.providers as xyz
import contextily as ctx

fig = plt.figure(figsize=(10,10))
ax = plt.axes()

gdf[gdf.gps_qual > 0].plot(ax=ax, alpha=.2, edgecolor="#ffff", color='red')

# Use the `xyzservices` provider directly
xyz.add_basemap(ax, source=xyz.Stamen.TonerLite, crs="EPSG:4326", alpha=.3)

plt.show()