
import os
import sys
import socket
import telegram
import configparser
import argparse
import pathlib
import signal

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


class Telegram:

    def __init__(self):
        config = None
        TOKEN = None
        CHAT_ID =  None
        HOST_NAME = None

        self.updater = None

        # Read config
        self.config = configparser.ConfigParser()
        self.config_file = os.path.join(pathlib.Path(__file__).parent.absolute(), 'config.ini')
        self.config.read(self.config_file)

        print(self.config_file)

        if not self.config.has_option('SERVER', 'token') or not self.config.has_option('USER', 'chat_id'):
            print("\033[41mTOKEN is NONE\033[00m")
            self.ini_init()

        self.update_ini()

        if len(self.TOKEN) <= 0 or len(self.CHAT_ID) <= 0:
            print("\033[41mTOKEN is NONE\033[00m")
            self.ini_init()
    
        self.update_ini()

        print('TOKEN :', self.TOKEN)
        print('self.CHAT_ID :', self.CHAT_ID)
        print('self.HOST_NAME :', self.HOST_NAME)

    def update_ini(self):
        self.TOKEN = self.config.get('SERVER', 'token')
        self.CHAT_ID = self.config.get('USER', 'chat_id')
        self.HOST_NAME = socket.gethostname()

    def ini_init(self) -> None:

        # Bot Token
        print('\033[32mEnter your telegram bot token : \033[0m', end='')
        input_token = input()
        self.config.set('SERVER', 'token', str(input_token))

        # Set new Token
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
        self.config.read(self.config_file)
        self.TOKEN = self.config.get('SERVER', 'token')

        # User id
        print('\033[32mEnter /start in the telegram \033[0m')
        print('\033[32m(waiting..) \033[0m')

        self.updater = Updater(self.TOKEN)
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.start_polling()
        self.updater.idle()

    def notifications(self, msg: str) -> None:

        bot = telegram.Bot(token=self.TOKEN)

        if os.path.isfile(msg):
            bot.send_photo(chat_id=self.CHAT_ID, photo=open(msg, 'rb'))
        else:
            msg = '[{}] {}'.format(self.HOST_NAME, msg)
            bot.send_message(chat_id=self.CHAT_ID, text=msg)

    def start(self, update: Update, context: CallbackContext) -> None:
        msg = f'Checked your id {update.effective_user.id}'
        update.message.reply_text(msg)

        # Set new chat_id to ini file
        self.config.set('USER', 'chat_id', str(update.effective_user.id))
        print('Your chat_id is {}'.format(update.effective_user.id))
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

        print('\033[32mVerified your id. Please restart.\033[0m')

    def pipe_mode(self, head_strs: list=None) -> None:

        if head_strs is None:
            for line in sys.stdin:
                self.notifications(line)
        else:
            for line in sys.stdin:
                for head_str in head_strs:
                    if line[:len(head_str)] == head_str:
                        self.notifications(line)
 
def main():

    telegram = Telegram()

    if len(sys.argv) == 1:
        telegram.pipe_mode()
    elif sys.argv[1] == 'init':
        telegram.ini_init()
    elif len(sys.argv) == 2:
        telegram.notifications(sys.argv[1])

def __main__():
    main()

if __name__ == '__main__':
    main()

