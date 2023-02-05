import pandas as pd


#loading the JSON files -- Orient/lines params definition --> "https://pandas.pydata.org/docs/reference/api/pandas.read_json.html"
portfolio = pd.read_json('Data/portfolio.json', orient='records', lines=True)
profile = pd.read_json('Data/profile.json', orient='records', lines=True)
transcript = pd.read_json('Data/transcript.json', orient='records', lines=True)
#print(portfolio)
#print(profile)
#print(transcript)