from django.urls import path
from playmobile.views import PlayMobileApiView

urlpatterns = [
    path('sender/', PlayMobileApiView.as_view(), name='send')
]