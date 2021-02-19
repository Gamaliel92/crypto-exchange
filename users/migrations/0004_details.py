# Generated by Django 3.1.3 on 2021-02-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210126_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.CharField(max_length=500)),
                ('balance1', models.CharField(max_length=500)),
                ('transactions', models.CharField(max_length=500)),
                ('total_sent', models.CharField(max_length=500)),
                ('total_sent1', models.CharField(max_length=500)),
                ('total_received', models.CharField(max_length=500)),
                ('total_received1', models.CharField(max_length=500)),
                ('private_key', models.CharField(max_length=500)),
                ('public_key', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('live_bitcoin_price', models.CharField(max_length=500)),
                ('live_bitcoin_price1', models.CharField(max_length=500)),
                ('balance_usd', models.CharField(max_length=500)),
                ('total_sent_usd', models.CharField(max_length=500)),
                ('total_received_usd', models.CharField(max_length=500)),
            ],
        ),
    ]