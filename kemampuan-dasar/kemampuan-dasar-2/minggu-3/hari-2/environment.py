## 12 MEMBUAT ENVIRONMENT VIRTUAL

import sys
sys.path

# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ python3 -m venv tutorial-env
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ "/home/donie/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2/tutorial-env/bin/python" "/home/donie/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2/environment.py"
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ python3 -m pip install novas
# Collecting novas
#   Downloading novas-3.1.1.5.tar.gz (135 kB)
#      |████████████████████████████████| 135 kB 49 kB/s 
# Building wheels for collected packages: novas
#   Building wheel for novas (setup.py) ... done
#   Created wheel for novas: filename=novas-3.1.1.5-cp38-cp38-linux_x86_64.whl size=169858 sha256=4d9be45bdeb4490e22a28fb50badce0ffc566c6ff9f2917c251ff009cc6181ca
#   Stored in directory: /home/donie/.cache/pip/wheels/5f/3b/72/e7dba9d085106f46a87b5c1ce1405b6132fb10e343d8d312a0
# Successfully built novas
# Installing collected packages: novas
# Successfully installed novas-3.1.1.5
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip install requests==2.6.0
# Collecting requests==2.6.0
#   Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
#      |████████████████████████████████| 469 kB 27 kB/s 
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ python3 -m pip install --upgrade requests
# Collecting requests
#   Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)
#      |████████████████████████████████| 63 kB 223 kB/s 
# Collecting charset-normalizer~=2.0.0; python_version >= "3"
#   Downloading charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
# Requirement already satisfied, skipping upgrade: urllib3<1.27,>=1.21.1 in /usr/lib/python3/dist-packages (from requests) (1.25.8)
# Requirement already satisfied, skipping upgrade: idna<4,>=2.5; python_version >= "3" in /usr/lib/python3/dist-packages (from requests) (2.8)
# Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests) (2019.11.28)
# Installing collected packages: charset-normalizer, requests
#   Attempting uninstall: requests
#     Found existing installation: requests 2.6.0
#     Uninstalling requests-2.6.0:
#       Successfully uninstalled requests-2.6.0
# Successfully installed charset-normalizer-2.0.12 requests-2.27.1
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip show requests
# Name: requests
# Version: 2.27.1
# Summary: Python HTTP for Humans.
# Home-page: https://requests.readthedocs.io
# Author: Kenneth Reitz
# Author-email: me@kennethreitz.org
# License: Apache 2.0
# Location: /home/donie/.local/lib/python3.8/site-packages
# Requires: idna, certifi, charset-normalizer, urllib3
# Required-by: conda
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip list
# Package               Version             
# --------------------- --------------------
# alabaster             0.7.8               
# apt-clone             0.2.1               
# apturl                0.5.2               
# Babel                 2.6.0               
# beautifulsoup4        4.8.2               
# blinker               1.4                 
# Brlapi                0.7.0               
# certifi               2019.11.28          
# chardet               3.0.4               
# charset-normalizer    2.0.12              
# click                 8.1.2               
# colorama              0.4.3               
# command-not-found     0.3                 
# conda                 4.3.16              
# configobj             5.0.6               
# cryptography          2.8                 
# cupshelpers           1.0                 
# dbus-python           1.2.16              
# defer                 1.0.6               
# distro                1.4.0               
# docopt                0.6.2               
# docutils              0.16                
# EditorConfig          0.12.2              
# entrypoints           0.3                 
# feedparser            5.2.1               
# Flask                 2.1.1               
# gitsome               0.8.0               
# grpcio                1.16.1              
# httplib2              0.14.0              
# idna                  2.8                 
# ifaddr                0.1.6               
# imagesize             1.2.0               
# IMDbPY                6.8                 
# importlib-metadata    4.11.3              
# itsdangerous          2.1.2               
# Jinja2                3.1.1               
# jsbeautifier          1.10.3              
# keyring               18.0.1              
# launchpadlib          1.10.13             
# lazr.restfulclient    0.14.2              
# lazr.uri              1.0.3               
# louis                 3.12.0              
# macaroonbakery        1.3.1               
# Mako                  1.1.0               
# MarkupSafe            2.1.1               
# nemo-emblems          5.2.0               
# netaddr               0.7.19              
# netifaces             0.10.4              
# novas                 3.1.1.5             
# numpydoc              0.7.0               
# oauthlib              3.1.0               
# onboard               1.4.1               
# packaging             20.3                
# PAM                   0.4.2               
# pexpect               4.6.0               
# Pillow                7.0.0               
# pip                   20.0.2              
# ply                   3.11                
# prompt-toolkit        2.0.10              
# protobuf              3.6.1               
# psutil                5.5.1               
# pycairo               1.16.2              
# pycosat               0.6.3               
# pycrypto              2.6.1               
# pycups                1.9.73              
# pycurl                7.43.0.2            
# Pygments              2.3.1               
# PyGObject             3.36.0              
# PyICU                 2.4.2               
# pyinotify             0.9.6               
# PyJWT                 1.7.1               
# pymacaroons           0.13.0              
# PyNaCl                1.3.0               
# pyparsing             2.4.6               
# pyparted              3.11.2              
# pyRFC3339             1.1                 
# python-apt            2.0.0+ubuntu0.20.4.7
# python-debian         0.1.36ubuntu1       
# python-magic          0.4.16              
# python-xapp           2.2.1               
# python-xlib           0.23                
# pytz                  2019.3              
# pyxdg                 0.26                
# PyYAML                5.3.1               
# reportlab             3.5.34              
# requests              2.27.1              
# requests-file         1.4.3               
# requests-unixsocket   0.2.0               
# roman                 2.0.0               
# ruamel.yaml           0.17.21             
# ruamel.yaml.clib      0.2.6               
# SecretStorage         2.3.1               
# setproctitle          1.1.10              
# setuptools            45.2.0              
# simplejson            3.16.0              
# six                   1.14.0              
# soupsieve             1.9.5               
# Sphinx                1.8.5               
# ssh-import-id         5.10                
# systemd-python        234                 
# tinycss2              1.0.2               
# tldextract            2.2.1               
# ubuntu-drivers-common 0.0.0               
# ufw                   0.36                
# Unidecode             1.1.1               
# urllib3               1.25.8              
# wadllib               1.3.3               
# wcwidth               0.1.8               
# webencodings          0.5.1               
# Werkzeug              2.1.1               
# wheel                 0.34.2              
# xkit                  0.0.0               
# xlrd                  1.1.0               
# xonsh                 0.9.13              
# youtube-dl            2021.4.26           
# zipp                  3.8.0               
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip install -r

# Usage:   
#   pip install [options] <requirement specifier> [package-index-options] ...
#   pip install [options] -r <requirements file> [package-index-options] ...
#   pip install [options] [-e] <vcs project url> ...
#   pip install [options] [-e] <local project path> ...
#   pip install [options] <archive url/path> ...
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip install novas
# Requirement already satisfied: novas in /home/donie/.local/lib/python3.8/site-packages (3.1.1.5)
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip install numpy
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ pip install numpy
# Collecting numpy
#   Downloading numpy-1.22.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
#      |████████████████████████████████| 16.8 MB 560 kB/s 
# Installing collected packages: numpy
# Successfully installed numpy-1.22.3
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/m
# an-dasar-2/minggu ke 3/hari 2$ pip freeze > requirements.txt
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ cat requirements.txt
# certifi==2021.10.8
# charset-normalizer==2.0.12
# idna==3.3
# novas==3.1.1.5
# numpy==1.22.3
# requests==2.27.1
# urllib3==1.26.9
# donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 2$ 