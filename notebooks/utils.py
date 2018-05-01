import pandas as pd
import numpy as np

def read_and_process(_df):
	_df = _df.copy()
	# solution simple
	_df['AmountRain'] = _df.AmountRain.fillna(-20)
	_df['AmountRain']= _df.apply(amount_rain,axis=1)

	
	_df['MorningHumidity'] = _df.MorningHumidity.fillna(-20)
	_df['MorningHumidity']= _df.apply(morning_humidity,axis=1)
	
	_df['MorningTemp'] = _df.MorningTemp.fillna(-20)
	_df['MorningTemp']= _df.apply(morning_temp,axis=1)

	_df['AfternoonTemp'] = _df.AfternoonTemp.fillna(-20)
	_df['AfternoonTemp']= _df.apply(afternoon_temp,axis=1)

	_df['AfternoonHumidity'] = _df.AfternoonHumidity.fillna(-20)
	_df['AfternoonHumidity']= _df.apply(afternoon_humidity,axis=1)
	

	"""
	_df['Season'] = _df.apply(create_season,axis=1)
	_df_season = _df.groupby(['Season']).median()
		
	"""

	_df = _df.drop(columns=['ID','DidRainToday','AfternoonWindDir','StrongWindDir'])
	
	
	#_df = _df.drop(columns='DaysSinceNewYear')
	#_df = _df.assign(Season=_df['Season'].astype('category'))
	#_df = pd.get_dummies(_df)
	#_df = _df.drop(columns='DaysSinceNewYear')
	
	_df = _df.assign(MorningWindDir=_df['MorningWindDir'].astype('category'))
	_df = pd.get_dummies(_df)

	_df = _df.fillna(_df.median())
	
	_df['diff_temp'] = _df['AfternoonTemp'] - _df['MorningTemp']
	return _df

	
def train_classifier():
	pass

def get_predictions():
	pass

def export_csv():
	pass

def morning_humidity(row):
	if row['MorningHumidity'] != -20:
		return row['MorningHumidity']
	else:
		if row['DidRainToday'] == 'Yes':
			return 87.0
		else:
			return 71.0

def amount_rain(row):
	if row['AmountRain'] != -20:
		return row['AmountRain']
	else:
		if row['DidRainToday'] == 'Yes':
			return 5.4
		else:
			return 0

def afternoon_humidity(row):
	if row['AfternoonHumidity'] != -20:
		return row['AfternoonHumidity']
	else:
		if row['DidRainToday'] == 'Yes':
			return 63.0
		else:
			return 43.0

def afternoon_temp(row):
	if row['AfternoonTemp'] != -20:
		return row['AfternoonTemp']
	else:
		if row['DidRainToday'] == 'Yes':
			return 18.8
		else:
			return 22.35

def morning_temp(row):
	if row['MorningTemp'] != -20:
		return row['MorningTemp']
	else:
		if row['DidRainToday'] == 'Yes':
			return 15.2
		else:
			return 16.00

def create_season(row):
   '''
   0 : winter
   1 : spring
   2 : summer
   3 : autumn
   '''
   if((row['DaysSinceNewYear']>=1) & (row['DaysSinceNewYear'] <=78)):
       return 0
   if((row.DaysSinceNewYear>=79) & (row.DaysSinceNewYear <=171)):
       return 1
   if((row.DaysSinceNewYear>=172) & (row.DaysSinceNewYear <=265)):
       return 2
   if((row.DaysSinceNewYear>=266) & (row.DaysSinceNewYear <=355)):
       return 3
   if((row.DaysSinceNewYear>=356) & (row.DaysSinceNewYear <=365)):
       return 0
   return 0 #default
def replace_na_median_season(row,df,column):
	if not row[column]:
		return row[column]
	else:
		if row['Season'] != np.nan:
			return df.loc[row['Season'],column]
		return 0 
def compute_yesterday_amount_rain(row,df):
	yesterday = row['DaysSinceNewYear']
	if yesterday == 0:
		yesterday = 365
	_df = df[df.DaysSinceNewYear==yesterday]
	return _df.DaysSinceNewYear.median()