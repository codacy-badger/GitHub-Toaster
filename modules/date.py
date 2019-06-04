from modules import shortcuts
from datetime import datetime
from time import time


def iso_to_ts(iso8601_date):
    date = datetime.strptime(iso8601_date, '%Y-%m-%dT%H:%M:%S%z')

    return shortcuts.real_int(date.timestamp())


def get_ago(timestamp):
    now = shortcuts.real_int(time())
    diff = now - timestamp

    seconds = diff
    minutes = seconds / 60
    hours = minutes / 60

    if seconds < 60:
        choice = 'seconds'

    elif minutes < 60:
        choice = 'minutes'

    else:
        choice = 'hours'

    if choice == 'seconds' and eval(choice) <= 5:
        return 'Just now'

    else:
        if eval(choice) == 1:
            choice = choice[0:len(choice)-1]

        return str(shortcuts.real_int(eval(choice))) + ' ' + choice + ' ' + 'ago'

