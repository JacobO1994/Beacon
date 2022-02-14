from geopy.geocoders import Nominatim

class Geolocator:

    def get_coordinates(location):
        geolocator = Nominatim(user_agent="App")
        location = geolocator.geocode(location)
        return (location.latitude, location.longitude)