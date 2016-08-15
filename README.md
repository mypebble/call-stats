# Asternic Call Stats

This is a python script which will connect against PBX In a Flash
and get call stats to your users

This is designed to be customisable, with more documentation to follow.

### Installation

Install Python 2.7 and pip, then run:

        pip install -r requirements.txt

### Settings

Copy local_settings.py.blank and replace the
variables with your actual setup.

If you have Asterisk/FreePBX with a login page and not the system
popup, in order to get call stats you will have to get the
system to login.

Set the config with:

        PBX_LOGIN_PAGE = True

### Running

An example called `monthly-stats.py` is included. You
can write others scripts which will produce different reports.

        python monthly-stats.py
