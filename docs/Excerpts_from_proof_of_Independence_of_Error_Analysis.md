# Meaning of Independence of Errors
- This is an assumption in regression models that the error terms (residuals) are statistically independent from one another.
- If residuals are correlated (which means autocorrelation is present), it can suggest that the model is missing some important information or structure, such as a variable that captures the effect causing the autocorrelation.
- Violation of this assumption can lead to inefficient estimates and issues with hypothesis testing, potentially misleading conclusions about the relationship between the variables of interest.

When the Independence of Errors assumption holds, the residuals from one observation do not provide any information about the residuals of another observation. When it is violated due to autocorrelation, it means that past errors could influence or predict the current error, which is problematic for the statistical properties of the estimators in a regression model.


### Steps taken to prove assumption
In order to prove that the residuals are independent of each other, I needed to build a Linear model to have access to the residuals.
The process of Feature engineering invloved encoding all the categorical columns in the dataset to numerical in order to fit it into the model object. The only categorical column in this case is the `Location` column in the cleaned dataset.

The `Location` contained over **800** unique categories. Using One-Hot Encoding or calling pandas's `get_dummy()` method would lead to many columns which will lead to the curse of High Dimensionality.
I decided to create a function that groups the columns that contain less than 1% of the observations in the dataset into a single category-`Others`.

After the grouping process, I called the `get_dummy()` method on the dataset, setting the `drop_first` parameter to `True`.

#### Model of choice
I opted to using the `statsmodels` package, this is because statsmodels excels in its support for hypothesis testing, offering a variety of functions to perform different statistical tests. This makes it an excellent tool for inferential statistics, where hypothesis testing plays a central role.

I trained the encoded dataframe with an Ordinal Least Square (OLS) Model, this choice was fueled by the availability of a pre-writted method that performs the `Durbin-Watson` Test on the models residuals. 


#### Interpreting the Durbin-Watson Statistic:
- A Durbin-Watson statistic close to 2.0 suggests no autocorrelation.
- Values approaching 0 indicate positive autocorrelation.
- Values approaching 4 indicate negative autocorrelation.

**The Result of the `Durbin-Watson` test indicates no autocorrelation in the residuals of the model. Therefore, I fail to reject the null hypothesis of no autocorrelation between the residuals.**

**This result implies that the residuals from the regression model are independent of each other, satisfying one of the critical assumptions of the OLS regression.**