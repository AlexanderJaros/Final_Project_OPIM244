#import requests
#from bs4 import BeautifulSoup
#
#url = 'https://www.ssa.gov/cgi-bin/babyname.cgi'
#post_params = {'value': 'Alex', 'value': 'M'}
#response = requests.post(url, data=post_params)
#soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

import requests

request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
params = {"name": "Alex", "sex": "M"}
response = requests.post(request_url, params)
print(response.status_code)
print(response.text)
#breakpoint()
# todo:
# soup = BeautifulSoup(response.text)