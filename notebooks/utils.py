import pandas as pd
import numpy as np

def read_and_process(_df):
	_df = _df.copy()

	_df['AmountRain']= _df[_df.DidRainToday=='Yes']['AmountRain'].replace(to_replace=np.nan,value=5.4)
	_df['AmountRain']= _df[_df.DidRainToday=='No']['AmountRain'].replace(to_replace=np.nan,value=0)
	_df['Season'] = _df.apply(create_season,axis=1)
	_df_season = _df.groupby(['Season']).median()
	
	_df = _df.drop(columns=['ID','DidRainToday','AfternoonWindDir','StrongWindDir'])
	
	
	#_df = _df.drop(columns='DaysSinceNewYear')
	#_df = _df.assign(Season=_df['Season'].astype('category'))
	#_df = pd.get_dummies(_df)
	#_df = _df.drop(columns='DaysSinceNewYear')
	
	_df = _df.assign(MorningWindDir=_df['MorningWindDir'].astype('category'))
	_df = pd.get_dummies(_df)
	_df['MorningTemp'] = _df.apply(replace_na_median_season,args=(_df_season,'MorningTemp'),axis=1)
	#_df['AfternoonTemp'] = _df.apply(replace_na_median_season,args=(_df_season,'AfternoonTemp'),axis=1)
	#_df['MorningHumidity'] = _df.apply(replace_na_median_season,args=(_df_season,'MorningHumidity'),axis=1)
	#_df['AfternoonHumidity'] = _df.apply(replace_na_median_season,args=(_df_season,'AfternoonHumidity'),axis=1)

	_df = _df.fillna(_df.median())
	#_df['yesterday_rain'] = _df.apply(compute_yesterday_amount_rain,args=(_df,),axis=1)
	
	_df['diff_temp'] = _df['AfternoonTemp'] - _df['MorningTemp']
	#_df = _df.drop(columns=['AfternoonTemp','MorningTemp'])
	return _df

	
def train_classifier():
	pass

def get_predictions():
	pass

def export_csv():
	pass

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