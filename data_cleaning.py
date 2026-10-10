"""
Data Cleaning Process:

Data columns and their reviews:
* "First Name" (type: str) - First name of the client
* "Last Name" (type: str) - Last name of the client
* "Postal Code" (type: str) - Zipcode of client
* "NUMBER OF SENIORS (AGE 55 AND ABOVE)" (type: float64) - Num of seniors in home
* "NUMBER OF ADULTS (AGE 18-54)" (type: float64) - Num of adults in home
* "NUMBER OF YOUTH (AGE 4-17)" (type: float64) - Num of children in home
* "NUMBER OF BABIES (AGE 3 AND UNDER)" (type: float64) - Num of babies in home
* "HOUSEHOLD SIZE" (type: str) - Num of people in home
* "GENDER" (type: str) - MF
* "Conversion Date" (type: str) - Date and time when registered
* "Conversion Title" (type: str) - Platform of registrarion - all are 'Form'
* "Contact first name" (type: str) - First name of the client
* "Contact last name" (type: str) - Last name of the client
"""
##### Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, re

##### Data Loading
DATA_PATH = os.path.join(
    os.getcwd(),
    'Data'
)
df = pd.read_csv(f'{DATA_PATH}/food_raw.csv')

##### Formatting headers
formatted = []
for col in df.columns:
    col_str = str(col)
    col_str = col_str.strip().replace(" ", "_")
    col_str = col_str.lower()
    col_str = col_str.split('_(')[0]
    formatted.append(col_str)
df.columns = formatted

##### Fixing First and Last names
def val_and_format(name:str):
    if pd.isna(name): return None
    one_only = name.split(' ')[0]
    if re.fullmatch(r'[A-Za-z\-]+', one_only):
        return one_only.capitalize()
    else: return None

df['first_name'] = df['first_name'].apply(val_and_format)
df['last_name'] = df['last_name'].apply(val_and_format)

##### Zip-code, ensuring all are int and 5 digits long
def fix_zip(zip_val: str):
    try: 
        zip = int(float(zip_val))
        return zip if 9999 < zip < 99999 else None
    except: return None

df['postal_code'] = df['postal_code'].apply(fix_zip).astype('Int64')

##### Convertir 'x-y people' into average(x,y)
mapping = {
    '1-2 People': 1.5,
    '3-4 People': 3.5,
    '5-6 People': 5.5,
    'More than 6 people': 7
}

df['household_size'] = df['household_size'].map(mapping).astype(float)

##### Date-time column
df['conversion_date'] = pd.to_datetime(
    df['conversion_date'],
    format="%m/%d/%Y %H:%M",
    errors="raise"
)

##### Deleting last 3 cols
    # Reasons
        # Last 2 are duplicated from first 2
        # Last 3rd is all 'Form'
df = df[df.columns[:-3]]

##### Saving data
df.to_csv(f'{DATA_PATH}/food_clean.csv')