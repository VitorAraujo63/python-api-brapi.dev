import requests
 
url = "https://brapi.dev/api/quote/list"
params = {
    'search': 'TR',
    'sortBy': 'close',
    'sortOrder': 'desc',
    'limit': '10',
    'sector': 'finance',
    'token': 'eJGEyu8vVHctULdVdHYzQd',
}
 
response = requests.get(url, params=params)
 
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
 