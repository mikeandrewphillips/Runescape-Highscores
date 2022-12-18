import requests

response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=PhysFighter')
response_list = response.text.split("\n")
#print(response_list)

skill_list = ["Overall","Attack","Defense","Strength","Hitpoints","Ranged","Prayer","Magic","Cooking","Woodcutting","Fletching","Fishing","Firemaking","Crafting","Smithing","Mining","Herblore","Agility","Thieving","Slayer","Farming","Runecrafting","Hunter","Construction"]
print(len(skill_list))