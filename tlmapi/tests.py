
import datetime 
import pytz
from datetime import timedelta 
utc_now = pytz.utc.localize(datetime.datetime.utcnow()+ timedelta(days=1))
pst_now = utc_now.astimezone(pytz.timezone('Asia/Bangkok'))
thaidatetime = pst_now.strftime("%Y-%m-%d %H:%M:%S")
thaidatetime2 = pst_now.strftime("%X")

print (type(int(pst_now.time().strftime("%H"))))

import random
print (round((random.random()*200000)+20000,2))

# utc_now_time = pytz.utc.localize()

# print (utc_now_time)



# from datetime import date
# today = date.today()
# print("Today's date:", today)


