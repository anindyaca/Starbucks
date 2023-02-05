import pandas as pd
import numpy as np
import math
import json
from sklearn.preprocessing import LabelEncoder
from matplotlib import pyplot
import matplotlib.pyplot as plt
import warnings

from preprocessing_helper import encode_person_id, encode_offer_id, convert_data_type, encode_channel
import progressbar
warnings.filterwarnings(action='once')

#loading the JSON files -- Orient/lines params definition --> "https://pandas.pydata.org/docs/reference/api/pandas.read_json.html"
portfolio = pd.read_json('Data/portfolio.json', orient='records', lines=True)
profile = pd.read_json('Data/profile.json', orient='records', lines=True)
transcript = pd.read_json('Data/transcript.json', orient='records', lines=True)
#print(portfolio)
#print(profile)
#print(transcript)