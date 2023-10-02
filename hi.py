import datetime

date = str(datetime.datetime.now())
lenToCut = len(date) - 7
date = date[0:lenToCut]
