import time

# Function to start the countdown timer
def alarm_clock(hours , mins):
    print(f'Alarm set for {hours:02}:{mins:02} {am_pm.upper()}: Waiting....')
    
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        
        current_12_hour = current_hour % 12     
        if current_12_hour == 0:
            current_12_hour = 12

        current_am_pm = "AM" if current_hour < 12 else "PM"
        

        if current_12_hour == hours and current_minute == mins and current_am_pm == am_pm.upper():
            print(f"Wake up! Time's up... {hours:02}:{mins:02} {am_pm.upper()}!")
        time.sleep(60)

hours = int(input('Enter the hour for the alarm (1-12): '))
mins = int(input('Enter the minute for the alarm (0-59): '))
am_pm = input('Enter am or pm: ')

if 1 <= hours <= 12 and 0 <= mins < 60: 
    alarm_clock(hours, mins)
else:
    print('Please enter a valid time (hour: 1-12, minute: 0-59, am/pm: am or pm).')

# if 0 <= hours < 24 and 0 <= mins < 60:
#     alarm_clock(hours,mins)



# import time       
#         current_12_hour = current_hour % 12
#         if current_12_hour == 0:  # For midnight or noon, set to 12
#             current_12_hour = 12
        
#         # Determine AM/PM
#         current_am_pm = "AM" if current_hour < 12 else "PM"
        
#         # Check if the current time matches the alarm time
#         if current_12_hour == hours and current_minute == mins and current_am_pm == am_pm.upper():
#             print(f"Wake up! Time's up... {hours:02}:{mins:02} {am_pm.upper()}!")
#             break
        
#         # Wait for a minute before checking the time again
#         time.sleep(60)

# # Get the alarm time from the user in 12-hour format (with AM/PM)
# hours = int(input('Enter the hour for the alarm (1-12): '))
# mins = int(input('Enter the minute for the alarm (0-59): '))
# am_pm = input('Enter AM or PM: ').strip().upper()

# # Validate the input
# if 1 <= hours <= 12 and 0 <= mins < 60 and am_pm in ['AM', 'PM']:
#     alarm_clock(hours, mins, am_pm)
# else:
#     print('Please enter a valid time (hour: 1-12, minute: 0-59, AM/PM: AM or PM).')