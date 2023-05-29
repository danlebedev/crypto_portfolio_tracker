from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    # Assets
    path('assets/', views.assets, name='assets'),
    path('assets/add/', views.AssetCreateView.as_view(), name='add_asset'),
]