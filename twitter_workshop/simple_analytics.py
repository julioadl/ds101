import pandas as pd
import json

#Input the name of your file here
data = json.load(open('name of your file here'))

#Get your data into lists
time = []
hashtags = []
screen_names = []

for tweet in data['tweets']:
	#Remember to get the timestamp as an integer
	time.apend(int(tweet['timestamp_ms']))
	screen_names.append(tweet['user']['screen_name'])

#For Hashtags the data may not be already there. Use try
for tweet in data['tweets']:
	try:
		hashtags.append(tweet['entities']['hashtags'][0]['text'])
	except:
		pass

#Build your dataframes
ts = pd.DataFrame({'time':time})
hashtags = pd.DataFrame({'hashtags': hashtags})
screen_names = pd.DataFrame({'screen_name': screen_names})

#Format your time
ts.time = pd.to_datetime(ts.time, unit='ms')
ts = ts.map(lambda x:x.strftime("%Y-%m-%d"))
date = ts.value_counts().index
frequency = ts.value_counts().values
ts = pd.DataFrame({'date':date, 'frequency': frequency})
ts.index = ts.date
ts = ts.sort()

#Hashtags
hashtags = hashtags.hashtags.value_counts().index
count = hashtags.hashtags.value_counts().values
hashtags = pd.DataFrame({'hashtags':hashtags, 'count':count})

#Screen name
sn = screen_names.screen_name.value_counts().index
count = screen_names.screen_name.value_counts().values
sn = pd.DataFrame({'sn':sn, 'count':count})


