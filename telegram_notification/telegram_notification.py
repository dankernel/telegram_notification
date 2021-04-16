
import os
import sys
import socket
import telegram
import configparser
import argparse
import pathlib

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


class Telegram:

    def __init__(self):
        config = None
        TOKEN = None
        CHAT_ID =  None
        HOST_NAME = None

        # Read config
        config = configparser.ConfigParser()
        # config_file = os.path.join(os.getcwd(), 'telegram_notification/config.ini')
        config_file = os.path.join(pathlib.Path(__file__).parent.absolute(), 'config.ini')
        print('Read', config_file)
        config.read(config_file)

        if not config.has_option('SERVER', 'token') or not config.has_option('USER', 'chat_id'):
            print("TOKEN is NONE")
            self.ini_init(config)

        self.TOKEN = config.get('SERVER', 'token')
        self.CHAT_ID = config.get('USER', 'chat_id')
        self.HOST_NAME = socket.gethostname()

    def ini_init(self, config) -> None:

        # Bot Token
        print('Enter your telegram bot token : ', end='')
        input_token = input()
        config.set('SERVER', 'token', input_token)
     
        self.TOKEN = config.get('SERVER', 'token')
        print('Enter /hello in the telegram : ', end='')
        updater = Updater(self.TOKEN)

        updater.dispatcher.add_handler(CommandHandler('hello', self.hello))
        updater.start_polling()
        updater.idle()

    def notifications(self, msg: str) -> None:

        bot = telegram.Bot(token=self.TOKEN)

        if os.path.isfile(msg):
            bot.send_photo(chat_id=self.CHAT_ID, photo=open(msg, 'rb'))
        else:
            msg = '[{}] {}'.format(self.HOST_NAME, msg)
            bot.send_message(chat_id=self.CHAT_ID, text=msg)

    def hello(self, update: Update, context: CallbackContext) -> None:
        msg = f'{update.effective_user.first_name} user id : {update.effective_user.id}'
        print(msg)
        update.message.reply_text(msg)

    def pipe_mode(self, head_strs: list) -> None:

        for line in sys.stdin:
            for head_str in head_strs:
                if line[:len(head_str)] == head_str:
                    self.notifications(line)
 
def main():

    telegram = Telegram()

    if len(sys.argv) == 1:
        telegram.pipe_mode(['noti', 'dkdk', 'test'])
    elif sys.argv[1] == 'init':
        telegram.ini_init()
    elif len(sys.argv) == 2:
        telegram.notifications(sys.argv[1])

if __name__ == '__main__':
    main()

