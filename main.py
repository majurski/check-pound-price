import json
from time import sleep
import ssl 

ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen

with urlopen("https://forex.1forge.com/1.0.3/quotes?pairs=GBPEUR,&api_key=pgLpTX44r4PBCj1qMlbjVXkXO7NlGOkY") as response:
   source = response.read()

data = json.loads(source)


#while True:
# sleep(1)
#  with open("/storage/sdcard0/qpython/curency.txt","w") as f:
#      f.write(data)
print(json.dumps(data, indent=2))

pricenow = data[0]["price"]

def future(amount):
    amount = int(amount*pricenow)
    return amount

print(future(25000))