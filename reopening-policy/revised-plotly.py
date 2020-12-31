import numpy as np
import pandas as pd
from datetime import datetime

import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as plo

import os
os.chdir('reopening-policy-viz')

st_abbrev = ['az', 'ca', 'ma', 'fl', 'ri', 'tx', 'ny', 'nj']
st_pop = [7378490, 39937500, 6976600, 21993000, 1056160, 29472300, 19440500, 8936570]

def clean(state, pop):
    state_cases = pd.read_csv(state+'_covid_data.csv')
    state_cases.rename(columns={
     'positive': 'cases_total'
    }, inplace=True)

    state_cases['date'] = pd.to_datetime(state_cases['date'], format='%Y%m%d', exact=False)

    if state == 'fl':
       del state_cases['negative']
    else:
       pass
    
    state_cases['cases_pop'] = (state_cases['cases_total']/pop)*100000
    return state_cases

# clean and read data
az_cases = clean('az', 7378490)
ca_cases = clean('ca', 39937500)
ma_cases = clean('ma', 6976600)
fl_cases = clean('fl', 21993000)
ri_cases = clean('ri', 1056160)
tx_cases = clean('tx', 29472300)
ny_cases = clean('ny', 19440500)
nj_cases = clean('nj', 8936570)

# combine it all into one
state_data = pd.concat([az_cases, ca_cases, ma_cases, fl_cases, ri_cases, tx_cases, ny_cases, nj_cases])


# state policy data with cases
state_policy = pd.read_csv('reopening_policy.csv')
state_policy['date'] = pd.to_datetime(state_policy['date'], format='%m/%d/%Y', exact=False)

# data = [go.Scatter(x=state_data['date'], y=state_data['cases_pop'], mode='lines', name='Cases per 100k', 
#    line=dict(color=(state_data['state'].map(colors)))),
#    go.Scatter(x=state_policy['date'], y=state_policy['cases_pop'], mode='markers',
#       name='Reopening Policies')
# ]

fig = px.line(state_data, x='date', y='cases_pop', color='state', labels={'state': 'State', 'cases_pop':'Cases per 100k', 'date':'Date'},
   title='Date of reopening policy measures for 8 U.S. states')
fig.update_xaxes(rangeslider_visible=True)
fig2 = px.scatter(state_policy, x='date', y='cases_pop', hover_name='type', 
   labels={'state': 'State', 'cases_pop':'Cases per 100k', 'date':'Date'}, hover_data=['state', 'cases_pop'], size_max = 150)

fig.add_trace(fig2.data[0])

# fig.add_scatter(x=state_policy['date'], y=state_policy['cases_pop'], mode='markers', hover_name='type', hoverlabel='<i>State</i>: %{state_policy['state']}'+
#     '<br><b>X</b>: %{x}<br>'+
#     '<b>%{text}</b>',)

fig.layout.yaxis.range = [0, 2250]

fig.write_html("/Users/Neha/Downloads/python/reopening-policy-viz/final-viz.html")
fig.show()

#fig.add_scatter(x=df.date, y=df.20m_critical_power).