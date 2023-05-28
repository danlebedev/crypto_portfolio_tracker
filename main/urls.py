from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    # Assets
    path('add/', views.AssetCreateView.as_view(), name='add_asset'),
]