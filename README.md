# Car Price Predictor

Project link: https://car-price-price.herokuapp.com
Demo Video: https://youtu.be/HEaFU68WAPM

<img src="https://github.com/rajtilakls2510/car_price_predictor/blob/master/demo.png">



# Aim

This project aims to predict the Price of an used Car by taking it's Company name, it's Model name, Year of Purchase, and other parameters.

<img src="https://github.com/rajtilakls2510/car_price_predictor/blob/master/predict.png">

## How to use?

1. Clone the repository
2. Install the required packages in "requirements.txt" file.

Some packages are:
 - numpy 
 - pandas 
 - scikit-learn

3. Run the "application.py" file
And you are good to go. 

# Description

## What this project does?

1. This project takes the parameters of an used car like: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
2. It then predicts the possible price of the car. For example, the image below shows the predicted price of our Hyundai Grand i10. 

<img src="https://github.com/rajtilakls2510/car_price_predictor/blob/master/predict.png">

## How this project does?

1. First of all the data was scraped from Quikr.com (https://quikr.com) 
Link for data: https://github.com/rajtilakls2510/car_price_predictor/blob/master/quikr_car.csv

2. The data was cleaned (it was super unclean :( ) and analysed.

3. Then a Linear Regression model was built on top of it which had 0.92 R2_score.

Link for notebook: https://github.com/rajtilakls2510/car_price_predictor/blob/master/Quikr%20Analysis.ipynb

4. This project was given the form of an website built on Flask where we used the Linear Regression model to perform predictions.

