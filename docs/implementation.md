---
title: Implementation
layout: template
filename: implementation
--- 
In order to make our code more managable, we essentially divided into four classes: DataScraper, Formatter, Interpreter, and Visualizer. As these names indicate, the first class grabs the data from the a source online, the Formatter class prevents and arranges the data into a dataframe that is then passed into an Interpreter class, which finds the paramters of the model by plotting the autocorrelation functions (ACF) and the partial autocorrelation functions (PACF). The Interpreter class then passes the data and its parameters into a SARIMA model which determines the prediction values for the wanted amount of days. This data is then passed into the Visualizer which then graphs the data, while also returning what day will have the lowest price. Our script for our website then calls upon this function, in order to output the lowest price and the graph to the user.

The following model demonstrates the layout of our web application. 
<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/SoftDes_ImageClasses.PNG" alt ="" />