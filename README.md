# metalearning-inisiatif
metalearning-inisiatif

## model.pkl
model.pkl adalah compiled code python logic untuk ai

## myproject.py
myproject.py adalah code logic yang berisikan service endpoint

## myprojectenv
myprojectenv adalah libray Flask yang berisikan built in service untuk menjalankan project service API

## /etc/systemd/system/myproject.service
setup project untuk menjalankan autorun Nginx dan FlaskService

## configurasi project service

```
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app
```
