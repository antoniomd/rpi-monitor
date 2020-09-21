#!/bin/bash

cpuTemp=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuFreq=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "Temperatura de la CPU => $((cpuTemp/1000)) ºC"
echo "Frecuencia de la CPU => $((cpuFreq/1000)) Hz"
echo "-------------------------------------------"
