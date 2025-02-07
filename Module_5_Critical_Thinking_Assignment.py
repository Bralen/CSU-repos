import pandas as pd
import statistics
yearCount = int(input("How many years would you like to calculate?"))
Months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
df=pd.DataFrame(columns=['Year','Month','Rainfall'])
rainfall = 0
for year in range(0,yearCount):
    for month in Months:
        rainfall = float(input(f'What was the rainfall for {month} in year {year + 1}?'))
        newData = pd.DataFrame({'Year':[year + 1],'Month':[month],'Rainfall':[rainfall]})
        df=pd.concat([df,newData],ignore_index = True)

monthCount = df.shape[0]
totalRainfall = sum(df.Rainfall)
avgRainfall = statistics.mean(df.Rainfall)
print(f'{monthCount} months were entered.')
print(f'The total rainfall is {totalRainfall} inches.')
print(f'The average rainfall for the entire period is {avgRainfall} inches.')



booksPurchased = int(input("How many books have you purchased this month?"))
if booksPurchased >= 8:
    print('You have earned 60 points.')
elif booksPurchased >= 6:
    print('You have earned 30 points.')
elif booksPurchased >= 4:
    print('You have earned 15 points.')
elif booksPurchased >= 2:
    print('You have earned 5 points.')
else:
    print('You have earned 0 points.')
