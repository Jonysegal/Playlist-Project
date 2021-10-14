SECOND_AS_MS = 1000 * 1
MINUTE_AS_MS = SECOND_AS_MS * 60
HOUR_AS_MS = MINUTE_AS_MS * 60
DAY_AS_MS = HOUR_AS_MS * 24

def milliseconds_to_seconds(milliseconds):
    return milliseconds/1000

#Converts milliseconds to format Days, Hours, Minutes, Seconds, Milliseconds. If a time is 24 days 1 hour that means it was total time 25 hours
def milliseconds_to_common_time(milliseconds):
    days, remain = divmod(milliseconds, DAY_AS_MS)
    hours, remain = divmod(remain, HOUR_AS_MS)
    minutes, remain = divmod(remain, MINUTE_AS_MS)
    seconds, remain = divmod(remain, SECOND_AS_MS)
    #Below line isn't necessary; could just return remain as ms here. imo improves code quality
    ms = remain
    return days, hours, minutes, seconds, ms

def readable_time(milliseconds, filterZeros=True):
    days, hours, minutes, seconds, ms = milliseconds_to_common_time(milliseconds)
    days = int_if_int(days)
    hours = int_if_int(hours)
    minutes = int_if_int(minutes)
    seconds = int_if_int(seconds)
    ms = int_if_int(ms)
    toReturn = ""
    if filterZeros:
        if milliseconds == 0:
            return "0 time"
        if days > 0:
            toReturn += f"{days} days, "
        if hours > 0:
            toReturn += f"{hours} hours, "
        if minutes > 0:
            toReturn += f"{minutes} minutes, "
        if seconds > 0:
            toReturn += f"{seconds} seconds, "
        if ms > 0:
            toReturn += f"{ms} milliseconds"
    else:
        toReturn = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds."
    return toReturn

def int_if_int(numb):
    if is_float(numb) and numb.is_integer():
        return int(numb)
    return numb

def is_int(x):
   return type(x) == int

def is_float(x):
    return type(x) == float
