import data_stream
import pandas as pd
model = data_stream.model

def classify():

    df = pd.read_csv('cleaned_data.csv')
    db = pd.read_csv('database.csv')
    db_data = pd.read_csv('incoming_data.csv')
    data_in = df
    data_in = data_in.drop(["is_fraud"], axis=1)

    pred = model.predict(data_in)

    db_data['pred'] = pred

    db.loc[len(db)] = db_data.iloc[0]

    db.to_csv('database.csv',index=False)
