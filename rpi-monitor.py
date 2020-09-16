#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bullsAndCowsBot.py

The script gets CPU and GPU temperatura and CPU uses.

Then these parameters can be view in the Terminal.

Usage:
Clone the repository.

Run rpi-monitor.py in your RPi.
"""

# Importo las librerias
import commands, psutil

def main():
    # Obtiene la Tª de la CPU y de la GPU
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    tempgpu = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp' ).replace('temp=', '' ).replace(''C', '')

    # Obtiene el uso de la CPU
    cpusan = psutil.cpu_percent(interval=1, percpu=False)

    # Muestra en el Terminal la temperatura de la CPU, la teperatura de la GPU y el porcentaje de uso de la CPU
    print 'Temp.CPU =>' + str(temp)
    print 'Temp.GPU =>' + str(tempgpu)
    print cpusan

if __name__ == "__main__":
	main()