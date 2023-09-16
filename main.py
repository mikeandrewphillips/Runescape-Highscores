import requests
import json

def get_highscores(username):
    response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='+username)
    response_list = response.text.split("\n")
    skill_names = ["Overall","Attack","Defense","Strength","Hitpoints","Ranged","Prayer","Magic","Cooking","Woodcutting","Fletching","Fishing","Firemaking","Crafting","Smithing","Mining","Herblore","Agility","Thieving","Slayer","Farming","Runecrafting","Hunter","Construction"]
    skill_values = response_list[0:24]
    skill_dictionary = dict(zip(skill_names,skill_values))
    skill_dictionary = {k:v.split(",") for k,v in skill_dictionary.items()}
    return skill_dictionary

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(get_highscores("PhysFighter"))
    }
