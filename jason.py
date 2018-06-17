import json
import time
import calendar
import tensorflow

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print (json)


localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)


cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print  (cal)