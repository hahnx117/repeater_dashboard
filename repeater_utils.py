import requests
import geopy.distance
from pprint import pprint
from geographiclib.geodesic import Geodesic

BASEURL = "https://www.repeaterbook.com/api"
COUNTY = "hennepin"
STATE = "minnesota"
SEARCH_THRESHHOLD = 25
HOME_LAT = 44.954539
HOME_LON = -93.290858

def get_repeater_data(frequency, state=None):
    if state is None:
        state = STATE
    url = f"{BASEURL}/export.php?state={state}&frequency={format(frequency, '.5f')}"

    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200 and response.json()['count'] > 0:
        return response.json()['results']
    else:
        return None

def return_repeater_in_search_area(repeater_data):
    for repeater in repeater_data:
        repeater_lat = repeater["Lat"]
        repeater_lon = repeater["Long"]
        distance = geopy.distance.geodesic((HOME_LAT, HOME_LON), (repeater_lat, repeater_lon)).miles
        if distance < SEARCH_THRESHHOLD:
            return repeater

    return None

def get_distance(repeater_data):
    repeater_lat = float(repeater_data['Lat'])
    repeater_lon = float(repeater_data['Long'])

    return geopy.distance.geodesic((HOME_LAT, HOME_LON), (repeater_lat, repeater_lon)).miles

def get_bearing(repeater_data):
    repeater_lat = float(repeater_data['Lat'])
    repeater_lon = float(repeater_data['Long'])

    bearing = Geodesic.WGS84.Inverse(HOME_LAT, HOME_LON, repeater_lat, repeater_lon)['azi1']

    if bearing < 0:
        bearing += 360
    
    return bearing
