#Stephen Kerr
# Testing the iris dataset 

# Machine Learning library that contains example datasets.

import sklearn as skl 

# load the dataset.
data = skl.datasets.load_iris()

# Look at the data
##print(data)

# look at the data keys 
##print(data.keys())

# look at the type of the data
##print(type(data))

# Look at the data column from the data 
##print(data['data'])

# Look at the data shape
##print(data['data'].shape)

# the target
##print(data['target'])

# target shape
##print(data['target'].shape)

# target names 
##print(data['target_names'])

# feature names
print(data['feature_names'])

