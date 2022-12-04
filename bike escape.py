
from google.colab import drive
drive.mount('/content/drive')

!pip install gpxcsv
!pip install geobr
!pip install geopandas
!pip install osmnx
!pip install matplotlib==3.1.3

from gpxcsv import gpxtolist
import pandas as pd
import geopandas as gpd
import geobr
import osmnx as ox
import os
from osmnx import graph_from_place
import matplotlib.pyplot as plt


df = pd.DataFrame(
    gpxtolist('/content/drive/MyDrive/PROGRAM./Pedalada_na_hora_do_almo_o.gpx'))

folder = '/content/drive/MyDrive/PROGRAM./DADOS/FRED'
files = os.listdir(folder)

br = geobr.read_metro_area(year=2010)
poa = br.query('name_muni == "Porto Alegre"')


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles      


def transformar(path):
  path = path
  df = pd.DataFrame(gpxtolist(path))
  gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon,df.lat))

  return gdf

  
b = []

fig, ax = plt.subplots(figsize=(50,50))

for i in list_files:
    x = transformar(i)
    x= x.query('lat < -30.0' and 'lon < -51.0')
    x.plot(ax=ax, markersize=1, cmap='inferno')
    b.append(x)

    
fig, ax = plt.subplots(figsize=(20,20))

for element in b:
  x = element
  x.plot(ax=ax, markersize=1, cmap='inferno')
  
  

 
