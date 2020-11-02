import requests
import random
import time
from datetime import date, timedelta
from requests.exceptions import ConnectionError

local_url = 'url'
# var keeps today's date
today = date.today()

# definition of the 1st and the last days of the Halloween period
HwStart = date(today.year, 10, 1)
HwStop = date(today.year, 10, 31)
# the list of the days of the Halloween period
HwTime = [HwStart + timedelta(days=x) for x in range((HwStop-HwStart).days + 1)]

# definition of the 1st and the last days of the Christmas period
XmasStart = date(today.year, 12, 10)
XmasStop = date(today.year+1, 1, 1)
# the list of the days of the Christmas period
XmasTime = [XmasStart + timedelta(days=x) for x in range((XmasStop - XmasStart).days + 1)]

def Changer():
# list of Halloween effects
    HwFx = random.choice([53, 77, 15, 78, 80, 106])
# list of Christmas effects
    XmasFx = random.choice([3, 7, 13, 15, 18, 19, 27, 34, 38, 52, 54, 56, 69, 74, 76, 78, 101, 107, 110, 44])
# var keeps random number of effects
    randomfx = random.randint(0, 113)
# list of annoying effects which I would like to avoid
    avoid = [1, 22, 23, 24, 25, 26]
    while randomfx in avoid:
        randomfx = random.randint(0, 113)
# vars for random colors
    r, g, b = random.sample(range(0, 255), 3)

    try:
# checking if HomeAssistant's turned LED lights on
        turned = requests.get(local_url + '/json').json()['state']['on']
# sends a new post request with one of the Halloween effect. Also there are 2  permanent colors (orange(RGB2) and purple(RGB1))
        if turned and today in HwTime:
            requests.post(local_url+'/win&FX={}&SX=100&IX=150&R=128&G=0&B=128&R2=255&G2=125&B2=0&R3=0&G3=0&B3=0'.format(HwFx))
# sends a new post request with one of the Christmas effect. Also there are 2  permanent colors (green(RGB2) and red(RGB1))
        elif turned and today in XmasTime:
            requests.post(local_url + '/win&FX={}&R=0&G=128&B=0&R2=255&G2=0&B2=0'.format(XmasFx))
# if today is not Halloween or Christmas time script sends a new post request with one of the random effect and random colors
        elif turned:
            requests.post(local_url + '/win&FX={}&SX=100&IX=150&R={}&G={}&B={}'.format(randomfx, r, g, b))
# waits for 60secs before calling func again
        time.sleep(60)
        Changer()
# exception for the poor Internet connection
    except ConnectionError:
        time.sleep(5)
        Changer()

Changer()