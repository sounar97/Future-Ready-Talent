# Future-Ready-Talent
Bike Rentals Prediction Using Azure Automated ML and Hosting on STATIC WEB SERVICES
# Bike Rental Prediction

This project is aimed at predicting bike rental demand using machine learning techniques. It leverages Azure AutoML, Linear Regression, and the MaxAbsScaler and XGBoostRegressor algorithms to make accurate predictions.

## Overview

Bike rental companies often face challenges in managing their bike fleets efficiently. Demand for bike rentals can vary based on several factors, including weather conditions, holidays, and time of day. This project uses machine learning to forecast bike rental demand, enabling the company to optimize operations and provide better services to its customers.

## Key Components

### Azure AutoML

Azure AutoML is a powerful tool for automating the machine learning model selection and tuning process. In this project, Azure AutoML is used to explore various algorithms and preprocessing techniques to find the best model for bike rental prediction.
![I have fetched the data for traing through the API from Microsoft ](https://github.com/sounar97/Future-Ready-Talent/blob/3cecb4481f0ff6475f4657562a13c0a071288008/Screenshot%202023-07-22%20005940.png)

### I have fetched the data for training through the API from Microsoft

### Linear Regression

Linear Regression is a fundamental machine learning algorithm used for predicting numeric values. It forms the basis of our bike rental prediction model, helping us understand how different features (e.g., temperature, time of day) impact rental demand.
![Alt Text](https://github.com/sounar97/Future-Ready-Talent/blob/b54c2bfee84123c4d556ad6f4a6c90625fd6184e/Screenshot%202023-07-22%20013227.png)
![Alt Text](https://github.com/sounar97/Future-Ready-Talent/blob/b54c2bfee84123c4d556ad6f4a6c90625fd6184e/Screenshot%202023-07-22%20013010.png)
### I have Automated ML service to add linear regression to the data


### MaxAbsScaler

The MaxAbsScaler is a preprocessing technique used to scale features to a range between -1 and 1. This normalization method is applied to ensure that all features have a similar influence on the prediction, preventing any feature from dominating the model.

### XGBoostRegressor

XGBoost (Extreme Gradient Boosting) is a powerful machine learning library known for its effectiveness in regression tasks. The XGBoostRegressor algorithm is employed to build a robust prediction model, fine-tuned for bike rental demand forecasting.
![Alt Text](https://github.com/sounar97/Future-Ready-Talent/blob/b54c2bfee84123c4d556ad6f4a6c90625fd6184e/Screenshot%202023-07-22%20013455.png)

### The Automated ML as have finalised MaxAbsScaler and XGBoostRegressor as the best suited algorithm for above data after training

![Alt Text](https://github.com/sounar97/Future-Ready-Talent/blob/b54c2bfee84123c4d556ad6f4a6c90625fd6184e/Screenshot%202023-07-22%20015119.png)

### I have fetched the API to connect it for my WEB application to interact dynamically

## Getting Started

To run this project locally or explore the code and data, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   https://github.com/sounar97/Future-Ready-Talent.git

2.Access the project link by clicking below:

  https://bike-rentals.azurewebsites.net/
