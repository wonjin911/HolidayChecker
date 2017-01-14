from datetime import date as dt
from datetime import timedelta as td

HOLIDAY = 2
MIN_TRAVEL_DAY = 5

HOLIDAY_LIST = \
    [ \
        dt(2017, 1, 1) \
        , dt(2017, 1, 27) \
        , dt(2017, 1, 30) \
        , dt(2017, 3, 1) \
        , dt(2017, 5, 1) \
        , dt(2017, 5, 3) \
        , dt(2017, 5, 5) \
        , dt(2017, 6, 6) \
        , dt(2017, 8, 15) \
        , dt(2017, 10, 3) \
        , dt(2017, 10, 4) \
        , dt(2017, 10, 5) \
        , dt(2017, 10, 6) \
        , dt(2017, 10, 9) \
        , dt(2017, 12, 25) \
        , dt(2018, 1, 1)
    ]

def isBreak(a):
    if (a.isoweekday() in (6,7)):
        return True
    elif a in HOLIDAY_LIST:
        return True
    else:
        return False

today = dt.today()
print today
print today.isoweekday()

# Start From 30 days ago
startDate = today + td(days=-30)
endDate = startDate + td(days=365)

print "Check from %s to %s" % (startDate, endDate)

straightBreak = 0
holidayLeft = HOLIDAY
checkStartDate = startDate
result = []
while(checkStartDate <= endDate):
    #print "%s check started" % (checkStartDate)
    currentDate = checkStartDate
    while(currentDate <= endDate):
        if isBreak(currentDate):
            #print "%s is break!!" % currentDate
            straightBreak += 1
            currentDate += td(days=1)
        elif (holidayLeft > 0):
            #print "%s use holiday!!" % currentDate
            straightBreak += 1
            holidayLeft -= 1
            currentDate += td(days=1)
        else:
            if(straightBreak >= MIN_TRAVEL_DAY):
                print "Found a super break!! \n %s ~ %s (%d days)" % (checkStartDate,currentDate,straightBreak)
            break
    straightBreak = 0
    checkStartDate += td(days=1)
    holidayLeft = HOLIDAY


