import datetime
today=datetime.datetime.now()
tomorrow= today + datetime.timedelta(days=1)
yesterday= today - datetime.timedelta(days=1)
print ("Yesterday: ", yesterday.strftime("%Y/%m/%d"))
print ("Today: ", today.strftime("%Y/%m/%d"))
print ("Tomorrow: ", tomorrow.strftime("%Y/%m/%d"))