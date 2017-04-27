---
title: The Story of Us
layout: template
filename: story_of_us
--- 

# The Story of us

We initially planned on using a machine learning algorithm-

At the beginning of the project our intent was to biuld a price tracker that would scrape Amazons price data and use a machine learning algorithm to determine probable future prices. We encountered our first problems early on. Amazon and most other major e-commerce sites are highly protective of their price histories, as the data could be used to gain a competetive advantage. We found that the price data was on a website called Traktor, but was not made available freely. In order to aquire the data we scraped Traktors HTML code to find their internal data request forms and reference numbers, so we could send our own data requests to collect all the data in a convenient form. Unfortunately, Traktor has a mechanism in place to avoid this type of exploit; only a certain number of data request per network are allowed per day. After a period of several days Traktor will remove a network from their blacklist, but the amount of data we could gather was restricted.

The second difficulty we encountered was in our predictive algorithm. We originally considered using a decision tree or forest for our machine learning algorithm, but found it was unsuitable for finding a numerical, rather than categorical, solution. We then looked at linear regression type models. We implemented an algorithm using this method, but we could not linearize our data without destroying most of the interesting trends, and we had insufficient data for most spline or interpolation methods.

We eventually found that the predictive method that best matched our needs was ARIMA, which involved looking 

finding price histories is hard, Traktor costs money unless you trick it-

Switch to different machine learning algorithm-

Get data collection working-

got formatting mostly working-

Got an early version of interpreter, but without predictive capabilities-

Found out about seasonality and stuff-

Started graphing using Bokeh-

Implemented ARIMA, mostly-

Changed to using SARIMA-

Started working with different data sources for longer histories-
