import requests

response = requests.get("https://api.github.com/users/dushyantsharma460")
print(response)                     # Should return <Response [200]>
print(response.json()['location']) # Correct way to access 'location'


response1 = requests.get("https://api.github.com")
print(response1.status_code)
