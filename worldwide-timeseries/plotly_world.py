import pandas as pd
import plotly.express as px

import os
os.chdir('worldwide-timeseries')

world_cases = pd.read_csv('WHO-COVID-19-global-data.csv')
world_cases['Date'] = pd.to_datetime(world_cases['Date_reported'], format='%Y-%m-%d', exact=False)
world_cases[' Cumulative_cases'] = pd.to_numeric(world_cases[' Cumulative_cases'])
  
fig = px.choropleth(world_cases, 
                    locations =" Country_code", 
                    color =" Cumulative_cases", 
                    hover_name =" Country",  
                    color_continuous_scale = px.colors.sequential.Plasma, 
                    scope ="world", 
                    animation_frame ="Date") 
fig.show()