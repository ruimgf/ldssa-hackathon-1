# Hackathon #1 - Binary Classification - LDSSA

We have got a final AUC Score of 0.881.

## Objectives
The objective of this hackathon is to predict if it will rain tomorrow. 

## Data Dictionary
- AmountRain: The amount of rainfall recorded for the day in mm;
- StrongWindDir: The direction of the strongest wind gust in the 24 hours to midnight;
- StrongWindSpeed: The speed (km/h) of the strongest wind gust in the 24 hours to midnight;
- MorningWindDir: Direction of the wind at 9am;
- AfternoonWindDir: Direction of the wind at 3pm;
- AfternoonWindSpeed: Wind speed (km/hr) averaged over 10 minutes prior to 3pm;
- MorningHumidity: Humidity (percent) at 9am;
- AfternoonHumidity: Humidity (percent) at 3pm;
- MorningTemp: Temperature (degrees C) at 9am;
- AfternoonTemp: Temperature (degrees C) at 3pm;
- DidRainToday: Yes if precipitation (mm) in the 24 hours to 9am exceeds 1mm, otherwise No;
- DaysSinceNewYear: How many days passed since January 1st of the same year;
- TomorrowRainForecast: 1 if it will rain tomorrow, otherwise 0 (TARGET).

