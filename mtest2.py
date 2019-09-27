import json
import re
from math import sin, cos, sqrt, atan2, radians

class GPSCord:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat  = lat
        self.lon  = lon
    def __str__(self):
        toreturn = "Uid: " +self.name+" Lat: " + str(self.lat) + " Long: " + str(self.lon)
        return toreturn 

with open("events50K.json", "r") as read_file:
    data = json.load(read_file)
#print (data['content'][4425]['properties']['geoCoordinates'])
pEvents = []
for cIndex in range(len(data['content'])):
    #print(len(data['content']))
    #print (cIndex, data['content'][cIndex]['properties']['geoCoordinates'])
    try:
        inter = data['content'][cIndex]['properties']['geoCoordinates']
        #print(inter)
        tempList = re.findall(r"[-+]?\d*\.\d+|\d+", inter)
        tempPObj = GPSCord(data['content'][cIndex]['locationUid'], float(tempList[0]), float(tempList[1]))
        pEvents.append(tempPObj)
        #print(tempPObj)
    except:
        print(cIndex, "rejected")

print("Recorded: *******")
for p in pEvents:
    print(p)

class PopSearch:
    def __init__(self, propNum):
        #self.props = [GPSCord("OrgProp",0,0)] * propNum
        self.numProps = propNum
        self.props = []
        self.hardprops()

    def hardprops(self):
        lat1 = 32.7477768
        lon1 = -117.1563164
        lat2 = 32.748451
        lon2 = -117.129517
        self.props.append(GPSCord("1620 5th Ave - Restaurant", lat1, lon1))
        self.props.append(GPSCord("2877 University Ave - Restaurant", lat2, lon2))
        self.props.append(GPSCord("2540 Congress St - Restaurant",32.7515737 , -117.1947923))
        self.props.append(GPSCord("1050 Garnet Ave - Restaurant",32.7976548 , -117.250931))
        self.props.append(GPSCord("4480 Haines St - Restaurant", 32.799015, -117.242705 ))
        self.props.append(GPSCord("801-809 Market St - Restaurant", 32.711643,  -117.132042))

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
        #print(lat2, lon2)
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
        #print("Result:", distance)
        return distance

    def searchMostPopular(self, pEve, filterRad):
        eyes = [0] * self.numProps
        index = 0
        for p in self.props:
            print("Meow")
            for pe in pEve:
                #print(pe.name)
                d = self.distbwgps(p.lat, p.lon, pe.lat, pe.lon)
                if d <= (filterRad*1.05) :
                    eyes[index] += 1
            index += 1
        for e in range(len(eyes)):
            print(self.props[e].name, eyes[e], " per day")
        
        maxI = eyes.index(max(eyes))
        print("Suggestion: ", self.props[maxI].name, " with ", eyes[maxI], " visitors a day")


runner = PopSearch(6)
runner.searchMostPopular(pEvents,3)