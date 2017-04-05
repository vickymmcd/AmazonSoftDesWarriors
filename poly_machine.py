%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from interpret_data import Interpreter
from sklearn.pipeline import make_pipeline

myinterpreter = Interpreter("", 'phone_data.txt', 'phone.txt', 10)
