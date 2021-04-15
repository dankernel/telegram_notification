
import os
import sys
import socket
import telegram
import configparser
import argparse

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

config = None

def init(config) -> None:

    # Bot Token
    print('Enter your telegram bot token : ', end='')
    input_token = input()
    config.set('SERVER', 'token', input_token)
 
    TOKEN = config.get('SERVER', 'token')
    print('Enter /hello in the telegram : ', end='')
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()

def notifications(msg: str) -> None:

    msg = '[{}] {}'.format(HOST_NAME, msg)

    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=msg)

def hello(update: Update, context: CallbackContext) -> None:
    msg = f'{update.effective_user.first_name} user id : {update.effective_user.id}'
    print(msg)
    update.message.reply_text(msg)

def pipe_mode(head_strs: list) -> None:

    for line in sys.stdin:
        for head_str in head_strs:
            if line[:len(head_str)] == head_str:
                notifications(line)
 
def main():

    # Read config
    config = configparser.ConfigParser()
    config_file = os.path.join(os.getcwd(), 'config.ini')
    print('Read', config_file)
    config.read(config_file)

    if not config.has_option('SERVER', 'token') or not config.has_option('USER', 'chat_id'):
        print("TOKEN is NONE")
        init(config)

    TOKEN = config.get('SERVER', 'token')
    CHAT_ID = config.get('USER', 'chat_id')
    HOST_NAME = socket.gethostname()

    if len(sys.argv) == 1:
        pipe_mode(['noti', 'dkdk', 'test'])
    elif sys.argv[1] == 'init':
        init()
    elif len(sys.argv) == 2:
        notifications(sys.argv[1])


if __name__ == '__main__':
    main()

    
