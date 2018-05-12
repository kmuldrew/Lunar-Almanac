def month_name(i):
    return {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
    }[i]

def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sun.', 
              'M.', 
              'Tu.', 
              'W.', 
              'Th.',  
              'F.', 
              'Sa.']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return week[int(dayOfWeek)]

def days_in_month(month):
    return {
        1:31,3:31,5:31,7:31,8:31,10:31,12:31,
        4:30,6:30,9:30,11:30,
        2: 28,
    }[month]

def day_of_week(date):
    dow = math.trunc(date - 0.5) % 7 + 3
    if (dow > 7): dow = dow - 7
    if (dow == 2): return('M. ')
    elif (dow == 3): return('Tu.')
    elif (dow == 4): return('W. ')
    elif (dow == 5): return('Th.')
    elif (dow == 6): return('F. ')
    elif (dow == 7): return('Sa.')
    elif (dow == 1): return('Sun.')
    else: return('Q. ')

def night_time(month,hour):
    dark = False
    if ((month == 1) or (month == 11) or (month == 12)):
        if ((hour >= 1) and (hour <= 7)): dark = True
    elif (month == 2):
        if ((hour >= 2) and (hour <= 7)): dark = True
    elif ((month == 3) or (month == 4) or (month == 9) or (month == 10)):
        if ((hour >= 2) and (hour <= 6)): dark = True
    else:
        if ((hour >= 3) and (hour <= 5)): dark = True
    return(dark)


