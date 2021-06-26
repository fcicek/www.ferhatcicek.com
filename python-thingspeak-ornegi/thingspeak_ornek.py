#https://ferhatcicek.com/2015/12/06/nesnelerin-interneti-icin-veri-kayit-alanlari-thingspeak-platformunun-raspberry-ile-kullanim-ornegi/

import httplib, urllib
import psutil
import time
import os

def cpu_sicaklik_oku():
 res = os.popen('vcgencmd measure_temp').readline()
 return(res.replace("temp=","").replace("'C\n",""))

if __name__ == "__main__":
    while True:
        cpu = psutil.cpu_percent()
        ram = (psutil.avail_phymem()/1024)/1024
        cpu_sicaklik = cpu_sicaklik_oku()
        params = urllib.urlencode({'field1': cpu, 'field2':ram, 'field3':cpu_sicaklik, 'key':'THINKSPEAK_KEY'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
        time.sleep(60)
