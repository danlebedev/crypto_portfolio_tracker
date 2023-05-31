from django.urls import path

from . import views


app_name = 'cptracker'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    # Portfolios.
    path('portfolios/', views.portfolios, name='portfolios'),
    path('portfolios/<int:portfolio_id>/', views.portfolio, name='portfolio'),
    path(
        'portfolios/<int:pk>/change_portfolio',
        views.PortfolioUpdateView.as_view(),
        name='change_portfolio'
    ),
    path('portfolios/add/', views.PortfolioCreateView.as_view(), name='add_portfolio'),
    # Assets.
    path(
        'portfolios/<int:pk>/add/',
        views.UserAssetCreateView.as_view(),
        name='add_userasset',
    ),
]