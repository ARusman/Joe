# howdy/urls.py
from django.conf.urls import url
from co2 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]