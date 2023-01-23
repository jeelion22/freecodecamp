import datetime


def add_time(start_time, duration, start_day_of_week=None):

    hr = int(duration.split(":")[0])
    min = int(duration.split(":")[1])

    sta_time_obj = datetime.datetime.strptime(start_time, "%I:%M %p")
    time_duration = datetime.timedelta(hours=hr, minutes=min)
    new_date = sta_time_obj + time_duration
    days_remaing = int(new_date.day) - 1
    cur_time = new_date.strftime("%I:%M %p")

    if start_day_of_week != None:
        days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        if start_day_of_week.title() in days:
            day = days_remaing % 7
            ind = days.index(start_day_of_week.title())
            cur_day = days[day + ind]

            if days_remaing == 1:
                return "{} (next day)".format(cur_time)
            elif days_remaing > 1:
                return "{}, {} ({} days later)".format(cur_time, cur_day, days_remaing)
            else:
                return "{}, {}".format(cur_time, cur_day)

    else:
        if days_remaing == 1:
            return "{} (next day)".format(cur_time)
        elif days_remaing > 1:
            return "{} ({} days later)".format(cur_time, days_remaing)
        else:
            return "{}".format(cur_time)


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
