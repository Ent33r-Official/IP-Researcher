from telegram.ext import Updater
import logging
import os

TOKEN = 'TOKEN'

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

up = Updater(TOKEN, use_context=True)
