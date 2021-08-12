
#!/usr/bin/env python3

import sys
from telegram_notification import Telegram


def main():

    telegram = Telegram("1602300000:AAHnXcDVGI0oYVfeWuHPsm1TGxxxxxxxxxx", "17880xxxxx")

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

