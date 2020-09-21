# -*- coding: utf-8 -*-

"""
rpi-monitor.py

The script gets CPU temperature, use and frequency.

Then these parameters can be viewed in the Terminal.

Usage:
Clone the repository.

Run rpi-monitor.py in your RPi. Maybe, you must install psutil.
"""

# Importo las librerias
import subprocess, psutil

def main():
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
    print('Frecuencia CPU => ' + str(cpuFreq) + ' Hz')

    # Gestión alarmas de temperatura
    warningTemp = tripTemp = False
    if cpuTemp > 80:
        warningTemp = True
    elif cpuTemp > 85:
        tripTemp = True



if __name__ == "__main__":
	main()
