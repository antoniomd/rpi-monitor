#!/bin/bash

cpu=$(cat /sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "Temperatura CPU => $((cpu/1000)) ºC"
echo "-------------------------------------------"