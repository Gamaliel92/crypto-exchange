from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import requests 
import json
from bitcoin import *
import bs4
from users.models import Details
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from urllib.parse import urlencode
# from shrimpy.auth_provider import AuthProvider

def index(request):
    url = 'https://api.bitfinex.com/v2/candles/trade:5m:tBTCUSD/hist'
    params = { 'start': 1434764470000, 'end': 1497922870000 }
    r = requests.get(url, params = params)
    data = r.json()
    print(data)
    return render(request, "index.html")


def exchange_2(request):
    resp = requests.get("https://api.cryptowat.ch/markets/kraken/btcusd/orderbook")
    orderbook = resp.json()['result']
    print(orderbook['asks'])
    # url = "https://dev-api.shrimpy.io/v1/historical/orderbooks"
    # params = { 'exchange': 'BTC', 'limit': 10 }
    # resp = requests.get(url, params=params)
    # orderbook = resp.json()
    # print(orderbook)
    context = {
        'orderbook_data': orderbook
    }
    return render(request, "exchange-2.html", context)


def exchange_3(request):
    return render(request, "exchange-3.html")


def exchange_4(request):
    return render(request, "exchange-4.html")


def overview(request):
    return render(request, "overview.html")


def marketcap(request):
    return render(request, 'marketcap.html')


def market_overview(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'20',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'a16fe6da-9414-4556-b345-cfeb4e1176e5',
    }

    session = Session()
    session.headers.update(headers)
    data = None

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    context = {
        'bitcoin_data': data
    }
    return render(request, 'market-overview.html',context)



def trading(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'20',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'a16fe6da-9414-4556-b345-cfeb4e1176e5',
    }

    session = Session()
    session.headers.update(headers)
    data = None

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    context = {
        'bitcoin_data': data
    }
    return render(request,'trading.html', context)


def account(request):
    return render(request, 'account.html')


def forgot(request):
    return render(request, 'forgot.html')


@login_required(login_url="login")
def withdrawal(request):
    user = User.objects.get(username=request.user)
    user_profile = None
    try:
        user_profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        user_profile = None
    context = {
        "profile": user_profile
    }
    return render(request, 'withdrawal.html', context)


def profile(request):
    resp = requests.get("https://api.cryptowat.ch/markets/kraken/btcusd/orderbook")
    orderbook = resp.json()['result']
    print(orderbook)

    context = {
        'orderbook_data': orderbook
    }
    return render(request, 'profile.html', context)


def bitcoin_wallet(request):
    user = User.objects.get(username=request.user)
    detail = None
    try:
        detail = Details.objects.get(user=user)
    except ObjectDoesNotExist:
        detail = None
        
    if request.method == 'POST':
        print('Passed')
        addr = request.POST['addr']
        res2 = requests.get('https://cryptowat.ch/')
        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
        live_price = soup2.find_all('span', {'class': 'price'})
        live_bitcoin_price = live_price[1].getText()
        live_bitcoin_price1 = live_price[1].getText()
        res = requests.get('https://www.blockchain.com/btc/address/'+addr)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        if res:
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            # bal = soup.find_all('span', {'class': 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk'})
            bal = soup.find_all('span', {'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
            bal[4].getText()
            final_bal = bal[4].getText()
            final_bal1 = final_bal.replace(" ", "").rstrip()[:-3].upper()
            transactions = bal[1].getText()
            total_received = bal[2].getText()
            total_received1 = total_received.replace(" ", "").rstrip()[:-3].upper()
            total_sent = bal[3].getText()
            total_sent1 = total_sent.replace(" ", "").rstrip()[:-3].upper()
            # print(bal[4].getText())
            final_bal1_int = float(final_bal1)
            total_received1_int = float(total_received1)
            total_sent1_int = float(total_sent1)
            live_bitcoin_price1_int = float(live_bitcoin_price1)
            
            balance_usd = final_bal1_int*live_bitcoin_price1_int
            total_received_usd = total_received1_int*live_bitcoin_price1_int
            total_sent_usd = total_sent1_int*live_bitcoin_price1_int
        else:
            return redirect('/')
        if detail:
            detail.balance = final_bal
            detail.balance1 = final_bal1
            detail.transactions = transactions
            detail.total_received = total_received
            detail.total_received1 = total_received1
            detail.total_sent = total_sent
            detail.total_sent1 = total_sent1
            detail.live_bitcoin_price = live_bitcoin_price
            detail.live_bitcoin_price1 = live_bitcoin_price1
            detail.balance_usd = int(balance_usd)
            detail.total_received_usd = int(total_received_usd)
            detail.total_sent_usd = int(total_sent_usd)
            detail.save()


    else:
        detail = ''
    
    context = {
        'detail': Details.objects.get(user=user),
    } 
    return render(request, 'bitcoin_wallet.html', context)


# Create your views here.
