import webbrowser
import time


def join_google_meet(link):
    # Open the Google Meet link in a web browser
    webbrowser.open(link)


def check_time_and_join_meet(link, target_time):
    while True:
        current_time = time.strftime("%H:%M")
        print(f"Current time: {current_time}", end="\r")

        if current_time == target_time:
            join_google_meet(link)
            break

        time.sleep(10)  # Wait for 10 seconds before checking the time again


# Set the Google Meet link and target time
google_meet_link = "https://meet.google.com/rre-byyf-ybv"
# Set the time you want to join the meet (in 24-hour format)
target_time = input("Enter meeting time in 24hours format HH:MM:  ")
print(f"Target time set: {target_time}")


# Start the program
check_time_and_join_meet(google_meet_link, target_time)
