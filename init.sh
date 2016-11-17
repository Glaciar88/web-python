sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
sudo ln -s /home/box/web/etc/ask.py   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
