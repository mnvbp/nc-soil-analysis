import geoplot as gplt
import geopandas as gpd
import matplotlib.pyplot as plt
import geoplot.crs as gcrs
import pandas as pd
import seaborn as sns
import numpy as np
import plotly.express as px


data = '/Users/manavparikh/Desktop/output/data_edit2_latlong.csv'
path = '/Users/manavparikh/Downloads/North_Carolina_State_and_County_Boundary_Polygons/North_Carolina_State_and_County_Boundary_Polygons.shp'
output = '/Users/manavparikh/Desktop/output/geoplot.html'
average = '/Users/manavparikh/Desktop/output/county.csv'



def csv_to_gdf(csv: str, lat: str, long: str, crs: str = "EPSG:4326", delimit: str = ",", header: int = 0) -> gpd:
    df = pd.read_csv(csv, delimiter=delimit, header = header)
    df = df[df[lat].notna()]
    df = df.reset_index()
    gdf = gpd.GeoDataFrame(
        df,
        geometry= gpd.points_from_xy(df.loc[:, long], df.loc[:, lat]),
        crs=crs)
    return (gdf)

gdf = csv_to_gdf(data, lat="LAT", long="LON")

#import shapefile and set to same CRS
world = gpd.read_file(path)
world = world.to_crs("EPSG:4326")


#removing outliers based on seaborn boxplot
#sns.boxplot(gdf['Mg']) #seaborn
#gdf["plot"] = np.where(gdf['pH'] < 9, gdf['pH'], np.nan)
#gdf["plot"] = np.where(gdf['plot'] > 0, gdf['plot'], np.nan)


#matplotlib chloropleth
#merge= pd.merge(world, pd.read_csv(average), on='County')
#merge.plot(column="Zn", cmap='rainbow', legend=True)
#plt.show()


#plotly choropleth
#merge= pd.merge(world, pd.read_csv(average), on='County')
#merge = merge.set_index('County')
#for columns in merge.columns:
#    print(columns)
#fig = px.choropleth(merge, geojson=merge.geometry, locations=merge.index, color='VW RESULT')
#fig.update_geos(fitbounds="locations", visible=False)
#fig.show()


#geoplot scatterplot
#ax = gplt.polyplot(world)
#gplt.pointplot(gdf, ax=ax, hue='pH', cmap='rainbow', legend=True)
#gplt.show()


#plotly scatter (NOT WORKING)
#fig = px.scatter_geo(world, geojson=world.geometry, lat=gdf.LAT, lon=gdf.LON, color = gdf.pH)
#fig.update_geos(fitbounds="locations", visible=False)
#fig.show()