# BENGALURU HOUSE PRICE PREDICTION

## Overview

This project aims to develop a regression model for predicting house prices in Bengaluru, India. The dataset used for this project is sourced from Kaggle and contains information about various factors that may influence house prices in the Bengaluru real estate market.

## Project Details
The dataset used in this project is sourced from Kaggle and contains the following features:

- area_type: Name of the area where the property is situated.
- location: Location of the property in Bengaluru.
- rooms: Number of rooms in the property.
- bathrooms: Number of bathrooms in the property.
- price: Price of the property (target variable).
- total_sqft: Total squarefoot of the property
- ... (other relevant features)

## Project Description:

### Objective

The main objective of this project is to develop a regression model that accurately predicts house prices in Bengaluru based on the available features. By leveraging machine learning techniques, we aim to provide valuable insights to potential homebuyers and stakeholders in the real estate industry.

### Assumptions
#### Linearity:
- **Assumption**: The relationship between the house prices (dependent variable) and the predictors (independent variables) is linear.
- **Why It's Important**: Ensures that changes in predictor variables have a consistent effect on the dependent variable.
- **How to Check**: Create scatter plots of house prices against each predictor variable and look for a linear pattern. Additionally, plotting residuals versus predicted values can help identify non-linearity.
- **Responsibility**: Investigate the linearity assumption by visualizing and statistically testing the relationships between house prices and predictor variables.

#### Independence of Errors: 
- **Assumption**: The residuals (errors) from the regression are independent of each other.
- **Why It's Important**: Ensures that the error term for one observation is not influenced by the error term of any other observation, which is critical for the reliability of standard errors, confidence intervals, and hypothesis tests.
- **How to Check**: Look for patterns in residual plots over time or order of data collection, or use statistical tests like the Durbin-Watson test for time series data.
- **Responsibility**: Confirm that there’s no autocorrelation in the residuals, especially important in time series data or if the data have a spatial component.

#### Homoscedasticity:
- **Assumption**: The variance of the error terms (residuals) is constant across all levels of the independent variables.
- **Why It's Important**: Variances of the error terms should be equal across values of the independent variables to ensure uniform prediction accuracy.
- **How to Check**: Plot residuals against predicted values or independent variables to look for patterns; ideally, the spread of residuals should be uniform (no funnel shapes).
- **Responsibility**: Verify the assumption of homoscedasticity and explore transformations or adjustments if variances are unequal.

#### Normal Distribution of Errors: 
- **Assumption**: The residuals of the model are normally distributed.
- **Why It's Important**: This assumption underpins the validity of various statistical tests, including hypothesis tests on the regression coefficients.
- **How to Check**: Use Q-Q plots of residuals or conduct a Shapiro-Wilk test.
- **Responsibility**: Assess the distribution of residuals and apply transformations if necessary to achieve normality.

#### No or Little Multicollinearity:
- **Assumption**: Independent variables are not too highly correlated with each other.
- **Why It's Important**: High multicollinearity can make it difficult to determine the individual effect of each predictor on the outcome.
- **How to Check**: Calculate the correlation matrix and Variance Inflation Factor (VIF) for the predictor variables.
- **Responsibility**: Identify and address multicollinearity among predictors such as living area, number of rooms, location scores, etc., possibly removing or combining highly correlated variables.

## Getting Started

### Installation
To run this project locally, you'll need Python and the following libraries:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn


