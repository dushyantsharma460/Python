# Request is an external Library 

import requests

#Before using this requests module you need to install this cmd

# pip install requests

# Request is the module which is used to fetch the html of online pages

r = requests.get("https://www.google.com/")

print(r.text)