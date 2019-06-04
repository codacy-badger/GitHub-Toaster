from modules import shortcuts, github, cfg_loader, date
from time import time, sleep
from requests import exceptions as internet_err


def main():
    cfg = cfg_loader.load()

    shortcuts.alert('Yay!', 'I am working. So you will receive notifications from GitHub ;)', cfg['notification_duration'])
    send_events_since = shortcuts.real_int(time())

    while True:
        events = github.ReceivedEvents.row()
        new_events = []

        for event in events:
            if date.iso_to_ts(event['created_at']) > send_events_since:
                new_events.append(event)

            else:
                break

        if new_events:
            new_events = new_events[::-1]
            send_events_since = date.iso_to_ts(new_events[0]['created_at'])

            for event in new_events:
                ev_actor = event['actor']['login']
                ev_type = event['type']
                ev_date = date.iso_to_ts(event['created_at'])

                if ev_type == 'WatchEvent':
                    message = ev_actor + ' ' + 'starred' + ' ' + event['repo']['name']

                elif ev_type == 'ForkEvent':
                    message = ev_actor + ' ' + 'forked' + ' ' + event['repo']['name']

                elif ev_type == 'CreateEvent':
                    message = ev_actor + ' ' + 'created' + ' ' + event['repo']['name']

                elif ev_type == 'PublicEvent':
                    message = ev_actor + ' ' + 'opened access to' + ' ' + event['repo']['name']

                # You can add more event types yourself. Just send pull request <3

                else:
                    message = ev_actor + ' ' + ev_type

                shortcuts.alert(
                    title='New event',
                    message=message + '\n' + date.get_ago(ev_date),
                    duration=cfg['notification_duration']
                )

        sleep(cfg['delay'])


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        shortcuts.alert('Yay!', 'Thank you for using me :3. Hope you enjoyed', 5)
        exit(0)

    except internet_err.ConnectionError:
        shortcuts.alert('Error', 'Connection error. Restarting...', 5)
        main()  # Check line 77

    except Exception as ex:
        shortcuts.alert('Unknown error', str(ex) + '\n' + 'Restarting...', 5)
        main()  # This is the WORTH way to restart program, bgc it restarts only 1 time.
                # If you know better way, please send pull request. (yes I tried to find solution in Google)
