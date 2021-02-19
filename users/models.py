from django.db import models
from django.contrib.auth.models import User

COUNTRIES = (
    ("NIGERIA", "Nigeria"),
    ("GHANA", "Ghana"),
    ("TOGO", "Togo"),
    ("CANADA", "Canada"),
    ("SOUTH_AFRICA", "South Africa"),
)

STATE = (
    ("ABIA", "Abia"),
    ("ADAMAWA", "Adamawa"),
    ("LAGOS", "Lagos"),
    ("EDO", "Edo"),
    ("ONDO", "Ondo"),
)

GENDER = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("OTHERS", "Others"),
)

STATUS = (
    ("SINGLE", "Single"),
    ("MARRIED", "Married"),
    ("DIVORCE", "Divorce"),
)

# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    countries = models.CharField(max_length=150, choices=COUNTRIES, blank=True, null=True)
    states = models.CharField(max_length=150, choices=STATE, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=150, choices=GENDER, blank=True, null=True)
    status = models.CharField(max_length=150, choices=STATUS, blank=True, null=True)

    # def __str__(self):
    #     return f'{self.user.username} Profile'

class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    balance = models.CharField(max_length=500)
    balance1 = models.CharField(max_length=500)
    transactions = models.CharField(max_length=500)
    total_sent = models.CharField(max_length=500)
    total_sent1 = models.CharField(max_length=500)
    total_received = models.CharField(max_length=500)
    total_received1 = models.CharField(max_length=500)
    private_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    live_bitcoin_price = models.CharField(max_length=500)
    live_bitcoin_price1 = models.CharField(max_length=500)
    balance_usd = models.CharField(max_length=500)
    total_sent_usd = models.CharField(max_length=500)
    total_received_usd = models.CharField(max_length=500)






