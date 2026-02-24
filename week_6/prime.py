
def is_prime (num):
    if num == 2 or num == 3: return True
    
    if num % 2 == 0: return False

    for i in range (3, num , 2):
        if num % i == 0:
            return False
        else:
            return True

    

# user_input = int(input())
# print(is_prime(user_input))


# def caught_speeding(speed, is_birthday):
#     if is_birthday:
#         speed -= 5
    
#     if speed <= 60:
#         print("No ticket")
#     elif 61 <= speed <= 80:
#         print("minor ticket")
#     elif speed >= 81:
#         print("Major ticket")

# num = int(input())
# t_or_f = bool()
# print(caught_speeding(num,t_or_f))

def alarm_clock(vacation, day):
    weekend = (day == 0 or day == 6)
    if vacation and weekend:
        return "off"
    return "10:00" if (vacation or weekend) else "7:00"

print(alarm_clock(True,2))








