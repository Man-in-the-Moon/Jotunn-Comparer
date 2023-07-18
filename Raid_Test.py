import os
import requests
import json

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://jotncomparer.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token"

# membershipType: Designates what machine the player uses. This number comes from the first device the account is set
# on. 1 - Xbox, 2- Playstation, 3 - Steam
# destinyMembershipId: The actual user account
# characterId: The specific character (Titan/Warlock/Hunter) that is used by the membership account
# Man in the Moon - Connor
membershipType = 1
destinyMembershipId = 4611686018450697084
characterId = 2305843009644414176

# The Chrome Leaf - Thomas
# membershipType = 1
# destinyMembershipId = 4611686018444441571
# Warlock:
# characterId = 2305843009265786295
# Titan:
# characterId = 2305843009283965144
# Hunter:
# characterId = 2305843009569534739

# MODE Numbers: 4 = Raids, 82 = Dungeons
# COUNT Limit: 250 per PAGE
# PAGE LIMIT: unknown

MODE = 82
COUNT = 250
PAGE = 0

test_url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={PAGE}"

payload = {}
headers = {
    'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
}

test_response = requests.request("GET", test_url, headers=headers, data=payload)
test_response_json = test_response.json()

test_activities_len = len(test_response_json["Response"]["activities"]) - 1


# Determines how large the test json file is. This will allow you to then determine if one json file is enough to
# acquire all available data or will more be necessary
def Length_Counter():
    if test_activities_len % 249 == 0:
        return True
    else:
        return False


# If the first .json is smaller than the page limit, create the active .json file for all operations to be performed on.
if not Length_Counter():
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={PAGE}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    pretty_raid_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('raid_data.json', 'w')
    writeFile.write(pretty_raid_data)
    writeFile.close

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()

# If the first page is longer than the page limit, create five .json files to and combine them to collect all the data
# Then proceeds to combine all .json files into one "mega"-file.
if Length_Counter():
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={PAGE}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    pretty_raid_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('raid_data_1.json', 'w')
    writeFile.write(pretty_raid_data)
    writeFile.close

    url2 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={1}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response2 = requests.request("GET", url2, headers=headers, data=payload)
    response2.content.decode('utf-8')
    pretty_raid_data2 = json.dumps(json.loads(response2.content), indent=2)
    writeFile = open('raid_data_2.json', 'w')
    writeFile.write(pretty_raid_data2)
    writeFile.close

    url3 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={2}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response3 = requests.request("GET", url3, headers=headers, data=payload)
    response3.content.decode('utf-8')
    pretty_raid_data3 = json.dumps(json.loads(response3.content), indent=2)
    writeFile = open('raid_data_3.json', 'w')
    writeFile.write(pretty_raid_data3)
    writeFile.close

    url4 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={3}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response4 = requests.request("GET", url4, headers=headers, data=payload)
    response4.content.decode('utf-8')
    pretty_raid_data4 = json.dumps(json.loads(response4.content), indent=2)
    writeFile = open('raid_data_4.json', 'w')
    writeFile.write(pretty_raid_data4)
    writeFile.close

    url5 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={4}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response5 = requests.request("GET", url5, headers=headers, data=payload)
    response5.content.decode('utf-8')
    pretty_raid_data5 = json.dumps(json.loads(response5.content), indent=2)
    writeFile = open('raid_data_5.json', 'w')
    writeFile.write(pretty_raid_data5)
    writeFile.close

    with open('raid_data_1.json.') as f:
        data1 = json.load(f)

    with open('raid_data_2.json') as f:
        data2 = json.load(f)

    with open('raid_data_3.json') as f:
        data3 = json.load(f)

    with open('raid_data_4.json') as f:
        data4 = json.load(f)

    items1 = data1['Response']
    items2 = data2["Response"]['activities']
    items3 = data3["Response"]
    items4 = data4["Response"]

    listitem = [items1, items2]
    finaljson = {"Response": []}

    finaljson["Response"].append(items1)
    finaljson['Response'].append(items2)


    with open('raid_data.json', "w") as f:
        f.write(json.dumps(finaljson, indent=2))

    raid_data_json = finaljson
    activities_len = len(raid_data_json["Response"][0]['activities']) - 1

print(activities_len)