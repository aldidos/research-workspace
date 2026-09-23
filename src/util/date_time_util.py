import datetime

def to_datetime(date_str) :     
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    return to_datetime_w(date_str, date_format)        

def to_datetime_w(date_str, format) :     
    date_format = format
    date_time = None
    if date_str : 
          date_time = datetime.datetime.strptime(date_str, date_format)        
    return date_time    

def time_diff(f : datetime, t : datetime) : 
    if f == None or t == None : 
        return 0
    
    diff = t - f
    return diff.seconds