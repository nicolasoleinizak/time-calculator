def add_time(start, duration, startDay = ""):

    startMinutes = getStartMinutes(start)
    durationMinutes = getDurationMinutes(duration)
    new_time = getEndString(startMinutes+durationMinutes, startDay)


    return new_time

def getEndString (minutes, startDay):
    ending = 'AM'

    minutesToAccount = minutes%1440
    daysLeft = int((minutes-minutesToAccount)/(1440))

    hours = round(minutesToAccount/60)
    minutes = minutesToAccount - hours*60

    if(minutes < 0):
        minutes += 60
        hours -= 1

    if(hours > 12 or (hours == 12 and minutes > 0)):
        hours -= 12
        ending = 'PM'

    if(minutes < 10):
        minutes = '0'+str(minutes)
    
    if(hours == 0):
        hours = 12
        
    
    time = str(hours)+":"+str(minutes)+" "+ending

    if(startDay):
        time += ', ' + getDayOfWeek(daysLeft, startDay)
    
    if(daysLeft == 1):
        time += ' (next day)'
    
    if(daysLeft > 1):
        time += ' (' + str(daysLeft) + ' days later)'
    
    return time

def getDayOfWeek (days, startDay):

    daysOfWeek = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY"
    ]
    startPosition = daysOfWeek.index(startDay.upper())
    finalPosition = (startPosition+days)%7
    return daysOfWeek[finalPosition].capitalize()


def getStartMinutes (time):
    ending = time.split(" ")[1]
    startHours = int(time.split(":")[0])
    if(ending == 'PM'):
        startHours += 12
    startMinutes = int(time.split(":")[1].split(" ")[0])
    return startHours*60 + startMinutes

def getDurationMinutes (time):
    startHours = int(time.split(":")[0])
    startMinutes = int(time.split(":")[1])
    return startHours*60 + startMinutes