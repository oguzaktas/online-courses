# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.day_name()

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())

'''
Output:
Ride start weekday
Friday       724.5
Monday       810.5
Saturday     462.0
Sunday       902.5
Thursday     652.0
Tuesday      641.5
Wednesday    585.0
Name: Duration, dtype: float64
'''