from datetime import datetime



now = datetime.now()

# Current time stamp
print now
# Current year 
print now.year
# Current month
print now.month 
# Current day
print now.day

print "Date in mm/dd/yyyy"
print '%s/%s/%s' % (now.month, now.day, now.year)
print "Time in hh:mm:ss"
print '%s:%s:%s' % (now.hour, now.minute, now.second)
print "Datetime in mm/dd/yyy hh:mm:ss format"
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)



