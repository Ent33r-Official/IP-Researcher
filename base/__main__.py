'''
LorxTeam Bot Base
Created By: Ent33r
Date: Feb 20 2020
'''
'''
Info about plugin:
Its the main file
'''


#The main part of imports(From telegram.ext or telegram)
from telegram.ext import Updater #Blank #<= This import required
from telegram.ext.dispatcher import run_async
#Import all you need from telegram following "Updater"

#Another importing
import os

#Importing modules from base that you need in your plugin
from base import up, TOKEN #<= This import required

#Main File

#PORT = int(os.environ.get('PORT', '8443'))

#Working with up
#up.start_webhook(listen="0.0.0.0",
 #                     port=PORT,
 #                     url_path=TOKEN)

#print(up.dispatcher.handlers)
#up.bot.set_webhook("https://ipresearcher.herokuapp.com/" + TOKEN)
up.start_polling()
up.idle()
