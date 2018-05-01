import pandas as pd
def read_and_process(_df):
	_df = _df.copy()
	_df = _df.drop(columns=['ID','DidRainToday','AfternoonWindDir','StrongWindDir'])
	#_df = _df.drop(columns='DaysSinceNewYear')
	#_df = _df.assign(Season=_df['Season'].astype('category'))
	#_df = pd.get_dummies(_df)
	#_df = _df.drop(columns='DaysSinceNewYear')
	_df = _df.assign(MorningWindDir=_df['MorningWindDir'].astype('category'))
	
	
	_df = pd.get_dummies(_df)
	_df = _df.fillna(_df.median())
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

def compute_yesterday_amount_rain(row,df):
	yesterday = row['DaysSinceNewYear']
	if yesterday == 0
	return df[df.DaysSinceNewYear==]