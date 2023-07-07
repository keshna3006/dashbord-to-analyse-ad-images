import os
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import webbrowser
from webcolors import rgb_to_name
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

names = []
rgb_values = []
def convert_rgb_to_names(red,green,blue):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    rgb_tuple=(red,green,blue)

    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return  {names[index]}

csv_file_path='sample.csv'
dataframe=pd.read_csv(csv_file_path)
img_column=dataframe['creative_img']
impressions_column=dataframe['impressions']
clicks_column=dataframe['clicks']

colors_in_img=[]

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='using-vision-api-for-dashboard-60c68f966514.json'
client=vision.ImageAnnotatorClient()
image=types.Image()

for i in img_column:
   image.source.image_uri=i
   response_image=client.image_properties(image=image)

   image_data = []

   for c in response_image.image_properties_annotation.dominant_colors.colors[:1]:
       d = {
           'color': c.color,
           'score': c.score,
           'pixel_fraction': c.pixel_fraction
        }
       red=c.color.red
       green=c.color.green
       blue=c.color.blue
       colors_in_img.append(convert_rgb_to_names(red,green,blue))



impressions_df=pd.DataFrame(colors_in_img)
impressions_df.columns=['colors']
impressions_df['impressions']=impressions_column
clicks_df=pd.DataFrame(colors_in_img)
clicks_df.columns=['colors']
clicks_df['clicks']=clicks_column

def returndf(csvfile):
    csv_file_path='sample.csv'
    dataframe=pd.read_csv(csv_file_path)
    img_column=dataframe['creative_img']
    impressions_column=dataframe['impressions']
    clicks_column=dataframe['clicks']
    colors_in_img=[]

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']='using-vision-api-for-dashboard-60c68f966514.json'
    client=vision.ImageAnnotatorClient()
    image=types.Image()

    for i in img_column:
        image.source.image_uri=i
        response_image=client.image_properties(image=image)

        image_data = []

        for c in response_image.image_properties_annotation.dominant_colors.colors[:1]:
           d = {
               'color': c.color,
               'score': c.score,
               'pixel_fraction': c.pixel_fraction
            }
           red=c.color.red
           green=c.color.green
           blue=c.color.blue
           colors_in_img.append(convert_rgb_to_names(red,green,blue))

    dftoreturn=pd.DataFrame(colors_in_img)
    dftoreturn.columns=['colors']
    dftoreturn['impressions']=impressions_column
    dftoreturn['clicks']=clicks_column

    return dftoreturn