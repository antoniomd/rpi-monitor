# -*- coding: utf-8 -*-

"""
bullsAndCowsBot.py

The script gets CPU temperature and use.

Then these parameters can be view in the Terminal.

Usage:
Clone the repository.

Run rpi-monitor.py in your RPi.
"""

# Importo las librerias
import subprocess#, psutil

def main():
    # Obtiene la Tª de la CPU y de la GPU
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3

    # Obtiene el uso de la CPU
    # cpuUse = psutil.cpu_percent(interval=1, percpu=False)

    # Muestra en el Terminal la temperatura de la CPU, la teperatura de la GPU y el porcentaje de uso de la CPU
    print('Temp.CPU =>' + str(temp))
    # print(cpuUse)

if __name__ == "__main__":
	main()