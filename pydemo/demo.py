
total_seconds = int(input("Enter seconds: "))

minutes = int(total_seconds / 60)

remaining_seconds = total_seconds % 60

print(minutes, 'minutes and' , remaining_seconds , 'seconds')

print(f"{minutes} minutes and {remaining_seconds} seconds")