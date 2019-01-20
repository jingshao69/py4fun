#!/bin/bash

sudo apt-get install -y apache2
sudo ufw app list
sudo ufw allow 'Apache Full'
sudo ufw status
sudo systemctl status apache2

