# Databricks notebook source
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from yellowbrick.cluster import KElbowVisualizer
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import n_colors
import numpy as np
import math

# COMMAND ----------

def log_transform(data):
  
  # create a copy to save the log transform values
  data_log = np.log(data.copy())
  
  return data_log

# COMMAND ----------

def standard_scal(data):
  
  # create a copy to save the scaled values
  data_scaled = data.copy()
  
  # create the scaler
  scaler = StandardScaler()
  
  # save the scaled data and round it
  data_scaled[data_scaled.columns] = scaler.fit_transform(data)
  
  return data_scaled

# COMMAND ----------

def min_max_scal(data, feature_range=(1,100)):
  
  # create a copy to save the scaled values
  data_scaled = data.copy()
  
  # create the scaler
  scaler = MinMaxScaler(feature_range=feature_range)
  
  # save the scaled data and round it
  data_scaled[data_scaled.columns] = scaler.fit_transform(data)
  
  return data_scaled

# COMMAND ----------

def scale_data(data):
  
  # scale in a range
  data = min_max_scal(data, feature_range=(1,100))
  
  # log transform
  data = log_transform(data)
  
  # standar scaller
  data = standard_scal(data)
  
  return data

# COMMAND ----------

def transform_col(data: pd.DataFrame(), groupby: list=[], col: str='', agg_op: str='count', transform: str=''):
  
  """
  Transform a column of the dataframe
  1. Aggregate the values needed
  2. Obtain the percent for each subgroup
  3. Pivot the subgroup with the values
  4. Scale the values to the main group
  5. Return the new dataframe
  
  --------
  
  Inputs:
  data: dataframe to use
  groubpy: list with columns to convert to index/cols
  col: name of the column to aggergate
  agg_op: aggregate operation to perform
  new_col: name of the resulting column
  
  Outputs:
  dataframe with the converted axis
  
  """
  # aggregate the data
  data_agg = (data
             .groupby(groupby)
             .agg(agg_col= pd.NamedAgg(col, agg_op))
            )

  # obtain the percentage by group
  percent =((data_agg['agg_col'] / data_agg.groupby(level=0)['agg_col'].sum() * 100) # calculate the % in the subgroup
            .rename('aggregated')
            .round(1)
            .to_frame()
           )

  # keep only percentage column
  data_agg = (data_agg.join(percent)
              .drop(columns='agg_col')
              .reset_index()
             )
  
  # pivot values
  data_agg = data_agg.pivot(index=groupby[0], columns=groupby[1], values='aggregated')
  
  # scale data
  if transform == 'scale':
    data_agg = scale_data(data_agg)
  elif transform == 'minmax':
    data_agg = min_max_scal(data_agg, feature_range=(1,100))
    
  
  return data_agg

# COMMAND ----------

def test_clusters(data: pd.DataFrame(), tests: list=[1,1,1]):
    
    """
    Test the best number of clusters 
    1. Generate the Kmeans model
    2. Run the differnt tests
    3. Show the results
    
    --------
    
    Inputs:
    data: dataframe with data to test the clustering
    tests: list with 3 positions
      0. Run Elbow test
      1. Run Calinski-harabasz test
      3. Run Silhouette score test
    
    Outputs:
    visualizations for the different tests
    
    """

    #create the model
    model = KMeans(init='k-means++', max_iter=600, n_init=10, random_state=0)

    if tests[0]:
        #find the inflexion point
        #the smaller the better
        visualizer = KElbowVisualizer(model, k=(2,15), timings=False, locate_elbow=False)
        visualizer.fit(data)       
        visualizer.show()

    if tests[1]:
        #ratio between cluster dispersion and inter cluster dispersion
        visualizer = KElbowVisualizer(model, k=(2,15), metric='calinski_harabasz', timings=False, locate_elbow=False)
        visualizer.fit(data)        
        visualizer.show()

    if tests[2]:
        #mean value between a sample and all the points in a cluster
        #mean distance between a sample and the next nearest cluster
        visualizer = KElbowVisualizer(model, k=(2,15), metric='silhouette', timings=False, locate_elbow=False)
        visualizer.fit(data)        
        visualizer.show()

    return 

# COMMAND ----------

def run_kmeans(data: pd.DataFrame(), no_clusters: int=4):
    
    """
    Performin Kmeans clustering 
    1. Generate the Kmeans model
    2. Fit & predict the data
    3. Create a series with the index indicading cluster
    4. Return the cluster column
    
    --------
    
    Inputs:
    data: dataframe with data to test the clustering
    no_clusters: number of clusters to create
    Return:
    cluster_data: pd.Series() with the cluster for each index
    
    """
    
    cluster_data = pd.DataFrame()
        
    #create the model with n number of clusters
    modelkm = KMeans(n_clusters=no_clusters, init='k-means++', max_iter=600, n_init=10, random_state=1)
    
    #fit & predict the data attributes
    y_model =  modelkm.fit_predict(data)
        
    #save the clusters in a new column
    cluster_data[f'cluster{no_clusters}'] = pd.Series(y_model, index=data.index).astype('category')

  
    return cluster_data
