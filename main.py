import repeater_utils
import geopy.distance
from pprint import pprint


if __name__ == "__main__":
    while True:
        user_input = float(input("Enter a frequency: "))

        repeater_data = repeater_utils.get_repeater_data(user_input)

        if repeater_data is not None:

            repeater = repeater_utils.return_repeater_in_search_area(repeater_data)

            pprint(repeater)
            print(f"Distance: {geopy.distance.geodesic((repeater_utils.HOME_LAT, repeater_utils.HOME_LON), (repeater['Lat'], repeater['Long'])).miles:.2f} miles.")
            print(f"Bearing: {repeater_utils.get_bearing(repeater):.2f} degrees.")
            print("")
        else:
            print(f"No repeaters found on {user_input:.5f}")
            print("")

