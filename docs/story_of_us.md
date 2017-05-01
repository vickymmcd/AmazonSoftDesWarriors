---
title: The Story of Us
layout: template
filename: story_of_us
--- 

# The Story of us

Sitting at a table in the Software Design studio four first year students put there heads together. "How can we help people?" "How can we learn more about data analysis and user interfaces?" "How do we even code?" They got an idea. What would happen if we analyzed product history data, found trends and predicted the best time of the year to buy a product at its cheapest?

With that the Super Shoppers were born.

At the beginning of the project our intent was to build a price tracker that would scrape Amazon's price data and use a machine learning algorithm to determine probable future prices. We encountered our first problems early on. Amazon and most other major e-commerce sites are highly protective of their price histories, as the data could be used to gain a competetive advantage. We found price data of various Amazon products on the website, Traktor. In order to aquire the data we scraped Traktor's HTML code to find their internal data request forms and reference numbers, so we could send our own data requests to collect all the data in a convenient form. Unfortunately, Traktor has a mechanism in place to avoid this type of exploit; only a certain number of data request per network are allowed per day. This restricted our data collection and it became clear this was not a sustainbable or desirable way of generating the data needed to test our model. This led to a pivot. The internet had years of free easy to access price history data on resources like oil and electicity. The new data could be easily acessed in .csv files, requiring us to develop a new data scraping algorithm. These datasets proved more desirable and effective than the short amazon price histories because they offered many years of data which allowed us to test our predictive model on a longterm span.

A large roadblock came in developing that predictive algorithm. We originally considered using a decision tree or forest for our machine learning algorithm, but found it was unsuitable for finding a numerical, rather than categorical solution. We then looked at linear regression type models. We implemented an algorithm using this method, but we could not linearize our data without destroying most of the interesting trends, and we had insufficient data for most spline or interpolation methods.

We eventually found the predictive method that best matched our needs was ARIMA. ARIMA involves breaking our data into seasonal, trend, and stationary components. ARIMA then analyzes the data, and predicts future patterns. After some experimentation we began using Seasonal ARIMA, or SARIMA. With this model, we were able to make predictions based on past seasonality and trends, which gives our user insight into future prices.


