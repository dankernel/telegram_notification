
## Simply use in terminal
```
$ noti test!
```
➡️ `test!`

## Send image file 
```
$ noti image.png
```
➡️ `{image}`

## Extended use in terminal
```
$ sleep 10; echo "Done" | noti
```
➡️ `Done!`

## Used in bash script

in script.sh
```
sleep 10
echo "Done"
noti Done!
```
run `bash script.sh`
➡️ `Done!`

## use in python
```
import telegram_notification
telegram = telegram_notification.Telegram()

try:
    pass
    # some code..
except:
    telegram.notifications('Fail')
```
➡️ `Fail!`

