# FILES INFO

## kmeans_test.py
Requirments: pandas, sklearn, yellowbrick pandas, plotly
Kmeans clustering requires that the user provides a number of clusters to create.   
Since if is an unsupervised learning ML algorithm, most of the times it is not possible   
to know the 'real' number of cluster. Different algorithms to test the best fitted   
number of clusters for each specific data input. 

The file provides the transformation needed to perform kmeans and also provides 3 different  
tests to help the user select the number of clusters. For the test, it makes use of the   
[yellobrick library](https://www.scikit-yb.org/en/latest/). 

# cluster_graph.py
Requirments: pandas, sklearn, yellowbrick pandas, plotl
Provides different graph methods that help visualize the clutsters provided in a dataframe. 
Each of the attributes used to generate the clusters can be graph in boxplots.  
The boxplots are a easy way to visualize the difference between the clustesr.   

