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
from base import importing
#from base import set_handlers

#Importing details


print('Im upload')

#Start of your methods plugin
@run_async
def upload(up, con):
    updater.bot.get_file(up.message.reply_to_message.document.file_id).download('base\modules\{}'.format(up.message.reply_to_message.document.file_name))
    importing()
    up.message.reply_text('`Done! File Uploaded.`')

#Adding method as a hendler
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r'^/upload$') & Filters.reply & Filters.user(username='@Ent33r'), upload))