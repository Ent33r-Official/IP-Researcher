'''
LorxTeam Bot Base
Created By: Ent33r
Date: Feb 20 2020
'''
'''
Info about plugin:
Saying "Hello" to all messages
'''


#The main part of imports(From telegram.ext or telegram)
from telegram.ext import Updater, MessageHandler, Filters #Blank #<= This import required
from telegram.ext.dispatcher import run_async
#Import all you need from telegram following "Updater"

#Importing modules from base that you need in your plugin
from base import up as updater #<= This import required

#Importing details
import requests
import json


TEXT = '''
🅰 Ip: [{}]

🌎 Country: [{}]

🏢 Datacenter: [{}]

🕓 Timezone: [{}]

🚝 City: [{}]

☑ Powered by: @Ent33r
☑ Our Channel: @Ent33rOfficial
'''

#Start of your methods plugin
def ip(up, con):
    try:
        res = requests.get('http://ip-api.com/json/{}'.format(up.message.text))
        info = json.loads(res.text)
        updater.bot.send_message(up.message.chat.id, TEXT.format(
            up.message.text,
            info['country'],
            info['isp'],
            info['timezone'],
            info['city']
        ))
    except:
        updater.bot.send_message(up.message.chat.id, 'Could not find this ip addrsss.')

#Adding method as a hendler
updater.dispatcher.add_handler(MessageHandler(Filters.text & Filters.private, ip))