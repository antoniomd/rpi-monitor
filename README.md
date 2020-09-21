# rpi-monitor
Raspberry Pi monitoring script

This project has different scripts:
    - rpi-monitor.sh: is a shell script adn show CPU temperature, use and frequency in the Terminal.
    - rpi-monitor.py: is a similar script that rpi-monitor.sh in Python.
    - rpi-monitorBot.py: this script sends a notification by Telegram's bot if the CPU temperature is higer than 80ºC or 85ºC.

Usage:
Modify auth.py's parameters with your info if you want to use rpi-monitorBot.py.
Run the script in your Raspebrry Pi.