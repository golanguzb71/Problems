import requests

for i in range(1000):
    print(requests.get("http://46.101.118.208:8000/api/tests"))
