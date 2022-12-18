import requests

response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=PhysFighter')
response_array = response.text.split("\n")
print(response_array)