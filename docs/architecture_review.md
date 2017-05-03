# Background and context
## What information about your project does the audience need to participate fully in the technical review? You should share enough to make sure your audience understands the questions you are asking, but without going into unnecessary detail.
We are building a price predictor which will allow the user to choose an item and see what is the best time of year for them to buy that item from a price perspective. We are going to be scraping Amazon data for product price history. We plan to use sentiment analysis of reviews to help predict future prices. Assumably negative reviews would be a sign of price decreases in the future. We are going to use machine learning to predict the future prices. Our goal is to have a website that sends an email of when the best time to buy the product is. Some of the machine learning algorithms we are considering are listed below.
* Linear Regression
* Lasso Regression
* Ridge Regression
* Singular Value Decomposition

The background information for each of these algorithms is on our powerpoint.

# Key questions
## What do you want to learn from the review? What are the most important decisions your team is currently contemplating? Where might an outside perspective be most helpful? As you select key questions to ask during the review, bear in mind both the time limitations and background of your audience.
* What machine learning algorithm best fits are need?
* Should we use SVD or Linear Regression or different path?
* Are there any good methods of ensuring our data requests are not confused with a DDOS attack?

# Agenda for technical review session
## Be specific about how you plan to use your allotted time. What strategies will you use to communicate with your audience?
* Give a brief presentation of what our project is and about different machine learning algorithms that we were looking into (no homework!)
* Give sticky notes and ask peers to write down thoughts
* Have an open discussion with our peers about what machine learning algorithm is best for our project
