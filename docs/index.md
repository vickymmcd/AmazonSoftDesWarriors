---
title: Project Overview
layout: template
filename: index
--- 
     
# Project Overview
We all need gas to heat our homes and fill up our cars. We need electricity to light our houses and power our machines. But wouldn't it be great if you could see how these prices might change throughout the year? That way you could be more aware of when to cut down on driving or power, or even when the best to invest in these markets. Well Super Shoppers, a final project created for Software Design at Olin College in Spring of 2017 will allow you to determine just when the price of any product, including oil and electricity, is cheapest.

In addition to the obvious motivation of saving money, we wanted to explore this particular idea because we wanted to use statistical modeling and machine learning in order to make valuable predictions. This project allowed us to learn about these two topics while also being useful. We implemented a SARIMA model (Seasonal Auto Regression Integrated Moving Average) that takes current price values and fits them based on past price values. How SARIMA works is that it takes in a stationary time series, which was a result of differencing our inputed data time series along with its parameters in addition to differencing the seasonality and finding the parameters for the seasonality of the data. In the end, the model is able to account for the time dependencies and the seasonalities in order to predict future prices.

With this model, our finished project is a website that allows users to enter what product they would like buy and by when they would like to buy it. The website then indicates when will be the cheapest day to buy this particular product. Our main products are oil and electricity since there is the most data for these two products, but any product can be implemented into our model if there is sufficient data. 
