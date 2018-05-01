def read_and_process(_df):
	_df = _df.copy()
	_df = _df.drop(columns=['ID','TomorrowRainForecast','DidRainToday','StrongWindDir','MorningWindDir','AfternoonWindDir'])
	_df = _df.fillna(_df.mean())
	return _df
	
def train_classifier():
	pass

def get_predictions():
	pass

def export_csv():
	pass

