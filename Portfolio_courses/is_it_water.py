import requests
# "api_key is not defined"
api_key = "sike"
# curl 'https://isitwater-com.p.rapidapi.com/?latitude=41.9029192&longitude=-70.2652276&rapidapi-key=YOUR-X-RAPIDAPI-KEY'
url = "https://isitwater-com.p.rapidapi.com/"
params = { "rapidapi-key" : api_key,
			"latitude" : "41.9019192",
			"longitude" : "-70.2652276"
}
response = requests.get(url, params)

data = response.json()
print(data)