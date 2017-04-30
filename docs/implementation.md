---
title: Implementation
layout: template
filename: implementation
--- 
In order to make our code more managable, we essentially divided it into four classes: DataScraper, Formatter, Interpreter, and Visualizer. As these names indicate, the first class grabs the data from the a source online, the Formatter class arranges the data into a dataframe that is then passed into the Interpreter class.

The following model demonstrates the layout of our web application. 
<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/SoftDes_ImageClasses.PNG" alt ="" />

The Seasonal Auto Regression Integrated Moving Average (SARIMA) model functions by finding the future prices based on the previous ones. The model requires parameters for the seasonality and for the stationarity parts of our data. Since electricity prices changes in respect to seasons, meaning that in the summer electricity is more expensive and in the winter it is generally cheaper, the model takes out this pattern. In addition, in order for the model to work, the prices need to be independent of time, which means that it must be stationary. In order to make the data stationarity, we took the difference between the prices and its previous values. We decomposed the data using seasonal decomposition to remove all seasonality.

Once we had our stationary data and seasonality data, we were able to find the parameters that would go into the model. We needed to determine the number of autoregression terms, which can be found through the second standard deviation of the autocorrelation function. We also needed to determine the lagged forecast errors which we determined in the same method as previously, except we used the partial autocorrelation functions.

The following graphs show the autocorrelation function and partial autocorrelation function for the differenced time series and the seasonality time series.

<img src="https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/acf1stdiff.png" alt ="" />
<img src="https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/pacf1stdiff.png" alt ="" />
<img src="https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/acfgraph.png" alt ="" />
<img src="https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/pacfgraph.png" alt ="" />

The Interpreter class then passes the data and its parameters into a SARIMA model which determines the prediction values for the requested amount of days. This data is then passed into the Visualizer which graphs the data, while also returning what day will have the lowest price. The script for our website then calls this function, in order to output the lowest price and the graph to the user.

