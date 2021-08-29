# -*- coding: utf-8 -*-

"""
rpi-monitor.py

The script gets CPU temperature, use and frequency.

Then these parameters can be viewed in the Terminal. This scrip send a Telegram message when the temperature is too high.

Usage:
Clone the repository. Update config.auth with your token and user Telegram ID.

Run rpi-monitor.py in your RPi. Maybe, psutil must be installed.
"""

# Importo las librerias
import subprocess, psutil, requests, time

# Importo la configuración del fichero
from config.auth import *


# Envía un mensaje a través de Telegram
def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + userTelegramID + '&parse_mode=Markdown&text=' + bot_message
    requests.post(send_text)

def main():
    """    
    # Obtengo la Tª de la CPU
    tempFile = open('/sys/class/thermal/thermal_zone0/temp', 'r')
    cpuTemp = float(tempFile.read())/1000
    tempFile.close()

    # Obtengo el % de uso de la CPU
    cpuUse = psutil.cpu_percent(interval=1, percpu=False)
    
    # Obtengo la frecuencia de la CPU
    freqFile = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r')
    cpuFreq = float(freqFile.read())/1000
    freqFile.close()
    
    # Muestra en el Terminal la información
    print('Temperatura CPU => ' + str(int(cpuTemp)) + ' ºC')
    print('Uso de la CPU => ' + str(cpuUse) + ' %')
    print('Frecuencia CPU => ' + str(cpuFreq) + ' MHz')
    """

    warningTemp = tripTemp = 0
    cpuTemp = 81

    # telegram_bot_sendtext('prueba')

    while True:
        print('prueba')
        if cpuTemp <= 80 and warningTemp == 1:
            print('La temperatura de la CPU es inferior a 80ºC')
            telegram_bot_sendtext('La temperatura de la CPU es inferior a 80ºC')
            warningTemp = 0
        elif cpuTemp > 80 and cpuTemp <= 85 and warningTemp == 0:
            print('La temperatura de la CPU es superior a 80ºC')
            telegram_bot_sendtext('La temperatura de la CPU es superior a 80ºC')
            warningTemp = 1
            tripTemp = 0
        elif cpuTemp > 85 and tripTemp == 0:
            print('La temperatura de la CPU es superior a 85ºC')
            telegram_bot_sendtext('La temperatura de la CPU es superior a 85ºC')
            tripTemp = 1      
        time.sleep(60)  

    """
    # Gestión alarmas de temperatura
    if cpuTemp >= 80 and cpuTemp < 85:
        if warningTemp is False:
	    message = 'La temperatura de la CPU de nuestra Raspberry ha alcanzado los 80ºC'
            telegram_bot_sendtext(message)
            warningTemp = True
    elif cpuTemp >= 85:
        if tripTemp is False:
            message = 'La temperatura de la CPU de nuestra Raspberry ha alcanzado los 85ºC'
	    telegram_bot_sendtext(message)
            tripTemp = True
    elif cpuTemp < 85:
        tripTemp = False
    elif cpuTemp < 80:
        warningTemp = False
    """

if __name__ == "__main__":
	main()
