import driver
import random
import requests
import time
face = "null"

print(face)
mylcd=driver.lcd()

def refresh():
      mylcd.lcd_display_string("                ",1,0)
      mylcd.lcd_display_string("                ",2,0)
time.sleep(1)
refresh()
part = 1
hor = 0

def wr(str, p = 1, h = 0, f = "null"):
    length = len(str)
    main = -1
    if length>15:
        for i in range(length+1):
            time.sleep(0.1)
            main = main+ 1
            mylcd.lcd_display_string(str[main:length]+"  ",p,0)

    else:
         mylcd.lcd_display_string(str,p,h)

def write(string):
    inp = string
    length = len(inp)
    main = -1
    if length>15:
        for i in range(length+1):
            time.sleep(0.2)
            main = main+ 1
            mylcd.lcd_display_string(inp[main:length]+"                        ",1,0)
    else:
        mylcd.lcd_display_string(string,part,hor)
part = 1
def write1(string):
    inp = string
    length = len(inp)
    main = -1
    if length>15:
        for i in range(length+1):
            time.sleep(0.2)
            main = main+ 1
            mylcd.lcd_display_string(inp[main:length]+"                        ",1,0)
    else:
          mylcd.lcd_display_string(inp[main:length]+"                        ",1,0)
part = 1
while(True):
    url =  "http://127.0.0.1:8666/api/v1/mesh/data"
    headers = {}
    payload = {}
    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json()
    part = 2
    hor = 5
    try:
        face = str(data["face"])
    except Exception:
        face  =  "null"



    time.sleep(1)
    if(face == "null"):
          part = 2
          hor = 5
          print("MANU") 
          write("MANUAL")
          hor = 15
          write(str(random.randint(1,9)))


    else:
          hor = 0
          time.sleep(1)
          url =  "http://127.0.0.1:8666/api/v1/mesh/data"
          headers = {}
          payload = {}
          response = requests.request("GET", url, headers=headers, data = payload)
          data = response.json()
          part = 2
          hor = 5
          face = str(data["face"])
          write(face+"         ")
          hor = 15
          write(str(random.randint(1,9)))
          part = 1
          print(face)
          msg = str(data["msg"])
          wr (msg, f = face)

