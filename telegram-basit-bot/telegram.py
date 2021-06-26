#https://ferhatcicek.com/2020/05/26/raspberry-pi-uzerinde-en-basitinden-telegram/

import sys
import time
import telepot
import requests
import datetime

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Komut: %s' % command)

    if command =='ip':
       ipadd = requests.get('https://checkip.amazonaws.com').text.strip()
       bot.sendMessage(chat_id, str(ipadd))
    elif command == 'zaman':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == 'resim':
        bot.sendPhoto(chat_id, photo="http://www.ferhatcicek.com/wp-content/uploads/2019/09/kalyon.jpg")
    elif command == 'dosya':
        bot.sendDocument(chat_id, document=open('/home/pi/telegram/telegram.py'))
    elif command == 'muzik':
        bot.sendAudio(chat_id, audio=open('/home/pi/test.mp3'))

bot = telepot.Bot('6686324245:AAVuDyUVKAYeKVLW3TuFD5ty_3XTVQTnpZQ')
bot.message_loop(handle)
print('Komut bekleniyor...')

while 1:
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print('\n Program sonlandı')
        exit()
    except:
        print('Hata')
