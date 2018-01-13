#!/usr/bin/env bash

sudo apt-get install python3-setuptools
sudo easy_install3 pip
pip3 install mypackage --user
git clone https://github.com/yetinet/CreateArt.git
cd CreateArt
pip3 install -r CreateArt-Req.txt --user
sudo apt-get install python3-tk

