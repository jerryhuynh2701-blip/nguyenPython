def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    
    if speed <= 60:
        print("No ticket")
    elif 61 <= speed <= 80:
        print("minor ticket")
    elif speed >= 81:
        print("Major ticket")


print(caught_speeding(64,True))