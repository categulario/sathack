import requests
from requests.utils import dict_from_cookiejar
from base64 import b64decode
import json

def get_viewstate():
    res = requests.get('https://agsc.siat.sat.gob.mx/PTSC/ValidaRFC/index.jsf')

    lines = list(map(lambda x:x.strip(), res.text.split('\n')))
    for line in lines:
        if line.endswith('autocomplete="off" />'):
            viewstate = line.split()[6][7:-1]
            break

    return viewstate, res.cookies

if __name__ == '__main__':
    # 1 get the viewstate
    viewstate, cookiejar = get_viewstate()

    # 2 get the captcha
    res = requests.post('https://agsc.siat.sat.gob.mx/PTSC/ValidaRFC/captchaReload', cookies=cookiejar)

    with open('captcha.png', 'wb') as pngfile:
        pngfile.write(b64decode(res.text))

    with open('cookies.json', 'w') as cookiefile:
        json.dump(dict_from_cookiejar(cookiejar), cookiefile, indent=2)

    with open('viewstate.txt', 'w') as viewstatefile:
        viewstatefile.write(viewstate)
