import datetime

# Another sulotion https://github.com/epochblue/exercism/blob/master/python/meetup/meetup.py

class MeetupDayException(ValueError):
    raise ValueError("Error")


WHICH_TO_INDEX = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4}


def next_day(dt, dow):
    dt = dt + datetime.timedelta(days = 1)
    while dt.strftime('%A') != dow:
        dt = dt + datetime.timedelta(days = 1)
    return dt


def meetup_day(year, month, dow, which):
    dt = datetime.date(year, month, 1)
    
    if which in WHICH_TO_INDEX:
        dt = dt - datetime.timedelta(days = 1)
        i = 0
        while i <= WHICH_TO_INDEX[which]:
            dt = next_day(dt, dow)
            print(dt.day)
            i = i + 1

    elif which == 'teenth':
        next_dt = next_day(dt, dow)
        while next_dt.day < 20:
            dt = next_dt
            next_dt = next_day(dt, dow)

    elif which == 'last':
        next_dt = next_day(dt, dow)
        while dt.month == next_dt.month:
            dt = next_dt
            next_dt = next_day(dt, dow)

    if dt.month != month:
        raise MeetupDayException()

    return dt


def main():
    dt = meetup_day(2013, 7, 'Wednesday', 'last')
    print(dt)


main()