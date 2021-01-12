import requests as re

print(re.__version__)

google_resp = re.get('https://www.google.com')
print(google_resp)