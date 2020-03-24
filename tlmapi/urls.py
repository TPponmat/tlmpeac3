from django.urls import path

from . import views

urlpatterns = [
    path('api/sampleapi', views.sample_api),
    path('api/auto_record', views.auto_record),
    path('api/record', views.record),
    path('api/gettestrecord', views.gettestrecord),
    path('api/gettlm', views.gettlm),
    # path('api/line', views.line)
]