%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from interpret_data import Interpreter
from sklearn.pipeline import make_pipeline
from statsmodels.tsa.stattools import acf, pacf

lag_acf = acf(ts_log_diff, nlags = 20)
myinterpreter = Interpreter("", 'phone_data.txt', 'phone.txt', 10)
