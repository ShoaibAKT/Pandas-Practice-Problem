#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keras
import pandas as pd
import numpy as np
import tensorflow.keras as keras

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()


# Load the MNIST dataset
dataset = keras.datasets.mnist.load_data()

# Create dataframes from the MNIST dataset
train_df = pd.DataFrame(list(zip(dataset[0][0], dataset[0][1])), columns =['image', 'label'])
test_df = pd.DataFrame(list(zip(dataset[1][0], dataset[1][1])), columns =['image', 'label'])

# Save the dataframes to CSV files
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)

# Load the CSV files and convert them back to the original format
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_images = train_data['image'].values
train_labels = train_data['label'].values
test_images = test_data['image'].values
test_labels = test_data['label'].values

train_images = np.array([np.array(img) for img in train_images])
test_images = np.array([np.array(img) for img in test_images])

train_dataset = (train_images, train_labels)
test_dataset = (test_images, test_labels)


# In[ ]:




