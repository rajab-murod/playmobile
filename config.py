import base64

from django.conf import settings

class Config:
    URL = settings.PLAY_MOBILE_SETTINGS['API_URL']
    PREFIX = settings.PLAY_MOBILE_SETTINGS['PREFIX']
    DEFAULT_ORIGINATOR = settings.PLAY_MOBILE_SETTINGS['ORIGINATOR']
    ORIGINATOR = '3700' if DEFAULT_ORIGINATOR == '' else DEFAULT_ORIGINATOR
    LOGIN = settings.PLAY_MOBILE_SETTINGS['LOGIN']
    PASSWORD = settings.PLAY_MOBILE_SETTINGS['PASSWORD']

    def __init__(self):
        self.HEADER = self.header()

    def header(self):
        data = '{}:{}'.format(self.LOGIN, self.PASSWORD)
        encoded = base64.b64encode(data.encode('utf-8'))
        header = {'Authorization': 'Basic {}'.format(str(encoded, 'utf-8'))}
        return header