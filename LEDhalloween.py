import requests
import random
import time
from requests.exceptions import ConnectionError

local_url = 'url'

def HalloweenChanger():
# var with a random effect from the list of necessary effects
    currentFx = random.choice([53, 77, 15, 78, 80, 106])
    try:
# checking if HomeAssistant's turned LED lights on
        turned = requests.get(local_url + '/json').json()['state']['on']
        if turned:
# sends new post request with one of the random effect. Also there are 2 Halloween permanent colors (orange(RGB2) and purple(RGB1))
            requests.post(local_url+'/win&FX={}&SX=100&IX=150&R=128&G=0&B=128&R2=255&G2=160&B2=0'.format(currentFx))
# waits for 60secs before calling func again
            time.sleep(60)
            HalloweenChanger()
# exception for the poor Internet connection
    except ConnectionError:
        time.sleep(5)
        HalloweenChanger()

HalloweenChanger()

