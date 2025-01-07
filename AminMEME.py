import urllib.request
import requests
import urllib

r = requests.get("https://meme-api.com/gimme")

rjson = r.json()

url = rjson["url"]
urllib.request.urlretrieve(url, "meme.png")