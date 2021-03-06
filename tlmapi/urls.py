from django.urls import path

from . import views

urlpatterns = [
    path('api/sampleapi', views.sample_api),
    path('api/sampleapi2', views.sample_api2),
    path('api/auto_record', views.auto_record),
    path('api/record', views.record),
    path('api/gettestrecord', views.gettestrecord),
    path('api/gettlm', views.gettlm),
    path('api/gettlmqtc', views.gettlmqtc),
    path('api/autorecordnodejs', views.autorecordnodejs),
    path('api/gettlmpci', views.gettlmpci),
    path('api/gettlmchi', views.gettlmchi),
]
