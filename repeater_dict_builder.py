import repeater_utils
import json
import time

frequency_list = [
    145.110,
    145.170,
    145.230,
    145.290,
    145.310,
    145.390,
    145.430,
    145.450,
    146.670,
    146.700,
    146.820,
    146.850,
    146.925,
    147.000,
    147.030,
    147.060,
    147.165,
    147.180,
    147.210,
    147.270,
]

repeater_dict = {}

for frequency in frequency_list:
    print(frequency)
    repeater_data = repeater_utils.get_repeater_data(frequency)

    if repeater_data is not None:
        repeater = repeater_utils.return_repeater_in_search_area(repeater_data)
        repeater_dict[frequency] = {}
        repeater_dict[frequency]['callsign'] = repeater['Callsign']
        repeater_dict[frequency]['lat'] = repeater['Lat']
        repeater_dict[frequency]['lon'] = repeater['Long']
        repeater_dict[frequency]['distance'] = repeater_utils.get_distance(repeater)
        repeater_dict[frequency]['bearing'] = repeater_utils.get_bearing(repeater)

    with open('repeater_dict.json', 'w') as f:
        f.write(json.dumps(repeater_dict))

    time.sleep(60)
    
print(repeater_dict)



