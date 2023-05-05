from django.urls import path

from . import views


app_name = 'cptracker'
urlpatterns = [
    # Homepage.
    path('', views.index, name="index")
]