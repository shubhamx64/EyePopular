import json
import re
from math import sin, cos, sqrt, atan2, radians
import copy

class Location:
    lat = 0.0
    lon = 0.0

    def __init__(self, lat):
        self.lat = lat
        self.lon = 0.0

    def __str__(self):
        toreturn = "Lat: " + str(self.lat) + " Long: " + str(self.lon)
        return toreturn

class ParkObj:
    tl = Location(0)
    tr = Location(0)
    bl = Location(0)
    br = Location(0)
    uid = 0.0

    def __init__(self, u, lat):
        self.tl.lat = Location(lat)
        self.uid = u
    
    def __str__(self):
        toreturn = "Uid: " +self.uid+" Lat: " + str(self.tl.lat) + " Long: " + str(self.tl.lon)
        return toreturn

with open("events.json", "r") as read_file:
    data = json.load(read_file)
inter = data['content'][0]['properties']['geoCoordinates']
pEvents = []
for cIndex in range(len(data['content'])):
    inter = data['content'][cIndex]['properties']['geoCoordinates']
    print(inter)
    tempList = re.findall(r"[-+]?\d*\.\d+|\d+", inter)
    tempPObj = ParkObj(data['content'][cIndex]['locationUid'], float(tempList[0]))
    tempPObj.tl.lon = float(tempList[1])
    pEvents.append(tempPObj)
    print(tempPObj)

print("Recorded: *******")
for p in pEvents:
    print(p)

class PopSearch:
    def __init__(self, propNum):
        self.props = [Location(0)] * propNum
        self.hardprops()

    def hardprops(self):
        self.props = [Location(0)]
        self.props[0].lat = 32.7477768
        self.props[0].lon = -117.1563164
        self.props[1].lat = 32.748451
        self.props[1].lon = -117.129517


    def setupProps(self):
        for i in range(propNum):
            s1 = "Enter lat of prop" + str(i) + " "
            lat1 = input(s1)
            s2 = "Enter lon of prop" + str(i) + " "
            lon1 = input(s2)
            self.props[i].lat = lat1
            self.props[i].lon = lon1

    def distbwgps(self, lat1, lon1, lat2,lon2):
        #1 - lat # 2 - lon
        print(lat2, lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        # approximate radius of earth in km
        R = 6373.0
        distance = R*c
        print("Result:", distance)

    def searchMostPopular2(self, pEve):
        for p in self.props:
            for peIndex in range(len(pEve)):
                print(pEve[peIndex].uid)
                self.distbwgps(p.lat, p.lon, pEve[peIndex].tl.lat, pEve[peIndex].tl.lon)

    def searchMostPopular(self, pEve):
        for p in self.props:
            print("New prop ****")
            for pe in pEve:
                print(pe.uid)
                self.distbwgps(p.lat, p.lon, pe.tl.lat, pe.tl.lon)

if __name__ == '__main__':
    runner = PopSearch(2)
    runner.searchMostPopular(pEvents)
        
