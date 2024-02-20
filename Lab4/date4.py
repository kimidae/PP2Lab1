import datetime
dayfirst_str=input()
daysecond_str=input() 
dayfirst=datetime.datetime.fromisoformat(dayfirst_str)
daysecond=datetime.datetime.fromisoformat(daysecond_str)
timedate_delta=dayfirst-daysecond
print (timedate_delta.total_seconds())