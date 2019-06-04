from modules import cfg_loader
from requests import get


cfg = cfg_loader.load()


class ReceivedEvents:
    @staticmethod
    def row():
        return get(
            'https://api.github.com/users/' + cfg['username'] + '/received_events?access_token=' + cfg['access_token']
        ).json()


class Notifications:
    @staticmethod
    def row():
        return get(
            'https://api.github.com/notifications?access_token=' + cfg['access_token']
        ).json()
