import json
import socket, urllib3

def scraper(option_dict):
    print(option_dict)

    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.google.com')
    print(r.data)


if __name__== "__main__":

   # JSON Input for testing purposes

   test_json = {"name": "One Piece", "market": "Japan"}
   
   scraper(test_json)