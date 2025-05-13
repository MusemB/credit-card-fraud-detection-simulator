import pandas as pd
import pickle

from xgboost import XGBClassifier
with open('xgboost_model.sav', 'rb') as f:
    model = pickle.load(f)


#initializing database # data stream
df = pd.read_csv("simulation_stream_data1.csv")
row_iter = iter(df.itertuples(index=False))

# getting
def fetch():
    output = None
    try:
        incoming = pd.DataFrame(columns=df.columns)
        incoming.loc[len(incoming)] = next(row_iter)

        incoming = incoming.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)
        incoming.to_csv('incoming_data.csv', index=False)
    except StopIteration:
        return
    return output


#transaction database
#incoming= pd.DataFrame(columns=df.columns)
#incoming.loc[len(incoming)] = next(row_iter)

#incoming = incoming.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)
#incoming.to_csv('incoming_data.csv',index=False)

##initializing database
'''
incoming = pd.DataFrame(columns=df.columns)
incoming.loc[len(incoming)] = next(row_iter)
incoming = incoming.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)
incoming.to_csv('incoming_data.csv', index=False)
db= pd.DataFrame(columns=incoming.columns)
db["pred"] = []
db.to_csv('database.csv',index=False)
'''
