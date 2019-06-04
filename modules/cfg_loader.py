import json
from modules import shortcuts


def load():
    with open('config.json', 'r') as file:
        data = json.load(file)
        file.close()

    error = False

    if not data['notification_duration']:
        data['notification_duration'] = 5

    if not data['delay']:
        data['delay'] = 10

    if not data['username']:
        print('Error: username is required variable in config.json. Please set it')
        shortcuts.alert(
            'Error', 'username is required variable in config.json. Please set it',
            data['notification_duration']
        )
        error = True

    if not data['access_token']:
        print('Error: access_token is required variable in config.json. Please set it')
        shortcuts.alert(
            'Error', 'access_token is required variable in config.json. Please set it',
            data['notification_duration']
        )
        error = True

    if data['notification_duration'] < 3:
        print('Error: notification_duration can\'t be less than 3')
        shortcuts.alert(
            'Error', 'notification_duration can\'t be less than 3',
            data['notification_duration']
        )
        error = True

    if error:
        exit(0)

    return data

