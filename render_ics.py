import arrow
import calendar
import dateutil
import json
from ics import Calendar, Event

MONTH_NUM_BY_NAME = {name: str(num) for num, name in enumerate(calendar.month_name)}

DATA = '[{"monthName":"October 2019","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":1},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":1},{"day":"30","holidayPortion":1},{"day":"1","holidayPortion":1},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0.5},{"day":"9","holidayPortion":1},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":1},{"day":"14","holidayPortion":1}]},{"monthName":"November 2019","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0.5},{"day":"21","holidayPortion":1},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"December 2019","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"January 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"February 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"March 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"April 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0.5},{"day":"14","holidayPortion":0.5}]},{"monthName":"May 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"June 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0.5},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"July 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"August 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]},{"monthName":"September 2020","daysInMonth":[{"day":"15","holidayPortion":0},{"day":"16","holidayPortion":0},{"day":"17","holidayPortion":0},{"day":"18","holidayPortion":0},{"day":"19","holidayPortion":0},{"day":"20","holidayPortion":0},{"day":"21","holidayPortion":0},{"day":"22","holidayPortion":0},{"day":"23","holidayPortion":0},{"day":"24","holidayPortion":0},{"day":"25","holidayPortion":0},{"day":"26","holidayPortion":0},{"day":"27","holidayPortion":0},{"day":"28","holidayPortion":0},{"day":"29","holidayPortion":0},{"day":"30","holidayPortion":0},{"day":"31","holidayPortion":0},{"day":"1","holidayPortion":0},{"day":"2","holidayPortion":0},{"day":"3","holidayPortion":0},{"day":"4","holidayPortion":0},{"day":"5","holidayPortion":0},{"day":"6","holidayPortion":0},{"day":"7","holidayPortion":0},{"day":"8","holidayPortion":0},{"day":"9","holidayPortion":0},{"day":"10","holidayPortion":0},{"day":"11","holidayPortion":0},{"day":"12","holidayPortion":0},{"day":"13","holidayPortion":0},{"day":"14","holidayPortion":0}]}]'


def _build_arrow(s):
    return arrow.get(s, 'YYYY/M/D HH:mm:ss').replace(tzinfo=dateutil.tz.gettz('Asia/Jerusalem'))


def main():
    months_list = json.loads(DATA)
    c = Calendar()
    for month_dict in months_list:
        month_name, year = month_dict['monthName'].split(' ')
        month_num = MONTH_NUM_BY_NAME[month_name]
        is_prev_month = True

        for day_dict in month_dict['daysInMonth']:
            holiday_portion = day_dict['holidayPortion']
            day = day_dict['day']

            if day == '1':
                is_prev_month = False

            if holiday_portion == 0:
                continue

            adjusted_month = _get_adjusted_month(is_prev_month, month_num)
            start_time, title = _get_title_and_start_time(holiday_portion)
            _add_event(c, title, year, adjusted_month, day, start_time)

    print(c.events)

    with open('my.ics', 'w') as my_file:
        my_file.writelines(c)


def _get_adjusted_month(is_prev_month, month_num):
    adjusted_month = month_num
    if is_prev_month:
        adjusted_month = str(int(adjusted_month) - 1)
    return adjusted_month


def _get_title_and_start_time(holiday_portion):
    if holiday_portion == 1:
        title = "Entire Day Off"
        start_time = '08:00:00'
    elif holiday_portion == .5:
        title = "Half Day Off"
        start_time = '13:00:00'
    else:
        raise ValueError('holiday_portion can only be 0, .5 or 1')
    return start_time, title


def _add_event(c, title, year, month, day, start_time):
    e = Event()
    e.name = title
    e.begin = _build_arrow(f'{year}/{month.zfill(2)}/{day.zfill(2)} {start_time}')
    e.end = _build_arrow(f'{year}/{month.zfill(2)}/{day.zfill(2)} 20:00:00')
    c.events.add(e)


if __name__ == '__main__':
    main()
