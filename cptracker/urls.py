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
        'portfolios/<int:pk>/change',
        views.PortfolioUpdateView.as_view(),
        name='change_portfolio'
    ),
    path('portfolios/add/', views.PortfolioCreateView.as_view(), name='add_portfolio'),
    # Assets.
    path(
        'portfolios/<int:pk>/asset/add',
        views.UserAssetCreateView.as_view(),
        name='add_userasset',
    ),
    path(
        'portfolios/<int:portfolio_id>/asset/<int:pk>/change',
        views.UserAssetUpdateView.as_view(),
        name='change_userasset',
    ),
]