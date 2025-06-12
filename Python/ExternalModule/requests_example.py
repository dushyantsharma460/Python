import requests

r = requests.get('https://api.github.com/users/dushyantsharma460')

# print(r.text)
with open("codewithduhyant.txt","w") as f:
    f.write(r.text)