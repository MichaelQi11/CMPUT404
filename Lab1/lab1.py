import requests as re

print(re.__version__)

google_resp = re.get('https://www.google.com')
print(google_resp)

code_resp = re.get('https://raw.github.com/MichaelQi11/CMPUT404/master/Lab1/lab1.py')
print(code_resp.text)