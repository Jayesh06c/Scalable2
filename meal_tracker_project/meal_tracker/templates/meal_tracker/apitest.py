import requests

query = '22 gram burger'
YOUR_API_KEY = "nKIDW5Xq3Fag7BaoDaqRVg==JwVLb1fVXFclI4k8"
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': YOUR_API_KEY})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)