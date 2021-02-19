from django.shortcuts import render,redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .models import Details
from bitcoin import *
import bs4
import requests 

# from .forms import UserUpdateForm,ProfileUpdateForm
# Create your views here.


def register(request):


    detail = Details()
    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    detail.private_key = private_key
    detail.public_key = public_key
    detail.address = address

    password_error = ''
    terms_error = ''
    user_error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # private_key = request.POST['private_key']
        # public_key = request.POST['public_key']
        # address = request.POST['address']


        terms = request.POST.get('terms')
        if password1 != password2:
            password_error = "Password does not match!"
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                if terms:
                    User.objects.create(username=username, email=email, password=password1)

                    
                    user = User.objects.get(username=username)
                    
                    Details.objects.create(
                        user=user,
                        private_key=private_key,
                        public_key=public_key,
                        address=address
                    )
                    messages.success(request, f'Account created for {username}!')
                    return redirect('login')
                else:
                    terms_error = "Accept terms and conditions!"
    context = {
        "password_error": password_error,
        "terms_error": terms_error,
        "user_error": user_error
    }
    return render(request, 'users/register.html', context)
    
# Create your views here.
def signin(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                login(request, user=user)
                return redirect("exchange")
            else:
                error = "Incorrect password!"
        except:
            error = "User doesn't exist"
    context = {
        "error": error
    }
    return render(request, 'users/login.html', context)
   
def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = User.objects.get(username=request.user)
    user_profile = None
    try:
        user_profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        user_profile = None
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        country = request.POST.get("country")
        state = request.POST.get("state")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        father = request.POST.get("father")
        mother = request.POST.get("mother")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        gender = request.POST.get("gender")
        status = request.POST.get("status")
        image = ""
        if request.FILES:
            image = request.FILES.get("image")

            user.first_name = first_name
            user.last_name = last_name
            user.save()
          
        try:  
            user_profile = Profile.objects.get(user=user)
            user_profile.countries = country
            user_profile.states = state
            user_profile.date_of_birth = dob
            user_profile.phone = phone
            user_profile.father_name = father
            user_profile.mother_name = mother
            user_profile.address1 = address1
            user_profile.address2 = address2
            user_profile.gender = gender
            user_profile.status = status
            user_profile.image = image
            user_profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(
                user=user,
                countries=country,
                states=state,
                date_of_birth=dob,
                phone=phone,
                father_name=father,
                mother_name=mother,
                address1=address1,
                address2=address2,
                gender=gender,
                status=status,
                image=image
            )
		
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'users/profile.html', context)


# def bitcoin_wallet(request):
#     detail = ''
#     if request.method == 'POST':
#         print('Passed')
#         addr = request.POST['addr']
#         res2 = requests.get('https://cryptowat.ch/')
#         soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
#         live_price = soup2.find_all('span', {'class': 'price'})
#         live_bitcoin_price = live_price[1].getText()
#         live_bitcoin_price1 = live_price[1].getText()
#         res = requests.get('https://www.blockchain.com/btc/address/'+addr)
#         soup = bs4.BeautifulSoup(res.text, 'lxml')
#         if res:
#             soup = bs4.BeautifulSoup(res.text, 'lxml')
#             print(soup)
#             # bal = soup.find_all('span', {'class': 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk'})
#             bal = soup.find_all('span', {'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
#             bal[4].getText()
#             final_bal = bal[4].getText()
#             final_bal1 = final_bal.replace(" ", "").rstrip()[:-3].upper()
#             transactions = bal[1].getText()
#             total_received = bal[2].getText()
#             total_received1 = total_received.replace(" ", "").rstrip()[:-3].upper()
#             total_sent = bal[3].getText()
#             total_sent1 = total_sent.replace(" ", "").rstrip()[:-3].upper()
#             final_bal1_int = float(final_bal1)
#             total_received1_int = float(total_received1)
#             total_sent1_int = float(total_sent1)
#             live_bitcoin_price1_int = float(live_bitcoin_price1)
            
#             balance_usd = final_bal1_int*live_bitcoin_price1_int
#             total_received_usd = total_received1_int*live_bitcoin_price1_int
#             total_sent_usd = total_sent1_int*live_bitcoin_price1_int
#         else:
#             return redirect('/')
#         user = User.objects.get(username=request.user)
#         detail = Details.objects.get(user=user)
#         detail.balance = final_bal
#         detail.balance1 = final_bal1
#         detail.transactions = transactions
#         detail.total_received = total_received
#         detail.total_received1 = total_received1
#         detail.total_sent = total_sent
#         detail.total_sent1 = total_sent1
#         detail.live_bitcoin_price = live_bitcoin_price
#         detail.live_bitcoin_price1 = live_bitcoin_price1
#         detail.balance_usd = int(balance_usd)
#         detail.total_received_usd = int(total_received_usd)
#         detail.total_sent_usd = int(total_sent_usd)


#     else:
#         detail = ''
    
#     return render(request, 'bitcoin_wallet.html', {
#         'detail' : detail,
#         'address': None})



