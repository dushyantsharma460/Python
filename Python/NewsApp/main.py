import requests  #pip install requests

query = input("What type of news are you interested in today? ")
api = "c476b5dbfd38486689c929cf20b42bbc"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-13&sortBy=publishedAt&apiKey={api}"
print(url)

r = requests.get(url)
data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(f"{index+1}. Title :- {article["title"]}\n")
    print(f"Check it out :- {article["url"]}\n")
    print(f"Desc :- {article["description"]}\n\n")
    print("*"*100)
    print("\n")


# Also fetch url like this 
# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-13&sortBy=publishedAt"

# headers = {
#     'x-api-key': 'c476b5dbfd38486689c929cf20b42bbc'
# }

# response = requests.get(url, headers=headers)
# print(response.json())
