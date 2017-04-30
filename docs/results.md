---
title: Results
layout: template
filename: results
--- 

# Results
For our project we created a website deployed on heroku which predicts future prices for various items using a seasonal ARIMA predictive model. Seasonal trends occur when there is a repeating pattern of an item being more expensive at a certain time of year. For example, winter coats would be more expensive in the winter than in the summer. Overall trends occur when the price of an item tends to go up or down as the years go by. We used seasonality and trends in items to determine when the best time for a person to buy a certain product is both in terms of seasonal and overall trend variations. We struggled to find sufficient data for Amazon products to make our model work, but we were able to demonstrate that our model was working by fitting and forecasting fake data on a product which has prices that change specifically with the season. 

Our model outputs a visualization of the price graph. We included a hover tool which shows what the price is, the date that that price occurred, and whether that price is within 10% of the cheapest price. Also, when it is one of the cheapest prices, it shows up in red instead of green or blue. This way people's eyes are immediately drawn to when the best time for them to buy a certain product is and they are able to see all the information in a understandable and easy to digest way. 

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/homepage.png" alt ="" />

*This is a screenshot of our user interface website home page.*

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/pricehistory.png" alt ="" />

*This is the output of our model with limited data we were able to collect and format from Amazon. Blue represents our model's price forecast. Green and red represents the original price history of the item.*

<img src="https://raw.githubusercontent.com/vickymmcd/AmazonSoftDesWarriors/master/images/predictionfake.png" alt ="" />
*This is the output of our model when we used fake data that was made to be perfectly seasonal. Green is the data we inputted and blue is the prediction our model outputted.*

<img src= "https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/model_fit.png" alt ="" />

<img src= "https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/prediction_hist.png" alt ="" />

<img src= "https://github.com/vickymmcd/AmazonSoftDesWarriors/blob/master/images/forecast.png" alt ="" />



