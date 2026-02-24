def alarm_clock(vacation, day):
    weekend = (day == 0 or day == 6)
    if vacation and weekend:
        return "off"
    return "10:00" if (vacation or weekend) else "7:00"

print(alarm_clock(True,2))
