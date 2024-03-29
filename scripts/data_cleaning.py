import pandas as pd
import numpy as np
import seaborn as sns



def wrangle(filepath):
    '''
    Wrangles the data in the specified CSV file to prepare it for analysis.

    Parameters:
    - filepath (str): The file path to the CSV file containing the data.

    Returns:
    - DataFrame: A cleaned and processed DataFrame ready for analysis.

    Steps:
    1. Reads the CSV file into a DataFrame.
    2. Drops columns with less useful information (society, availability, area_type).
    3. Splits the "size" column into "House_size" and "house_ppty" columns, converting to float.
    4. Drops the "size" and "house_ppty" columns.
    5. Checks for multicollinearity among numeric columns.
    6. Cleans the "total_sqft" column by converting strings to floats, handling ranges, and removing null values.
    7. Drops outliers based on quantiles for "House_size", "new_total_sqft", "price", and "bath" columns.
    8. Drops rows with null values in the "location" column.
    9. Calculates the average of the "balcony" column and fills null values with the average.

    Note:
    - This function assumes a specific structure and format of the input CSV file.
    - It performs data cleaning, outlier removal, and handling of missing values to prepare the data for analysis.

    
    '''
    df = pd.read_csv(filepath)
    
    #drop columns with less useful information
    df.drop(columns=['society', 'availability', 'area_type'], inplace=True)
    
    #split column "size" 
    df[["House_size", "house_ppty"]] = df["size"].str.split(" ", n=1, expand=True).astype({0: float})
    
    #drop size column and house_type
    df.drop(columns=["house_ppty","size"], inplace=True)
    
    #checking for multicollinearity 
    corr = df.select_dtypes("number").corr()
    
    
    # Cleaning total_sqft column by splitting,averaging
    #the rows where necessary and removing null.
    
    total_sqft_int = []

    for val in df['total_sqft']:
        try:
            total_sqft_int.append(float(val))
        except:
            try:
                val = val.split('-')
                total_sqft_int.append((float(val[0]) + float(val[1])) / 2)  
            except:
                total_sqft_int.append(np.nan)

    # join new integer column
    df = df.join(pd.DataFrame({'new_total_sqft':total_sqft_int}))

    #convert the column to float
    df["new_total_sqft"] = df["new_total_sqft"].astype(float)
    
    #Dropping the outliers
    low, high = df["House_size"].quantile([0.1, 0.9])
    mask_bath = df["House_size"].between(low, high)
    df = df[mask_bath]
    
    low, high = df["new_total_sqft"].quantile([0.1, 0.9])
    mask_new_tot = df["new_total_sqft"].between(low, high)
    df = df[mask_new_tot]
    
    low, high = df["price"].quantile([0.1, 0.9])
    mask_price = df["price"].between(low, high)
    df = df[mask_price]
    
    low, high = df["bath"].quantile([0.1, 0.9])
    mask_bath = df["bath"].between(low, high)
    df = df[mask_bath]
    
    # Dropping null values in location column
    df.dropna(subset=['location'], inplace=True, axis=0)
    
    # Finding average of balcony column and inputing the average inplace of na

    df['balcony'] = df['balcony'].fillna(df["balcony"]).mean().round()
    df.drop(columns=["total_sqft"], inplace=True)
    
    
    return df
    