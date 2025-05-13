#loading and cleaning input
import pandas as pd

from sklearn.preprocessing import LabelEncoder

def clean():
    cleaned_data = pd.read_csv('incoming_data.csv')
    #converting all variables to their respectable types
    variables = cleaned_data.columns.tolist()


    #encoder for turning strings into categorical variables
    le = LabelEncoder()
    for var in variables:
        try:
            cleaned_data[var] = cleaned_data[var].astype('float')
        except ValueError:
            cleaned_data[var] = cleaned_data[var].astype('category')

            #turning string columns into categorical variables
            cleaned_data[var] = le.fit_transform(cleaned_data[var])

    cleaned_data.to_csv('cleaned_data.csv',index=False)