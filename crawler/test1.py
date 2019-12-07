import requests

url = "http://google.co.kr";

req = requests.get( url );

html = req.text;

print( html );