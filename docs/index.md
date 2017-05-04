---
title: Project Overview
layout: template
filename: index
--- 
     
# Project Overview
We all need gas to heat our homes and fill up our cars. We need electricity to light our houses and power our machines. But wouldn't it be great if you could see how these prices might change throughout the year? That way you could be more aware of when to cut down on driving or when to reduce your electricity consumption, in addition to determining when it might be the best time to buy stock in these markets. Well Super Shoppers, a final project created for Software Design at Olin College in Spring of 2017 will allow you to determine just when the price of any product, including oil and electricity, is cheapest.

In addition to the obvious motivation of saving money, we wanted to explore this particular idea because we wanted to use statistical modeling and machine learning in order to make valuable predictions. We implemented a SARIMA model (Seasonal Auto Regression Integrated Moving Average) that takes current price values and fits them based on past price values. How SARIMA works is that it takes in a time series along with the parameters of the stationary time series and of the seasonality time series. In the end, the model is able to account for the time dependencies and the seasonalities in order to predict future prices.
    
With this model, our finished project is a website that allows users to investigate resources such as oil and electricity. With more data on product price history this website can be easily expanded to display the prices for any product. When the user interacts with the website they choose a product that they would like to learn more about. The website then indicates the cheapest days to buy this particular product.
