
echo -e "\e[32mInstall shell script"

echo -e "\e[32mInstall shell script ok.."

echo -e "\e[34mRun the following command in terminal:"
echo -e "\e[37m $ vim ~/bash/notifications/config_sample.ini"
echo -e "\e[34mAnd" 
echo -e "\e[37m $ cp ~/bash/notifications/config_sample.ini bash/notifications/config.ini"

echo "alias noti='python3 $(pwd)/telegram_main.py'"  >> ~/.bashrc
