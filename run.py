import subprocess
import main
import data_stream
import pandas as pd
#resetting transaction history database
df = pd.read_csv("simulation_stream_data1.csv")
row_iter = iter(df.itertuples(index=False))
incoming = pd.DataFrame(columns=df.columns)
incoming.loc[len(incoming)] = next(row_iter)
incoming = incoming.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)
incoming.to_csv('incoming_data.csv', index=False)
db= pd.DataFrame(columns=incoming.columns)
db["pred"] = []
db.to_csv('database.csv',index=False)

subprocess.Popen(['python','simulation.py'])

#uncomment below to run locally
#main.app.run(debug=True)

#uncomment below to run with docker
#main.app.run(host="0.0.0.0", port=8050, debug=True)