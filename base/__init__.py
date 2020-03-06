from telegram.ext import Updater
import logging
import os

TOKEN = '1084877238:AAFpKmuVcjsfUx-ZJOr_segR-EW72RdxIdQ'

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

up = Updater(TOKEN, use_context=True)
