import requests
print(requests.__version__)

r = requests.get("http://www.google.com")
#print(r.status_code)
#print(r.text)

a = requests.get("https://raw.githubusercontent.com/amalik2/CMPUT-404-Lab-1/master/lab1.py")
print(a.text)