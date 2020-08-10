import pandas as pd
import plotly.express as px
import numpy as np

import os
os.chdir('texas-mobility')

global_mobility = pd.read_csv('Global_Mobility_Report.csv')
tx_mobility = global_mobility[global_mobility['sub_region_1']=='Texas']

pd.to_datetime(tx_mobility['date'], format='%Y-%m-%d')
pd.to_numeric(tx_mobility['census_fips_code'])
pd.to_numeric(tx_mobility["parks_percent_change_from_baseline"])

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig = px.choropleth(tx_mobility, 
                    locations ="census_fips_code", 
                    locationmode = 'USA-states',
                    geojson = counties,
                    color="parks_percent_change_from_baseline", 
                    hover_name ="sub_region_2",  
                    color_continuous_scale = px.colors.sequential.Darkmint, 
                    scope ="usa", 
                    animation_group ="date",
                    animation_frame = 'date',
                    labels={'date': 'Date', 'parks_percent_change_from_baseline':'Percent change', 'sub_region_2':'County'},
                    hover_data=['date', 'parks_percent_change_from_baseline'],
                    title='Mobility data for parks based on baseline reported by Google'
                    ) 
fig.show()