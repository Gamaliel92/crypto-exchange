"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from wallet.views import index
from wallet.views import exchange_2
from wallet.views import exchange_3
from wallet.views import exchange_4
from wallet.views import market_overview
from wallet.views import marketcap
from wallet.views import trading
from wallet.views import account
from wallet.views import forgot
from wallet.views import withdrawal
from wallet.views import bitcoin_wallet
from users.views import logout_user 
from users.views import signin
from users.views import register
from users.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet', include('wallet.urls')),
    path('register/',register , name='register'),
    path("login", signin, name='login'),
    path("logout/", logout_user, name='logout'),
    path("forgot", forgot, name='forgot'),
    path('', index, name='exchange'),
    path("exchange-2" ,exchange_2, name="exchange-2"),
    path("exchange-3" ,exchange_3, name="exchange-3"),
    path("exchange-4" ,exchange_4, name="exchange-4"),
    path("market-overview" ,market_overview, name='market-overview'),
    path("marketcap" ,marketcap, name='marketcap'),
    path("trading" ,trading, name='trading'),
    path("account" ,account, name='account'),
    path("withdrawal",withdrawal, name='withdrawal'),
    path("profile", profile, name='profile'),
    path("bitcoin_wallet", bitcoin_wallet, name='bitcoin_wallet')  
] 
  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)