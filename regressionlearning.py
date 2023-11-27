import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

mpg = pd.read_csv('mpg.csv')
mpg = mpg.dropna