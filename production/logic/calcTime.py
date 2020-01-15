def addTime(*t_tuple:str):
    times = []
    for time in (t_tuple):
        times.append(time.split(":"))
    hours = 0
    minutes = 0
    for i,time in enumerate(times):
        hours += int(time[0])
        minutes += int(time[1])
    
    if minutes >= 0:
        h = int(minutes/60)
    else:
        h = int(minutes/60)
        if not minutes %60 == 0:
            h -= 1

    hours +=h
    minutes =(minutes%60)
    hours = hours%24

    return str(hours).zfill(2) + ":" +str(minutes).zfill(2) # format this!

def substractTime(t1:str,t2:str):
    t2 = t2.split(":")
    t2 = "-"+t2[0]+":-"+t2[1]
    return addTime(t1,t2)