---
title: Implementation
layout: template
filename: implementation
--- 
In order to make our code more managable, we essentially divided it into four classes: DataScraper, Formatter, Interpreter, and Visualizer. As these names indicate, the first class grabs the data from the a source online, the Formatter class arranges the data into a dataframe that is then passed into the Interpreter class. This class then uses the data frame and passes it into the model, which predicts values. These values are passed to the Visualizer which creates images of the predicted prices and past prices. The way that the user interacts with our web application is that they chose a product that they want to predict its future price and also select when they want to buy it by. The website then passes these parameters to the other classes, which produce the best time to buy the product based on the requested time period.

The following model demonstrates the layout of our web application. 
<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/SoftDes_ImageClasses.PNG" alt ="" />
The Seasonal Auto Regression Integrated Moving Average (SARIMA) model functions by finding the future prices based on the previous ones. The model requires parameters for the seasonality and for the stationarity parts of our data. For example, electricity prices changes in respect to seasons, meaning that in the summer electricity is more expensive and in the winter it is generally cheaper. So in order to take into account this seasonality, we decomposed the data using seasonal decomposition. Once we had the seasonality trend, we were able to find these parameters to pass into the model. In addition, in order for the model to work, we had to pass parameters where the prices were independent of time, meaning that they were stationary. In order to make the data stationarity, we took the difference between the prices and its previous values. 

Once we had our stationary data and seasonality data, we were able to find the parameters that would go into the model. We needed to determine the number of autoregression terms and lagged forecast errors for both the stationarity and seasonality data. One way to find the number of autoregression terms was by calculating, to the nearest integer, the first moment of the second standard deviation of the autocorrelation function for both the stationary and seasonality data. In order to determine the lagged forecast errors we found the first time the second standard deviation of the partial autocorrelation function was reached. After calculating these values, we now had all the parameters for our model.

The following graphs show the autocorrelation function and partial autocorrelation function for the differenced time series and the seasonality time series. The two dotted lines indicate the second standard deviation away from the mean.

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/acf1stdiff.png" alt ="" /> 

*Autocorrelation function of differenced prices.* 

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/pacf1stdiff.png" alt ="" />


*Partial autocorrelation function of differenced prices.*

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/acfgraph.png" alt ="" />


*Autocorrelation function of seasonality in prices.*

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/pacfgraph.png" alt ="" />


*Partial autocorrelation function of seasonality in prices.*

The Interpreter class then passes the data and its parameters into a SARIMA model which determines the prediction values for the requested amount of days. This data is then passed into the Visualizer which graphs the data, while also returning what day will have the lowest price. The script for our website then calls this function, in order to output the lowest price and the graph to the user.

