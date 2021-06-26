#https://ferhatcicek.com/2015/08/08/raspberry-uzerinden-python-tweepy-kutuphanesi-kullanilarak-tweet-gonderilmesi/
#!/usr/bin/env python
#gerekli kütüphaneleri import edelim
import os
import sys
import tweepy

#apps.twitter.com adresinden aldığımız consumer ve access bilgileri tanımlayalım
CONSUMER_KEY = 'size ait Consumer Key (API Key)'
CONSUMER_SECRET = 'size ait Consumer Secret (API Secret)'
ACCESS_KEY = 'size ait Access Token'
ACCESS_SECRET = 'size ait Access Token Secret'

#twitter ile doğrulama işlemleri gerçekleştirelim
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#meşhur sıcaklık verisini alıp işleyelim
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

#sıcaklık bilgisini tweet olarak gönderelim.
api.update_status(temp);
