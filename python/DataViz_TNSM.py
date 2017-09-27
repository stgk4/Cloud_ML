import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

#visualize the important characteristics of the dataset
import matplotlib.pyplot as plt 

#step1: download the data
df_dataset = pd.read_csv("https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv")
num_rows = df_dataset.shape[0]


print("done....")
