import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from playmobile.serializers import PlayMobileSerializer

from playmobile.config import Config

class  PlayMobileApiView(APIView):
    def __init__(self):
        self.conf = Config()
        super(PlayMobileApiView, self).__init__()

    def post(self, request):
        serializer = PlayMobileSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        result = self.sender(serializer.validated_data)
        return Response({'status': result})

    def sender(self, validated_data):
        data = {
            'messages': [
                {
                    'recipient': validated_data['phone_number'],
                    'message-id': '{}{}'.format(self.conf.PREFIX, validated_data['message_id']),
                    'sms': {
                        'originator': self.conf.ORIGINATOR,
                        'content': {
                            'text': validated_data['text']
                        }
                    }
                }
            ]
        }
        response = requests.post(self.conf.URL, json=data, headers=self.conf.HEADER)
        return response.status_code
