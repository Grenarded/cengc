import datetime

def time(elapsed_minutes):
    start_time = datetime.datetime.strptime('07:00', '%H:%M')  # Set the start time at 7 AM
    total_time = datetime.timedelta(minutes=elapsed_minutes)  # Elapsed time in minutes

    end_time = start_time + total_time  # Calculate the end time by adding the total time
    print("End Time:", end_time)
    return end_time.strftime('%H:%M')  # Return the end time in hour:minute format
