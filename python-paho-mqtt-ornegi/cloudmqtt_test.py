
#https://ferhatcicek.com/2015/07/30/mqtt-client-pahonun-python-kutuphanesi-kullanilarak-cloudmqtt-servisi-uzerinde-bir-ornek/

import mosquitto, os, urlparse
import paho.mqtt.client as paho

def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqtt_pahoclient = paho.Client()
mqtt_pahoclient.on_message = on_message
mqtt_pahoclient.on_connect = on_connect
mqtt_pahoclient.on_publish = on_publish
mqtt_pahoclient.on_subscribe = on_subscribe

mqtt_pahoclient.on_log = on_log

url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://iskarfwb:tRi1l3nkuCCa@m20.cloudmqtt.com:11440')
#mqtt://USER:PASSWORD@host:port
url = urlparse.urlparse(url_str)

mqtt_pahoclient.username_pw_set(url.username, url.password)
mqtt_pahoclient.connect(url.hostname, url.port)

mqtt_pahoclient.subscribe("hello/world", 0)

mqtt_pahoclient.publish("hello/world", "my message")

rc = 0
while rc == 0:
    rc = mqtt_pahoclient.loop()
print("rc: " + str(rc))
