import datetime


def add_time(start_time, duration, start_day_of_week=None):
    hr = int(duration.split(":")[0])
    min = int(duration.split(":")[1])

    sta_time_obj = datetime.datetime.strptime(start_time, "%I:%M %p")
    time_duration = datetime.timedelta(hours=hr, minutes=min)
    new_date = sta_time_obj + time_duration
    days_remaing = int(new_date.day) - 1

    hour_format = int(new_date.strftime("%I"))
    cur_time = str(hour_format) + str(new_date.strftime(":%M %p"))

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
            day_index = day + ind
            if day_index > 6:
                cur_day = days[day_index % 7]
            else:
                cur_day = days[day + ind]

            if days_remaing == 1:
                return "{}, {} (next day)".format(cur_time, cur_day)
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


print(add_time("6:30 PM", "205:12"))
