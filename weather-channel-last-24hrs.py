import requests, json, csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime
from openpyxl import Workbook
from timezonefinder import TimezoneFinder
from pytz import timezone
from scipy.interpolate import interp1d
from geopy.geocoders import Nominatim
from tabulate import tabulate

tf = TimezoneFinder()
geolocator = Nominatim(user_agent="weather-last-24")

def printTitle(title):
    print("-" * len(title))
    print(title)
    print("-" * len(title))

def printSecondTitle(title):
    print("-" * len(title))
    print(title)

def getLocation(inputCity):
    location = geolocator.geocode(inputCity)
    return location

def getCurrentTime(lc):
    timeZone = tf.timezone_at(lng=lc.longitude, lat=lc.latitude)
    tz = timezone(timeZone)
    cDate = datetime.now(tz)
    return cDate

# Obtain data
def weather24(cred, location):
    line = 'https://'+cred[0]+':'+cred[1]+'@twcservice.mybluemix.net/api/weather/v1/geocode/'+f'{location.latitude}'+'/'+f'{location.longitude}'+'/observations/timeseries.json?&units=m&language=es&hours=23'
    r = requests.get(line)
    data  = json.loads(r.text)
    #print (json.dumps(data,indent=1))
    nameCity = data['observations'][0]['obs_name']
    return data, nameCity

def unix2date(ts):
    date = datetime.fromtimestamp(ts)
    return date

def getObservations(data):
    obsJSON = data['observations']
    observations = []
    for j in range(len(obsJSON)):
        conditions = []
        obs = obsJSON[j]
        date = unix2date(obs['valid_time_gmt'])
        temp = obs['temp']
        wx_phrase = obs['wx_phrase']
        dewPt = obs['dewPt']
        rh = obs['rh']
        pressure = obs['pressure']
        uv_index = obs['uv_index']
        conditions.extend((date, temp, wx_phrase, dewPt, rh, pressure, uv_index))
        observations.append(conditions)
    return observations

# Write a xlsx file
def save2xslx(filename, obsArray, headers):
    nameFile = f'{filename}.xlsx'
    wb = Workbook() 
    ws = wb.active # Grab the active worksheet
    ws.append(headers) # Rows can also be appended
    siz = len(obsArray)
    for j in range(siz):
        ws.append(tuple(obsArray[j,:]))   
    wb.save(nameFile)   # Save the file

# Write a csv file
def save2csv(city, cDate, obsArray, headers):
    nameFile = f'{filename}.csv'
    csvFile = open(nameFile, 'w+', newline='')
    siz = len(obsArray)
    try:
        writer = csv.writer(csvFile)
        writer.writerow(headers)
        for j in range(siz):
            writer.writerow(tuple(obsArray[j,:]))
    finally:
        csvFile.close()

# Plot date vs other value
def data2matplot(obs, city):
    listM = np.array(obs) # Convert list of list into array
    dateList = listM[:,0] # Obtain datetime
    tempList = listM[:,1] # Obtain temperatures

    #Plot with dates
    plt.subplots_adjust(bottom=0.2)
    plt.xticks( rotation=25 )
    ax=plt.gca()
    #xfmt = md.DateFormatter('%Y-%m-%d %H:%M')
    xfmt = md.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    plt.plot(dateList, tempList)

    # Legend and Labels
    plt.legend(['Temperatura de '+f'{city}'+' en las últimas horas'])
    plt.ylabel('Temperatura [°C]')
    plt.grid(True)
    plt.show()

# Weather Company Credentials
username="79d0822d-f48c-40f8-8808-8fac1defe2df"
password="XxeVJJ9XMU"
credentials = [username, password]

# Main function
printTitle("WEATHER LAST 24HRS")
print("INPUT DATA")
inputCity = input("Input the city name: ")

# Procesing data
location = getLocation(inputCity)
currentTime = getCurrentTime(location)
date = currentTime.strftime('%Y-%m-%d_H%H')
data, city = weather24(credentials, location)
filename = f'{city}_{date}'
observations = getObservations(data)
obsArray = np.array(observations) 

# Output data
printSecondTitle("OUTPUT DATA")
print("City:", city)
print("Date:", date)
print("Filename:", filename)

# Observations
printSecondTitle("OBSERVATIONS")
headers=['date', 'temp', 'wx_phrase', 'dewPt', 'rh', 'pressure', 'uv_index']
print(tabulate(obsArray, headers))
save2xslx(filename, obsArray, headers)
data2matplot(observations, city)