from django.urls import path
from apps.sensor.views import DashBoardView

app_name = 'apps.sensor'

urlpatterns = [
    path('', DashBoardView.as_view(), name="dashboard"),
]
