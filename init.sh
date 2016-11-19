sudo /etc/init.d/mysql start
#sudo mysql -uroot -e 'CREATE DATABASE IF NOT EXISTS db_ask DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/ask.py   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
