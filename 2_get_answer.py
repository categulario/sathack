import requests
from requests.utils import cookiejar_from_dict
import json

if __name__ == '__main__':
    with open('cookies.json', 'r') as cookiefile:
        cookiejar = cookiejar_from_dict(json.load(cookiefile))

    with open('viewstate.txt', 'r') as viewstatefile:
        viewstate = viewstatefile.read().strip()

    captchasolution = input('Captcha: ')

    res = requests.post('https://agsc.siat.sat.gob.mx/PTSC/ValidaRFC/index.jsf', cookies=cookiejar, data={
        'formMain': 'formMain',
        'formMain:captchaInput': captchasolution,
        'formMain:j_idt57': 'formMain:j_idt57',
        'javax.faces.partial.ajax': 'true',
        'javax.faces.partial.execute': '@all',
        'javax.faces.partial.render': 'formMain',
        'javax.faces.source': 'formMain:j_idt57',
        'javax.faces.ViewState': viewstate,
    })
    # Hasta aquí todo funciona

    # TODO validar que la respuesta sea afirmativa
    rfc = 'pollo'

    res = requests.post('https://agsc.siat.sat.gob.mx/PTSC/ValidaRFC/index.jsf', cookies=cookiejar, data={
        'formMain': 'formMain',
        'formMain:consulta': '',
        'formMain:valRFC': rfc,
        'javax.faces.ViewState': viewstate,
    })

    # TODO validar que la respuesta sea afirmativa

    with open('sol.html', 'w') as solfile:
        if 'incorrecta' in res.text:
            print('incorrecta')
        elif 'válida':
            print('correcta')
        else:
            print('salió mal todo')
