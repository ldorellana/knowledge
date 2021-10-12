# Databricks notebook source
import plotly.io as pio
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np

# COMMAND ----------

def set_renderer(render: str='jupyterlab', height: int=950, width: int=500):
    newrender = pio.renderers[render]
    newrender.width = width
    newrender.height = height
    
    pio.renderers.default = render

# COMMAND ----------

def graph_cluster_features(df: pd.DataFrame,  clusters: str='cluster', title: str='CLUSTERS FEATURES COMPARISON', 
                           rows: int=2, cols: int=2, height: int=800, width: int=800, horizontal_spacing: float=0.05,
                           renderer: str='jupyterlab', font: int=14, vertical_spacing: float=0.1):
     
    """
    
    Takes a pandas dataframe and graph boxplots to compare the features of each cluster
    
    df: pandas DataFrame with the data
    clusters: name of the column containing the clusters
    title: title to show for the whole plot
    rows: number of rows to divide the subplots
    cols: number of columns to divide the subplots
    height: height of the whole plot
    width: width of the whole plot
    
    """
    
    
    #set_renderer(renderer, height, width)
    
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=df.columns, 
                        horizontal_spacing = horizontal_spacing, vertical_spacing = vertical_spacing)
    
    #initial position for subplots
    col = 0
    row = 1
    #go thru every feature
    for feature in df.columns:
        #if the feature is not the cluster colun
        if feature != clusters:
            #go thru the columns and rows
            if col < (cols):
                col+= 1
            else:
                #next row
                row+=1
                col=1

            #add the boxplots to the plot
            fig.add_trace( go.Box(y=df[feature],  
                                 x=df[clusters],
                                 name='',
                                 boxpoints='all', 
                                 text=df.index,
                                 customdata=df,
                                 hovertemplate=(
                                   '<b>店舗: %{text}</b><br>'
                                   'グループ: %{x}<br>'
                                   '訪問率: %{y}%<br>'
                                   '<extra></extra>'
                                 )
                                                              
                                ),
                          row=row,col=col, )    
        
    #update the layout
    fig.update_layout(title_text=title ,showlegend=False,
                     colorway=px.colors.qualitative.T10, font={'size':font})
    
    fig.update_layout(height=rows*400)
    #fig.update_layout(height=height, width=width)
    fig.update_xaxes(tickfont=dict(size=12), 
                     categoryorder='category ascending',
                     title=dict(font=dict(size=14), text='グループ'),
                    )
    
    return fig
