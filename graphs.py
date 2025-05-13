import plotly as py
import plotly_express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import geopandas as gpd
from pandas.io.formats.info import show_counts_sub
import numpy as np

df = pd.read_csv("database.csv")
df["is_fraud"].astype(str)
df['pred'].astype(str)
#df.dropna(inplace=True)


def create_map():
    df = pd.read_csv("database.csv")
    df["is_fraud"].astype(str)
    df['pred'].astype(str)

    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.long,df.lat), crs="EPSG:4326")

    fig = px.scatter_geo(gdf, color = "category", lat= gdf.geometry.y ,lon= gdf.geometry.x, hover_name="category",hover_data=["city","city_pop","state","amt","is_fraud","job"])
    fig.update_layout(geo_scope="usa",paper_bgcolor="#19272a")
    fig.update_layout(legend = dict(font=dict(family="Asimov",color = "#cccccc")))

    fig.update_geos(showlakes=True, lakecolor="#19272a", bgcolor="#19272a", showsubunits =True, subunitcolor="#cccccc")
    return fig

def create_counters():
    df = pd.read_csv("database.csv")
    df["is_fraud"].astype(str)
    df['pred'].astype(str)


    fig2 = go.Figure()
    fig2.add_trace(go.Indicator(mode= "number",
                   value = df['pred'].astype(int).sum(),
                   number= {'font_color':'#cccccc'},
                   title={"text":"<span style='font-size:0.8em;color:#cccccc'> amount of predicted fraud</span>"},
                   domain = {'x':[0,0.5],'y':[0.5,1]}))

    fig2.add_trace(go.Indicator(mode= "number",
                   value = df["is_fraud"].astype(int).sum(),
                   number= {'font_color':'#cccccc'},
                   title={"text":"<span style='font-size:0.8em;color:#cccccc'>actual fraud</span>"},
                   domain = {'x':[0.5,1],'y':[0.5,1]}))

    fig2.add_trace(go.Indicator(mode= "number",
                   value = np.where(df["is_fraud"] < df['pred'],df['is_fraud']+df["pred"],0).astype(int).sum(),
                   number= {'font_color':'#cccccc'},
                   title={"text":"<span style='font-size:0.8em;color:#cccccc'>false positives</span>"},
                   domain = {'x':[0,0.5],'y':[0,0.5]}))

    fig2.add_trace(go.Indicator(mode= "number",
                   value = np.where(df["is_fraud"] > df['pred'],df['is_fraud']+df["pred"],0).astype(int).sum(),
                   number= {'font_color':'#cccccc'},
                   title={"text":"<span style='font-size:0.8em;color:#cccccc'>false negatives</span>"},
                   domain = {'x':[0.5,1],'y':[0,0.5]}))

    fig2.update_layout(paper_bgcolor="#19272a")
    fig2.update_layout(legend = dict(font=dict(family="Asimov",color = "#cccccc")))
    return fig2

fig = create_map()
fig2 = create_counters()

