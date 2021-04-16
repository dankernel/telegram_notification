
import sys
from telegram_notification import Telegram

def __main__():

    telegram = Telegram()

    if len(sys.argv) == 1:
        telegram.pipe_mode(['noti', 'dkdk', 'test'])
    elif sys.argv[1] == 'init':
        telegram.ini_init()
    elif len(sys.argv) == 2:
        telegram.notifications(sys.argv[1])

    main()

if __name__ == '__main__':
    __main__()

