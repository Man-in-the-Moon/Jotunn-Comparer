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

MODE = 4
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

# All Raid Data
# Totals for all Raids
Raid_Tot_Kills = 0
Raid_Tot_Deaths = 0
Raid_Tot_Time = 0

# Total for specific raids
Levi_Start = 0
SotP_Start = 0
LW_Start = 0
GoS_Start = 0
DSC_Start = 0
VoG_Start = 0
Vow_Start = 0
KF_Start = 0
Root_Start = 0

Levi_Tot_Time = 0
SotP_Tot_Time = 0
LW_Tot_Time = 0
GoS_Tot_Time = 0
DSC_Tot_Time = 0
VoG_Tot_Time = 0
Vow_Tot_Time = 0
KF_Tot_Time = 0
Root_Tot_Time = 0

Levi_Tot_K = 0
SotP_Tot_K = 0
LW_Tot_K = 0
GoS_Tot_K = 0
DSC_Tot_K = 0
VoG_Tot_K = 0
Vow_Tot_K = 0
KF_Tot_K = 0
Root_Tot_K = 0

Levi_Tot_D = 0
SotP_Tot_D = 0
LW_Tot_D = 0
GoS_Tot_D = 0
DSC_Tot_D = 0
VoG_Tot_D = 0
Vow_Tot_D = 0
KF_Tot_D = 0
Root_Tot_D = 0

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
    raid_data_json = response.json()

    activities_len = len(raid_data_json["Response"]["activities"]) - 1

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
    items2 = data2["Response"]
    items3 = data3["Response"]
    items4 = data4["Response"]

    listitem = [items1, items2, items3, items4]
    finaljson = {"Response":[]}

    finaljson['Response'].append(items1)
    finaljson["Response"].append(items2)
    finaljson["Response"].append(items3)
    finaljson["Response"].append(items4)

    with open('raid_data.json', "w") as f:
        f.write(json.dumps(finaljson, indent=2))

    raid_data_json = finaljson
    activities_len = len(raid_data_json["Response"][0]['activities']) - 1

#for number in range(0, activities_len):
#    Raid_Name = raid_data_json["Response"]["activities"][number]["activityDetails"]["referenceId"]
#    Raid_Kills = raid_data_json["Response"]["activities"][number]["values"]["kills"]["basic"]["value"]
#    Raid_Deaths = raid_data_json["Response"]["activities"][number]["values"]["deaths"]["basic"]["value"]
#    Raid_KD = raid_data_json["Response"]["activities"][number]["values"]["killsDeathsRatio"]["basic"]["value"]
#    Raid_KAD = raid_data_json["Response"]["activities"][number]["values"]["killsDeathsAssists"]["basic"]["value"]
#    Raid_Time = raid_data_json["Response"]["activities"][number]["values"]["activityDurationSeconds"]["basic"]["value"]
#    Raid_PlayerCount = raid_data_json["Response"]["activities"][number]["values"]["playerCount"]["basic"]["value"]
#    Raid_Complete = raid_data_json["Response"]["activities"][number]["values"]["completed"]["basic"]["value"]



#     if Raid_Name == 2122313384:
#         LW_Tot_Time += Raid_Time
#         LW_Tot_K += Raid_Kills
#         LW_Tot_D += Raid_Deaths
#     elif Raid_Name == 3458480158 or Raid_Name == 2659723068:
#         GoS_Tot_Time += Raid_Time
#         GoS_Tot_K += Raid_Kills
#         GoS_Tot_D += Raid_Deaths
#     elif Raid_Name == 910380154:
#         DSC_Tot_Time += Raid_Time
#         DSC_Tot_K += Raid_Kills
#         DSC_Tot_D += Raid_Deaths
#     elif Raid_Name == 3881495763:
#         VoG_Tot_Time += Raid_Time
#         VoG_Tot_K += Raid_Kills
#         VoG_Tot_D += Raid_Deaths
#     elif Raid_Name == 1441982566:
#         Vow_Tot_Time += Raid_Time
#         Vow_Tot_K += Raid_Kills
#         Vow_Tot_D += Raid_Deaths
#     elif Raid_Name == 1374392663 or Raid_Name == 2964135793:
#         KF_Tot_Time += Raid_Time
#         KF_Tot_K += Raid_Kills
#         KF_Tot_D += Raid_Deaths
#     elif Raid_Name == 2381413764:
#         Root_Tot_Time += Raid_Time
#         Root_Tot_K += Raid_Kills
#         Root_Tot_D += Raid_Deaths
#     elif Raid_Name == 2693136601:
#         Levi_Tot_Time += Raid_Time
#         Levi_Tot_K += Raid_Kills
#         Levi_Tot_D += Raid_Deaths
#     elif Raid_Name == 548750096:
#         SotP_Tot_Time += Raid_Time
#         SotP_Tot_K += Raid_Kills
#         SotP_Tot_D += Raid_Deaths
#
#     if Raid_Name == 2122313384:
#         Raid_Name = "Last Wish"
#     elif Raid_Name == 3458480158 or Raid_Name == 2659723068:
#         Raid_Name = "Garden of Salvation"
#     elif Raid_Name == 910380154:
#         Raid_Name = "Deep Stone Crypt"
#     elif Raid_Name == 3881495763:
#         Raid_Name = "Vault of Glass"
#     elif Raid_Name == 1441982566:
#         Raid_Name = "Vow of the Disciple"
#     elif Raid_Name == 1374392663:
#         Raid_Name = "King's Fall"
#     elif Raid_Name == 2964135793:
#         Raid_Name = "King's Fall: Master"
#     elif Raid_Name == 2381413764:
#         Raid_Name = "Root of Nightmares"
#     elif Raid_Name == 2693136601:
#         Raid_Name = "Leviathan"
#     elif Raid_Name == 548750096:
#         Raid_Name = "Scourge of the Past"
#
#     if Raid_Complete == 0:
#         Raid_Complete = "Activity Incomplete"
#     else:
#         Raid_Complete = "Activity Complete"
#
#     if Raid_Deaths == 0 and Raid_Complete == 1:
#         Raid_Deaths = "Flawless"
#
#     Raid_Info = (Raid_Name, Raid_Kills, Raid_Deaths, Raid_KD, Raid_KAD, Raid_Time, Raid_PlayerCount, Raid_Complete)
#     #print(Raid_Info)
#
#     Raid_Tot_Kills += Raid_Kills
#     Raid_Tot_Deaths += Raid_Deaths
#     Raid_Tot_Time += Raid_Time
#
# print(Raid_Tot_Time, Raid_Tot_Kills, Raid_Tot_Deaths)
#
# Last_Wish = (LW_Tot_Time, LW_Tot_K, LW_Tot_D)
# Garden_of_Salv = (GoS_Tot_Time, GoS_Tot_K, GoS_Tot_D)
# Deep_Stone = (DSC_Tot_Time, DSC_Tot_K, DSC_Tot_D)
# Vault_of_Glass = (VoG_Tot_Time, VoG_Tot_K, VoG_Tot_D)
# Vow_Disciple = (Vow_Tot_Time, Vow_Tot_K, Vow_Tot_D)
# Kings_Fall = (KF_Tot_Time, KF_Tot_K, KF_Tot_D)
# Root_of_Night = (Root_Tot_Time, Root_Tot_K, Root_Tot_D)
#
# print(f"{Last_Wish} \n{Garden_of_Salv} \n{Deep_Stone} \n{Vault_of_Glass} \n{Vow_Disciple} \n{Kings_Fall} "
#       f"\n{Root_of_Night}")