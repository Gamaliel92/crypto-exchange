from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='exchange'),
    path("exchange-2/", views.exchange_2, name="exchange-2"),
    path("exchange-3/", views.exchange_3, name="exchange-3"),
    path("exchange-4/", views.exchange_4, name="exchange-4"),
    path("market-overview/", views.market_overview, name='market-overview'),
    path("marketcap/", views.marketcap, name='marketcap'),
    path("trading/", views.trading, name='trading'),
    path("account/", views.account, name='account'),
    # path("register" ,register, name='Register'),
    path("forgot/", views.forgot, name='forgot'),
    path("withdrawal/", views.withdrawal, name='withdrawal'),
    path("bitcoin_wallet/", views.bitcoin_wallet, name='bitcoin_wallet'),

] 