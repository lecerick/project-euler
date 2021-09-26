""" Problem #19
-----------------
You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
daysOfWeek = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
def increment(year, month, day):
    # CASE: end of year
    if month==12 and day==31:
        return (year+1, 1, 1)
    # CASE: leap year, end of February
    elif month==2 and (year%4==0 and (year%100!=0 or year%400==0)) and day==29:
        return (year, month+1, 1)
    # CASE: end of month not in a leap year
    elif day==daysInMonth[month]:
        return (year, month+1, 1)
    # CASE: any other day
    else:
        return (year, month, day+1)

year = 1900
month = 1
day = 1
dias = 0
PEcounter = 0
while year < 2001:
    date = str(year).rjust(4,'0')+'/'+str(month).rjust(2,'0')+'/'+str(day).rjust(2,'0')
    dayOfWeek = daysOfWeek[dias % 7]
    if day==1 and dayOfWeek=='Sunday' and year>1900:
        print(date)
        PEcounter+=1
    # print("Dias {}: {}, {}".format(str(dias).ljust(6,' '), dayOfWeek.rjust(10,' '), date))
    newdatetuple = increment(year,month,day)
    year =newdatetuple[0]
    month =newdatetuple[1]
    day =newdatetuple[2]
    dias+=1

print(PEcounter)