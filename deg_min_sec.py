def dms_str(label,Decimal):
    d = int(Decimal)
    m = int((Decimal - d) * 60)
    s = (Decimal - d - m/60) * 3600.00
    z= round(s, 2)
    if d >= 0:
        print(label,": ",abs(d),'deg ',abs(m),"' ",abs(z),'"', sep='')
    else:
        print(label,": -",abs(d),"deg ",abs(m),"' ",abs(z),'"', sep='')

def dms_string(Decimal):
    d = int(Decimal)
    if (d < 100): dd = "0" + str(abs(d))    
    else: dd = str(abs(d))
    if (d < 10): dd = "0" + dd
    m = int((Decimal - d) * 60)
    if (abs(m) < 10): mm = "0" + str(abs(m))
    else: mm = str(abs(m))
    s = int((Decimal - d - m/60) * 3600.00)
    if (abs(s) < 10): ss = "0" + str(abs(s))
    else: ss = str(abs(s))
    #z= round(s, 2)
    if d >= 0:
        st = dd+u'\xb0'+mm+"'"+ss+'"'
    else:
        st = "-"+dd+u'\xb0'+mm+"'"+ss+'"'
    return(st)

def dms_string2(Decimal):
    d = int(Decimal)
    if (d < 100): dd = "  " + str(abs(d))    
    else: dd = str(abs(d))
    if (d < 10): dd = "  " + dd
    m = int((Decimal - d) * 60)
    if (abs(m) < 10): mm = "0" + str(abs(m))
    else: mm = str(abs(m))
    s = int((Decimal - d - m/60) * 3600.00)
    if (abs(s) < 10): ss = "0" + str(abs(s))
    else: ss = str(abs(s))
    #z= round(s, 2)
    if d >= 0:
        st = dd+'.'+mm+"."+ss
    else:
        st = "-"+dd+'.'+mm+"."+ss
    return(st)

def ms_string(Decimal):
    m = int(Decimal)
    if (m < 10): mm = "0" + str(abs(m))
    else: mm = str(abs(m))
    s = int((Decimal - m) * 60)
    if (abs(s) < 10): ss = "0" + str(abs(s))
    else: ss = str(abs(s))
    if m >= 0:
        st = mm+"'"+ss+'"'
    else:
        st = "-"+mm+"'"+ss+'"'
    return(st)

def lat_dms_string(Decimal):
    if (Decimal < 0):
        Decimal = -1 * Decimal
        Northing = False
    else: Northing = True
    d = int(Decimal)
    if (d < 10): dd = "  " + str(abs(d))
    else: dd = str(abs(d))
    m = int((Decimal - d) * 60)
    if (m < 10): mm = "0" + str(abs(m))
    else: mm = str(abs(m))
    s = int((Decimal - d - m/60) * 3600.00)
    if (s < 10): ss = "0" + str(abs(s))
    else: ss = str(abs(s))
    #z= round(s, 2)
    if Northing:
        st = dd+'.'+mm+"."+ss+' N'
    else:
        st = dd+'.'+mm+"."+ss+' S'
    return(st)

def hms_string(Decimal):
    d = int(Decimal)
    if (d < 10): dd = "0" + str(abs(d))
    else: dd = str(abs(d))
    m = int((Decimal - d) * 60)
    if (m < 10): mm = "0" + str(abs(m))
    else: mm = str(abs(m))
    s = int((Decimal - d - m/60) * 3600.00)
    if (s < 10): ss = "0" + str(abs(s))
    else: ss = str(abs(s))
    #z= round(s, 2)
    if d >= 0:
        st = dd+'h'+mm+"m"+ss+'s'
    else:
        st = "-"+dd+'h'+mm+"m"+ss+'s'
    return(st)

def hm_string(Decimal):
    d = int(Decimal)
    if (d < 10): dd = "0" + str(abs(d))
    else: dd = str(abs(d))
    m = int((Decimal - d) * 60)
    if (m < 10): mm = "0" + str(abs(m))
    else: mm = str(abs(m))
    if d >= 0:
        st = dd+'h'+mm+"m"
    else:
        st = "-"+dd+'h'+mm+"m"
    return(st)

