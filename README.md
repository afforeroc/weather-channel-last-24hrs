# Last weather conditions of a city using Weather Company API of IBM Cloud

## Description
Python app that show some weather conditions in the last 24 hours of a city using the weather company API rest of IBM Cloud.

## Prerequisites
Python >= v3.7.2

## Setup
Install all necessary dependencies for Python 3

Windows: `> .\setup-windows.ps1` <br>
Linux: `$ ./setup-linux.sh` <br>

## Execution app
Windows: `> python weather24.py` <br>
Linux: `$ python3 weather24.py` <br>

## Output example
<pre>
WEATHER LAST 24HRS
------------------
INPUT DATA
Input the city name: bogota
-----------
OUTPUT DATA
City: Bogota
Date: 2019-01-05_H00
Filename: Bogota_2019-01-05_H00
------------
OBSERVATIONS
date                   temp  wx_phrase               dewPt    rh    pressure    uv_index
-------------------  ------  --------------------  -------  ----  ----------  ----------
2019-01-04 02:00:00       8  Parcialmente nublado        6    87      752.53           0
2019-01-04 03:00:00       8  Parcialmente nublado        7    93      752.28           0
2019-01-04 04:00:00       8  Parcialmente nublado        7    93      752.28           0
2019-01-04 05:00:00       9  Parcialmente nublado        7    87      752.53           0
2019-01-04 05:30:00       9  Mayormente nublado          7    87      752.78           0
2019-01-04 06:00:00       9  Mayormente nublado          7    87      753.02           0
2019-01-04 07:00:00      11  Mayormente nublado          8    82      753.52           0
2019-01-04 08:00:00      12  Mayormente nublado          8    77      754.51           1
2019-01-04 09:00:00      14  Chubascos en la área        8    67      754.51           3
2019-01-04 10:00:00      15  Chubascos en la área        9    67      754.76           6
2019-01-04 11:00:00      18  Soleado                     8    52      754.02          12
2019-01-04 12:00:00      20  Soleado                     6    40      753.27          13
2019-01-04 13:00:00      20  Parcialmente nublado        6    40      752.53          10
2019-01-04 14:00:00      21  Parcialmente nublado        5    35      751.78           7
2019-01-04 15:00:00      21  Parcialmente nublado        5    35      751.53           4
2019-01-04 16:00:00      20  Parcialmente nublado        6    40      751.53           2
2019-01-04 17:00:00      18  Parcialmente nublado        7    49      751.78           0
2019-01-04 18:00:00      17  Parcialmente nublado        5    45      752.28           0
2019-01-04 19:00:00      16  Parcialmente nublado        9    63      752.53           0
2019-01-04 20:00:00      15  Despejado                   5    51      753.27           0
2019-01-04 21:00:00      11  Despejado                   6    71      753.77           0
2019-01-04 22:00:00      10  Despejado                   6    76      754.02           0
2019-01-04 23:00:00      10  Despejado                   6    76      754.02           0
2019-01-05 00:00:00       7  Despejado                   6    93      753.77           0
</pre>
